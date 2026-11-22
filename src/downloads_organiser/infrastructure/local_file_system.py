"""@file
@brief The file system port implemented with the local disk.
"""

import shutil
from pathlib import Path


class LocalFileSystem:
    """@brief Reads and changes files on the local disk with `pathlib`."""

    def list_files(self, folder: Path) -> list[Path]:
        """@brief List the files directly inside a folder, sorted by name.

        @param folder The folder to list.
        @return The paths of the files; sub-folders are left out.
        """
        return sorted(path for path in folder.iterdir() if path.is_file())

    def exists(self, path: Path) -> bool:
        """@brief Tell whether a path exists.

        @param path The path to test.
        @return True when a file or folder is at the path.
        """
        return path.exists()

    def make_folder(self, folder: Path) -> None:
        """@brief Create a folder, with its parents, when it is missing.

        @param folder The folder to create.
        """
        folder.mkdir(parents=True, exist_ok=True)

    def move(self, source: Path, target: Path) -> None:
        """@brief Move a file.

        @param source The file to move.
        @param target The new path of the file.
        """
        shutil.move(source, target)

    def read_text(self, path: Path) -> str:
        """@brief Read a text file.

        @param path The file to read.
        @return The text of the file.
        """
        return path.read_text(encoding="utf-8")

    def write_text(self, path: Path, text: str) -> None:
        """@brief Write a text file, replacing it.

        @param path The file to write.
        @param text The text to store.
        """
        path.write_text(text, encoding="utf-8")

    def delete_file(self, path: Path) -> None:
        """@brief Delete a file.

        @param path The file to delete.
        """
        path.unlink()

    def remove_folder_if_empty(self, folder: Path) -> bool:
        """@brief Remove a folder only when nothing is inside it.

        @param folder The folder to remove.
        @return True when the folder was removed.
        """
        try:
            folder.rmdir()
        except OSError:
            return False
        return True
