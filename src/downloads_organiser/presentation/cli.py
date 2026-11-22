"""@file
@brief The command line of the Downloads organiser.
"""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import TextIO

from downloads_organiser import constants
from downloads_organiser.api import organise_folder, undo_last_run
from downloads_organiser.application.demo import create_demo_folder
from downloads_organiser.domain.models import Move
from downloads_organiser.infrastructure.local_file_system import LocalFileSystem

_COMMANDS = ("organise", "undo", "demo")


def _build_parser() -> argparse.ArgumentParser:
    """@brief Describe the commands and options.

    @return The argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="downloads-organiser",
        description="Sort the files of a folder into sub-folders by file type.",
    )
    commands = parser.add_subparsers(dest="command", metavar="{organise,undo,demo}")
    organise = commands.add_parser("organise", help="plan or apply the sorting (the default)")
    organise.add_argument("folder", nargs="?", type=Path, default=default_folder())
    organise.add_argument("--apply", action="store_true", help="move the files (default: dry run)")
    undo = commands.add_parser("undo", help="move the files of the last applied run back")
    undo.add_argument("folder", nargs="?", type=Path, default=default_folder())
    demo = commands.add_parser("demo", help="create a folder with sample files")
    demo.add_argument("folder", nargs="?", type=Path, default=Path("demo-downloads"))
    return parser


def default_folder() -> Path:
    """@brief Give the folder used when none is named.

    @return The Downloads folder of the current user.
    """
    return Path.home() / constants.DEFAULT_FOLDER_NAME


def _describe(move: Move, folder: Path) -> str:
    """@brief Write one move as a line of text.

    @param move The move to describe.
    @param folder The organised folder; paths are shown relative to it.
    @return A line like `report.pdf -> Documents/report.pdf`.
    """
    return f"  {move.source.relative_to(folder)} -> {move.target.relative_to(folder).as_posix()}"


def _run_organise(folder: Path, *, apply: bool, out: TextIO) -> int:
    """@brief Run the organise command.

    @param folder The folder to organise.
    @param apply True to move the files.
    @param out Where the output goes.
    @return The exit code.
    """
    if not folder.is_dir():
        out.write(f"Error: {folder} is not a folder.\n")
        return 2
    moves = organise_folder(folder, apply=apply)
    out.write(f"{'Moved' if apply else 'Plan for'} {folder}:\n")
    for move in moves:
        out.write(_describe(move, folder) + "\n")
    if not moves:
        out.write("  Nothing to move.\n")
    elif apply:
        out.write(f"Moved {len(moves)} files. Undo with: downloads-organiser undo {folder}\n")
    else:
        out.write(f"Dry run: {len(moves)} files would move. Add --apply to move them.\n")
    return 0


def _run_undo(folder: Path, out: TextIO) -> int:
    """@brief Run the undo command.

    @param folder The organised folder.
    @param out Where the output goes.
    @return The exit code.
    """
    if not folder.is_dir():
        out.write(f"Error: {folder} is not a folder.\n")
        return 2
    result = undo_last_run(folder)
    if not result.restored and not result.missing:
        out.write("Nothing to undo.\n")
        return 0
    out.write(f"Restored {len(result.restored)} files.\n")
    for move in result.missing:
        out.write(f"  Missing, left alone: {move.target.name}\n")
    return 0


def main(argv: Sequence[str] | None = None, out: TextIO | None = None) -> int:
    """@brief Run the command line.

    Without a command the tool organises, so `downloads-organiser DIR` is a dry run.

    @param argv The arguments without the program name; the process arguments when None.
    @param out Where the output goes; standard output when None.
    @return The exit code: 0 on success, 2 for a bad folder or bad arguments.
    """
    out = out or sys.stdout
    args_in = list(sys.argv[1:] if argv is None else argv)
    if args_in and args_in[0] not in (*_COMMANDS, "-h", "--help"):
        args_in.insert(0, "organise")
    parser = _build_parser()
    args = parser.parse_args(args_in or ["organise"])
    if args.command == "demo":
        created = create_demo_folder(args.folder, LocalFileSystem())
        out.write(f"Created {len(created)} sample files in {args.folder}\n")
        return 0
    if args.command == "undo":
        return _run_undo(args.folder, out)
    return _run_organise(args.folder, apply=args.apply, out=out)
