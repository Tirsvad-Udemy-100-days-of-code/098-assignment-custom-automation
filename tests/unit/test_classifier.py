"""Tests of the classification and naming rules."""

from pathlib import Path

import pytest

from downloads_organiser import constants
from downloads_organiser.domain.classifier import folder_for, is_partial_download
from downloads_organiser.domain.naming import free_path, numbered_name


@pytest.mark.parametrize(
    ("file_name", "folder"),
    [
        ("holiday.jpg", "Images"),
        ("Photo.JPG", "Images"),
        ("report.pdf", "Documents"),
        ("backup.tar.gz", "Archives"),
        ("setup.exe", "Installers"),
        ("mystery.xyz", constants.UNKNOWN_FOLDER),
        ("no_extension", constants.UNKNOWN_FOLDER),
    ],
)
def test_folder_for_uses_the_extension_ignoring_case(file_name: str, folder: str) -> None:
    assert folder_for(file_name) == folder


def test_partial_download_is_recognised() -> None:
    assert is_partial_download("movie.mp4.crdownload")
    assert not is_partial_download("movie.mp4")


def test_numbered_name_goes_before_the_extension() -> None:
    assert numbered_name("photo.jpg", 1) == "photo (1).jpg"
    assert numbered_name("README", 2) == "README (2)"


def test_free_path_returns_the_wanted_path_when_free() -> None:
    wanted = Path("a") / "photo.jpg"
    assert free_path(wanted, lambda _: False) == wanted


def test_free_path_numbers_until_a_name_is_free() -> None:
    wanted = Path("a") / "photo.jpg"
    taken = {wanted, Path("a") / "photo (1).jpg"}
    assert free_path(wanted, lambda path: path in taken) == Path("a") / "photo (2).jpg"
