"""Tests of the use cases on a real temporary folder."""

from pathlib import Path

import pytest

from downloads_organiser import constants
from downloads_organiser.application.organise import (
    apply_moves,
    organise_folder,
    plan_moves,
    undo_last_run,
)
from downloads_organiser.infrastructure.local_file_system import LocalFileSystem


@pytest.fixture
def folder(tmp_path: Path) -> Path:
    for name in ("a.jpg", "b.pdf", "c.zip", "d.unknown", ".hidden", "e.mp4.part"):
        (tmp_path / name).write_text(name, encoding="utf-8")
    (tmp_path / "subfolder").mkdir()
    (tmp_path / "subfolder" / "inner.jpg").write_text("inner", encoding="utf-8")
    return tmp_path


def snapshot(folder: Path) -> dict[str, str]:
    return {
        str(path.relative_to(folder)): path.read_text(encoding="utf-8")
        for path in sorted(folder.rglob("*"))
        if path.is_file()
    }


def test_plan_chooses_a_folder_per_file_and_skips_the_rest(folder: Path) -> None:
    moves = plan_moves(folder, LocalFileSystem())
    targets = {move.source.name: move.target.parent.name for move in moves}
    assert targets == {
        "a.jpg": "Images",
        "b.pdf": "Documents",
        "c.zip": "Archives",
        "d.unknown": constants.UNKNOWN_FOLDER,
    }


def test_dry_run_changes_nothing(folder: Path) -> None:
    before = snapshot(folder)
    moves = organise_folder(folder, LocalFileSystem())
    assert len(moves) == 4
    assert snapshot(folder) == before


def test_apply_moves_the_files_and_writes_the_undo_log(folder: Path) -> None:
    organise_folder(folder, LocalFileSystem(), apply=True)
    assert (folder / "Images" / "a.jpg").read_text(encoding="utf-8") == "a.jpg"
    assert not (folder / "a.jpg").exists()
    assert (folder / constants.UNDO_LOG_NAME).exists()
    assert (folder / ".hidden").exists()
    assert (folder / "e.mp4.part").exists()


def test_apply_then_undo_restores_the_start_state(folder: Path) -> None:
    before = snapshot(folder)
    file_system = LocalFileSystem()
    organise_folder(folder, file_system, apply=True)
    result = undo_last_run(folder, file_system)
    assert len(result.restored) == 4
    assert result.missing == ()
    assert snapshot(folder) == before
    assert not (folder / "Images").exists()


def test_name_clash_never_overwrites(tmp_path: Path) -> None:
    (tmp_path / "Images").mkdir()
    (tmp_path / "Images" / "photo.jpg").write_text("old", encoding="utf-8")
    (tmp_path / "photo.jpg").write_text("new", encoding="utf-8")
    organise_folder(tmp_path, LocalFileSystem(), apply=True)
    assert (tmp_path / "Images" / "photo.jpg").read_text(encoding="utf-8") == "old"
    assert (tmp_path / "Images" / "photo (1).jpg").read_text(encoding="utf-8") == "new"


def test_target_taken_after_planning_is_not_overwritten(tmp_path: Path) -> None:
    (tmp_path / "photo.jpg").write_text("new", encoding="utf-8")
    file_system = LocalFileSystem()
    moves = plan_moves(tmp_path, file_system)
    (tmp_path / "Images").mkdir()
    (tmp_path / "Images" / "photo.jpg").write_text("late", encoding="utf-8")
    made = apply_moves(tmp_path, moves, file_system)
    assert made[0].target.name == "photo (1).jpg"
    assert (tmp_path / "Images" / "photo.jpg").read_text(encoding="utf-8") == "late"


def test_undo_reports_a_file_that_is_gone(folder: Path) -> None:
    file_system = LocalFileSystem()
    organise_folder(folder, file_system, apply=True)
    (folder / "Images" / "a.jpg").unlink()
    result = undo_last_run(folder, file_system)
    assert [move.target.name for move in result.missing] == ["a.jpg"]
    assert len(result.restored) == 3


def test_undo_does_not_overwrite_a_file_that_took_the_old_place(tmp_path: Path) -> None:
    (tmp_path / "a.jpg").write_text("first", encoding="utf-8")
    file_system = LocalFileSystem()
    organise_folder(tmp_path, file_system, apply=True)
    (tmp_path / "a.jpg").write_text("second", encoding="utf-8")
    undo_last_run(tmp_path, file_system)
    assert (tmp_path / "a.jpg").read_text(encoding="utf-8") == "second"
    assert (tmp_path / "a (1).jpg").read_text(encoding="utf-8") == "first"


def test_undo_without_a_log_does_nothing(tmp_path: Path) -> None:
    result = undo_last_run(tmp_path, LocalFileSystem())
    assert result.restored == ()
    assert result.missing == ()


def test_two_runs_are_undone_one_at_a_time(tmp_path: Path) -> None:
    file_system = LocalFileSystem()
    (tmp_path / "a.jpg").write_text("a", encoding="utf-8")
    organise_folder(tmp_path, file_system, apply=True)
    (tmp_path / "b.pdf").write_text("b", encoding="utf-8")
    organise_folder(tmp_path, file_system, apply=True)
    undo_last_run(tmp_path, file_system)
    assert (tmp_path / "b.pdf").exists()
    assert (tmp_path / "Images" / "a.jpg").exists()
    undo_last_run(tmp_path, file_system)
    assert (tmp_path / "a.jpg").exists()
    assert not (tmp_path / constants.UNDO_LOG_NAME).exists()
