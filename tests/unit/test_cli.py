"""Tests of the command line, calling main() directly."""

import io
from pathlib import Path

import pytest

import downloads_organiser
from downloads_organiser import constants
from downloads_organiser.presentation.cli import main


def run(*argv: str) -> tuple[int, str]:
    out = io.StringIO()
    code = main(list(argv), out)
    return code, out.getvalue()


def test_demo_creates_the_sample_files(tmp_path: Path) -> None:
    code, text = run("demo", str(tmp_path / "demo"))
    assert code == 0
    assert len(list((tmp_path / "demo").iterdir())) == len(constants.DEMO_FILES)
    assert str(len(constants.DEMO_FILES)) in text


def test_default_run_is_a_dry_run(tmp_path: Path) -> None:
    run("demo", str(tmp_path))
    code, text = run(str(tmp_path))
    assert code == 0
    assert "Dry run" in text
    assert (tmp_path / "report.pdf").exists()


def test_apply_moves_and_undo_restores(tmp_path: Path) -> None:
    run("demo", str(tmp_path))
    code, text = run("organise", str(tmp_path), "--apply")
    assert code == 0
    assert "Undo with" in text
    assert (tmp_path / "Documents" / "report.pdf").exists()
    code, text = run("undo", str(tmp_path))
    assert code == 0
    assert "Restored" in text
    assert (tmp_path / "report.pdf").exists()


def test_undo_with_nothing_to_undo(tmp_path: Path) -> None:
    assert run("undo", str(tmp_path)) == (0, "Nothing to undo.\n")


def test_missing_folder_gives_exit_code_2(tmp_path: Path) -> None:
    code, text = run(str(tmp_path / "missing"))
    assert code == 2
    assert "not a folder" in text


def test_help_exits_zero(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as stop:
        main(["--help"])
    assert stop.value.code == 0
    assert "downloads-organiser" in capsys.readouterr().out


def test_assignment_function_names_are_exported(tmp_path: Path) -> None:
    (tmp_path / "a.jpg").write_text("a", encoding="utf-8")
    assert len(downloads_organiser.organise_folder(tmp_path)) == 1
    downloads_organiser.organise_folder(tmp_path, apply=True)
    assert len(downloads_organiser.undo_last_run(tmp_path).restored) == 1
    assert (tmp_path / "a.jpg").exists()
