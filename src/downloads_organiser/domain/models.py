"""@file
@brief The data the organiser works with.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Move:
    """@brief One file that moves, or has moved, from a source path to a target path."""

    source: Path
    target: Path


@dataclass(frozen=True)
class UndoResult:
    """@brief What an undo run did."""

    restored: tuple[Move, ...]
    missing: tuple[Move, ...]
