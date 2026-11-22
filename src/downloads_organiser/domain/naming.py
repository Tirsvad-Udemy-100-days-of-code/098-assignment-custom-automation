"""@file
@brief The rule that keeps a move from overwriting an existing file.
"""

from collections.abc import Callable
from pathlib import Path


def numbered_name(file_name: str, number: int) -> str:
    """@brief Insert a number before the extension: `photo.jpg` becomes `photo (1).jpg`.

    @param file_name The original file name.
    @param number The number to insert, from 1 upwards.
    @return The numbered file name.
    """
    path = Path(file_name)
    return f"{path.stem} ({number}){path.suffix}"


def free_path(wanted: Path, is_taken: Callable[[Path], bool]) -> Path:
    """@brief Find a path that is not taken, numbering the name when needed.

    @param wanted The path the file would like to have.
    @param is_taken Answers whether a path is already in use.
    @return `wanted` when it is free, otherwise the first free numbered path.
    """
    candidate = wanted
    number = 0
    while is_taken(candidate):
        number += 1
        candidate = wanted.with_name(numbered_name(wanted.name, number))
    return candidate
