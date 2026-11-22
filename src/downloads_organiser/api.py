"""@file
@brief The plain function names of the assignment, wired to the local disk.

This module is the composition root: it is the one place where the use cases
meet the real file system.
"""

from pathlib import Path

from downloads_organiser.application import organise as use_cases
from downloads_organiser.domain.models import Move, UndoResult
from downloads_organiser.infrastructure.local_file_system import LocalFileSystem


def organise_folder(folder: str | Path, *, apply: bool = False) -> list[Move]:
    """@brief Sort the files of a folder into sub-folders by type.

    @param folder The folder to organise.
    @param apply True to move the files; False (the default) is a dry run.
    @return The planned moves for a dry run, or the moves made.
    """
    return use_cases.organise_folder(Path(folder), LocalFileSystem(), apply=apply)


def undo_last_run(folder: str | Path) -> UndoResult:
    """@brief Move the files of the last applied run back to where they were.

    @param folder The organised folder.
    @return The restored moves and the moves whose file was missing.
    """
    return use_cases.undo_last_run(Path(folder), LocalFileSystem())
