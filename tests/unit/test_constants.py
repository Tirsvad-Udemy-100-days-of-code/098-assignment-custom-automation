"""Tests of the rule table in constants.py."""

from downloads_organiser import constants


def test_every_extension_is_lower_case_with_a_dot() -> None:
    for extensions in constants.EXTENSION_FOLDERS.values():
        for extension in extensions:
            assert extension.startswith(".")
            assert extension == extension.lower()


def test_no_extension_belongs_to_two_folders() -> None:
    seen: dict[str, str] = {}
    for folder, extensions in constants.EXTENSION_FOLDERS.items():
        for extension in extensions:
            assert extension not in seen, f"{extension} is in {seen[extension]} and {folder}"
            seen[extension] = folder


def test_unknown_folder_is_not_a_rule_folder() -> None:
    assert constants.UNKNOWN_FOLDER not in constants.EXTENSION_FOLDERS
