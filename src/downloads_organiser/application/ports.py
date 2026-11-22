"""@file
@brief The file system operations the use cases need, as a port.
"""

from pathlib import Path
from typing import Protocol


class FileSystem(Protocol):
    """@brief What the use cases need from a file system."""

    def list_files(self, folder: Path) -> list[Path]:
        """@brief List the files directly inside a folder, sorted by name.

        @param folder The folder to list.
        @return The paths of the files; sub-folders are left out.
        """
        ...

    def exists(self, path: Path) -> bool:
        """@brief Tell whether a path exists.

        @param path The path to test.
        @return True when a file or folder is at the path.
        """
        ...

    def make_folder(self, folder: Path) -> None:
        """@brief Create a folder, with its parents, when it is missing.

        @param folder The folder to create.
        """
        ...

    def move(self, source: Path, target: Path) -> None:
        """@brief Move a file.

        @param source The file to move.
        @param target The new path of the file.
        """
        ...

    def read_text(self, path: Path) -> str:
        """@brief Read a text file.

        @param path The file to read.
        @return The text of the file.
        """
        ...

    def write_text(self, path: Path, text: str) -> None:
        """@brief Write a text file, replacing it.

        @param path The file to write.
        @param text The text to store.
        """
        ...

    def delete_file(self, path: Path) -> None:
        """@brief Delete a file.

        @param path The file to delete.
        """
        ...

    def remove_folder_if_empty(self, folder: Path) -> bool:
        """@brief Remove a folder only when nothing is inside it.

        @param folder The folder to remove.
        @return True when the folder was removed.
        """
        ...
