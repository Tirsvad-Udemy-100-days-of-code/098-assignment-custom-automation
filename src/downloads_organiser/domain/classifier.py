"""@file
@brief The rule that decides which folder a file belongs to.
"""

from pathlib import PurePath

from downloads_organiser import constants


def _build_lookup() -> dict[str, str]:
    """@brief Invert the folder table into an extension to folder lookup.

    @return A dictionary from extension (lower case, with dot) to folder name.
    """
    return {
        extension: folder
        for folder, extensions in constants.EXTENSION_FOLDERS.items()
        for extension in extensions
    }


_FOLDER_BY_EXTENSION = _build_lookup()


def folder_for(file_name: str) -> str:
    """@brief Choose the target folder of a file from its extension.

    The comparison ignores case, so `Photo.JPG` goes where `photo.jpg` goes.

    @param file_name The name of the file, with or without a directory.
    @return The folder name, or the unknown folder when no rule matches.
    """
    extension = PurePath(file_name).suffix.lower()
    return _FOLDER_BY_EXTENSION.get(extension, constants.UNKNOWN_FOLDER)


def is_partial_download(file_name: str) -> bool:
    """@brief Tell whether a file is a download that has not finished.

    @param file_name The name of the file.
    @return True when the suffix marks an unfinished download.
    """
    return PurePath(file_name).suffix.lower() in constants.PARTIAL_DOWNLOAD_SUFFIXES
