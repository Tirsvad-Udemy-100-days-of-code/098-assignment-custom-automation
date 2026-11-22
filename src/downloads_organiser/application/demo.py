"""@file
@brief Creates a throw-away folder with sample files for trying the tool and for screenshots.
"""

from pathlib import Path

from downloads_organiser import constants
from downloads_organiser.application.ports import FileSystem


def create_demo_folder(folder: Path, file_system: FileSystem) -> list[Path]:
    """@brief Fill a folder with small sample files of many types.

    The files are made up, so nothing private is ever shown.

    @param folder The folder to fill; it is created when missing.
    @param file_system The file system to write to.
    @return The paths of the sample files, in creation order.
    """
    file_system.make_folder(folder)
    created: list[Path] = []
    for name in constants.DEMO_FILES:
        path = folder / name
        file_system.write_text(path, f"Sample file {name}\n")
        created.append(path)
    return created
