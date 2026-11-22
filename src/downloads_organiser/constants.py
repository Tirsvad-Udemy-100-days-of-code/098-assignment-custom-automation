"""@file
@brief All constants of the Downloads organiser.

The rules that decide where a file goes live here, so they can be changed in
one place without touching the logic.
"""

from typing import Final

## @brief Folder name for files whose extension has no rule.
UNKNOWN_FOLDER: Final[str] = "Other"

## @brief Target folder and the file extensions (lower case, with dot) it holds.
EXTENSION_FOLDERS: Final[dict[str, tuple[str, ...]]] = {
    "Images": (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"),
    "Documents": (".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf", ".md", ".epub"),
    "Spreadsheets": (".xls", ".xlsx", ".ods", ".csv"),
    "Presentations": (".ppt", ".pptx", ".odp", ".key"),
    "Archives": (".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz"),
    "Audio": (".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac"),
    "Video": (".mp4", ".mkv", ".mov", ".avi", ".webm", ".wmv"),
    "Installers": (".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"),
    "Code": (".py", ".js", ".ts", ".json", ".html", ".css", ".c", ".cpp", ".cs"),
}

## @brief Name of the undo log written into the organised folder.
UNDO_LOG_NAME: Final[str] = ".downloads-organiser-undo.json"

## @brief Suffixes of files that are still being downloaded; they are never moved.
PARTIAL_DOWNLOAD_SUFFIXES: Final[tuple[str, ...]] = (".crdownload", ".part", ".tmp", ".download")

## @brief Folder organised when the command line gets no folder argument.
DEFAULT_FOLDER_NAME: Final[str] = "Downloads"

## @brief Number of sample files per type in the demo folder.
DEMO_FILES: Final[tuple[str, ...]] = (
    "holiday.jpg", "logo.png", "report.pdf", "notes.txt", "budget.xlsx",
    "slides.pptx", "backup.zip", "song.mp3", "clip.mp4", "setup.exe",
    "script.py", "mystery.xyz",
)
