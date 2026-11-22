"""@file
@brief Draws the screenshots of the lecture steps from real command output.

The commands run for real on a generated demo folder inside a temporary
directory, so no private file name is ever shown and the host desktop is not
used. Needs Pillow (`python -m pip install -e ".[screenshots]"`).

Usage, from the repository root with the virtual environment active:
    python docs/tools/make_screenshots.py
"""

import contextlib
import io
import platform
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

import pytest
from PIL import Image, ImageDraw, ImageFont

from downloads_organiser.presentation.cli import main as run_cli

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "screenshots"
FONT_PATHS = ("C:/Windows/Fonts/consola.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
PROMPT = r"PS C:\downloads-organiser> "
BACKGROUND, TEXT, PROMPT_COLOUR, TITLE_BAR = "#1e1e1e", "#d4d4d4", "#6a9955", "#323233"


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """@brief Load a monospace font.

    @param size The font size in pixels.
    @return The first font found, or the default font.
    """
    for path in FONT_PATHS:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def render(title: str, lines: list[str], target: Path) -> None:
    """@brief Draw terminal text into a PNG file.

    @param title The title shown in the window bar.
    @param lines The lines of text; a line starting with the prompt is coloured.
    @param target The PNG file to write.
    """
    font = load_font(18)
    line_height, margin, bar = 26, 20, 34
    width = max(int(font.getlength(line)) for line in [title, *lines]) + 2 * margin
    height = bar + 2 * margin + line_height * len(lines)
    image = Image.new("RGB", (max(width, 640), height), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, image.width, bar), fill=TITLE_BAR)
    for index, colour in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
        draw.ellipse((12 + 22 * index, 11, 24 + 22 * index, 23), fill=colour)
    draw.text((90, 7), title, fill=TEXT, font=font)
    for number, line in enumerate(lines):
        y = bar + margin + number * line_height
        if line.startswith(PROMPT):
            draw.text((margin, y), PROMPT, fill=PROMPT_COLOUR, font=font)
            offset = int(font.getlength(PROMPT))
            draw.text((margin + offset, y), line[len(PROMPT) :], fill="#ffffff", font=font)
        else:
            draw.text((margin, y), line, fill=TEXT, font=font)
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)


def capture(action: Callable[[], object], shown: str, cwd: Path) -> list[str]:
    """@brief Run an action in a folder and return the terminal lines it would show.

    The action runs inside this process, so no external command is started.

    @param action The code to run; what it writes to standard output is captured.
    @param shown The command as the reader should type it.
    @param cwd The working directory.
    @return The prompt line followed by the output lines.
    """
    buffer = io.StringIO()
    with contextlib.chdir(cwd), contextlib.redirect_stdout(buffer):
        action()
    return [PROMPT + shown, *buffer.getvalue().rstrip().splitlines()]


def cli(arguments: list[str], shown: str, cwd: Path) -> list[str]:
    """@brief Run the command line of the tool and return the terminal lines.

    @param arguments The arguments after the program name.
    @param shown The command as the reader should type it.
    @param cwd The working directory.
    @return The prompt line followed by the output lines.
    """
    return capture(lambda: run_cli(arguments), shown, cwd)


def tree(folder: Path) -> list[str]:
    """@brief List the files below a folder, one per line, like a directory listing.

    @param folder The folder to list.
    @return Lines such as `Documents/report.pdf`.
    """
    return sorted(
        path.relative_to(folder).as_posix()
        for path in folder.rglob("*")
        if path.is_file() and not path.name.startswith(".")
    )


def main() -> int:
    """@brief Make all screenshots.

    @return The exit code.
    """
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        demo = work / "demo-downloads"
        plan = [
            "Plan: five milestones",
            "MIL-001  Project baseline and setup",
            "MIL-002  Core organiser",
            "MIL-003  Command line and demo",
            "MIL-004  Documentation and wiki",
            "MIL-005  Publication",
        ]
        setup = [
            PROMPT + "py -3.14 -m venv .venv",
            PROMPT + r".\.venv\Scripts\Activate.ps1",
            PROMPT + "python -m pip install --upgrade pip",
            PROMPT + 'python -m pip install -e ".[dev]"',
            PROMPT + "python --version",
            f"Python {platform.python_version()}",
            PROMPT + "python -m pytest --version",
            f"pytest {pytest.__version__}",
        ]
        constants = (ROOT / "src/downloads_organiser/constants.py").read_text(encoding="utf-8")
        rules = [line for line in constants.splitlines() if line and not line.startswith("##")]
        listing = [PROMPT + "ls -R demo-downloads"]
        steps: list[tuple[str, str, list[str]]] = [
            ("01-plan", "Step 1: plan the project", plan),
            ("02-setup", "Step 2: set up the virtual environment", setup),
            ("03-rules", "Step 3: the rules live in constants.py", rules[:14]),
        ]
        steps.append(
            (
                "04-demo",
                "Step 4: make a demo folder",
                cli(["demo", "demo-downloads"], "downloads-organiser demo demo-downloads", work)
                + listing
                + tree(demo),
            )
        )
        steps.append(
            (
                "05-dry-run",
                "Step 5: dry run (nothing changes)",
                cli(["organise", "demo-downloads"], "downloads-organiser demo-downloads", work),
            )
        )
        applied = cli(
            ["organise", "demo-downloads", "--apply"],
            "downloads-organiser demo-downloads --apply",
            work,
        )
        steps.append(("06-apply", "Step 6: apply the moves", applied + listing + tree(demo)))
        undone = cli(["undo", "demo-downloads"], "downloads-organiser undo demo-downloads", work)
        steps.append(("07-undo", "Step 7: undo the run", undone + listing + tree(demo)))
        tests = capture(
            lambda: pytest.main(["-q", "-p", "no:cacheprovider", str(ROOT / "tests")]),
            "python -m pytest -q",
            ROOT,
        )
        steps.append(("08-tests", "Step 8: run the tests", tests))
        for name, title, lines in steps:
            render(title, lines, OUT / f"step-{name}.png")
            print(f"wrote step-{name}.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
