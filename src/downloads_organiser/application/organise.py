"""@file
@brief The use cases: plan the moves, apply them, and undo the last run.
"""

import json
from pathlib import Path

from downloads_organiser import constants
from downloads_organiser.application.ports import FileSystem
from downloads_organiser.domain.classifier import folder_for, is_partial_download
from downloads_organiser.domain.models import Move, UndoResult
from downloads_organiser.domain.naming import free_path

_LOG_VERSION = 1


def _is_candidate(path: Path) -> bool:
    """@brief Tell whether a file may be moved.

    Hidden files, the undo log and unfinished downloads stay where they are.

    @param path The file to test.
    @return True when the file is a candidate for a move.
    """
    name = path.name
    if name.startswith("."):
        return False
    return name != constants.UNDO_LOG_NAME and not is_partial_download(name)


def plan_moves(folder: Path, file_system: FileSystem) -> list[Move]:
    """@brief Work out where each file of a folder would go, without moving anything.

    @param folder The folder to organise.
    @param file_system The file system to read from.
    @return The planned moves; a target never equals an existing path.
    """
    claimed: set[Path] = set()

    def is_taken(path: Path) -> bool:
        return path in claimed or file_system.exists(path)

    moves: list[Move] = []
    for source in file_system.list_files(folder):
        if not _is_candidate(source):
            continue
        wanted = folder / folder_for(source.name) / source.name
        target = free_path(wanted, is_taken)
        claimed.add(target)
        moves.append(Move(source, target))
    return moves


def apply_moves(folder: Path, moves: list[Move], file_system: FileSystem) -> list[Move]:
    """@brief Carry out planned moves and write the undo log.

    A target that was taken since the plan was made gets a numbered name, so
    nothing is overwritten.

    @param folder The organised folder; the undo log is written here.
    @param moves The moves to carry out.
    @param file_system The file system to change.
    @return The moves that were made, with their final targets.
    """
    made: list[Move] = []
    for move in moves:
        target = free_path(move.target, file_system.exists)
        file_system.make_folder(target.parent)
        file_system.move(move.source, target)
        made.append(Move(move.source, target))
    if made:
        _write_log(folder, made, file_system)
    return made


def _write_log(folder: Path, made: list[Move], file_system: FileSystem) -> None:
    """@brief Store the moves so that the run can be undone.

    @param folder The organised folder.
    @param made The moves that were made.
    @param file_system The file system to write to.
    """
    log_path = folder / constants.UNDO_LOG_NAME
    runs: list[list[dict[str, str]]] = []
    if file_system.exists(log_path):
        runs = json.loads(file_system.read_text(log_path))["runs"]
    runs.append([{"source": str(m.source), "target": str(m.target)} for m in made])
    _store_runs(log_path, runs, file_system)


def _store_runs(log_path: Path, runs: list[list[dict[str, str]]], file_system: FileSystem) -> None:
    """@brief Write the runs of the undo log.

    @param log_path The undo log file.
    @param runs The applied runs, oldest first, each a list of source and target paths.
    @param file_system The file system to write to.
    """
    document = {"version": _LOG_VERSION, "runs": runs}
    file_system.write_text(log_path, json.dumps(document, indent=2))


def organise_folder(folder: Path, file_system: FileSystem, *, apply: bool = False) -> list[Move]:
    """@brief Sort the files of a folder into sub-folders by type.

    By default this is a dry run: the moves are planned and nothing changes.

    @param folder The folder to organise.
    @param file_system The file system to use.
    @param apply True to carry out the moves, False for a dry run.
    @return The planned moves for a dry run, or the moves made.
    """
    moves = plan_moves(folder, file_system)
    return apply_moves(folder, moves, file_system) if apply else moves


def undo_last_run(folder: Path, file_system: FileSystem) -> UndoResult:
    """@brief Move the files of the last applied run back to where they were.

    A file that was moved away or deleted since is reported as missing. A file
    that has taken the old place is not overwritten: the restored file gets a
    numbered name.

    @param folder The organised folder that holds the undo log.
    @param file_system The file system to change.
    @return The restored moves and the moves whose file was missing.
    """
    log_path = folder / constants.UNDO_LOG_NAME
    if not file_system.exists(log_path):
        return UndoResult((), ())
    data = json.loads(file_system.read_text(log_path))
    runs: list[list[dict[str, str]]] = data["runs"]
    last = [Move(Path(m["source"]), Path(m["target"])) for m in runs.pop()]
    restored: list[Move] = []
    missing: list[Move] = []
    for move in reversed(last):
        if not file_system.exists(move.target):
            missing.append(move)
            continue
        destination = free_path(move.source, file_system.exists)
        file_system.move(move.target, destination)
        file_system.remove_folder_if_empty(move.target.parent)
        restored.append(Move(move.target, destination))
    if runs:
        _store_runs(log_path, runs, file_system)
    else:
        file_system.delete_file(log_path)
    return UndoResult(tuple(restored), tuple(missing))
