"""@file
@brief Draws the screenshots of the lecture steps from real command output.

The commands run for real on a generated demo folder inside a temporary
directory, so no private file name is ever shown and the host desktop is not
used. Needs Pillow (`python -m pip install -e ".[screenshots]"`).

Usage, from the repository root with the virtual environment active:
    python docs/tools/make_screenshots.py
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

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


def run(command: list[str], shown: str, cwd: Path) -> list[str]:
    """@brief Run a command and return the terminal lines it would show.

    @param command The real command to run.
    @param shown The command as the reader should type it.
    @param cwd The working directory.
    @return The prompt line followed by the output lines.
    """
    environment = {**os.environ, "PYTHONUTF8": "1"}
    done = subprocess.run(
        command, cwd=cwd, capture_output=True, text=True, env=environment, check=False
    )
    return [PROMPT + shown, *(done.stdout + done.stderr).rstrip().splitlines()]


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
    python = sys.executable
    tool = [python, "-m", "downloads_organiser"]
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        steps: list[tuple[str, str, list[str]]] = []
        plan_lines = [
            "MIL-001  Project baseline and setup",
            "MIL-002  Core organiser",
            "MIL-003  Command line and demo",
            "MIL-004  Documentation and wiki",
            "MIL-005  Publication",
        ]
        steps.append(
            ("01-plan", "Step 1: plan the project", ["Plan: five milestones", *plan_lines])
        )
        versions = run([python, "--version"], "python --version", ROOT)
        pytest_version = run(
            [python, "-m", "pytest", "--version"], "python -m pytest --version", ROOT
        )
        steps.append(
            (
                "02-setup",
                "Step 2: set up the virtual environment",
                [
                    PROMPT + "py -3.14 -m venv .venv",
                    PROMPT + r".\.venv\Scripts\Activate.ps1",
                    PROMPT + "python -m pip install --upgrade pip",
                    PROMPT + 'python -m pip install -e ".[dev]"',
                    *versions,
                    *pytest_version,
                ],
            )
        )
        constants = (ROOT / "src/downloads_organiser/constants.py").read_text(encoding="utf-8")
        excerpt = [line for line in constants.splitlines() if line and not line.startswith("##")][
            :14
        ]
        steps.append(("03-rules", "Step 3: the rules live in constants.py", excerpt))
        steps.append(
            (
                "04-demo",
                "Step 4: make a demo folder",
                run(
                    [*tool, "demo", "demo-downloads"],
                    "downloads-organiser demo demo-downloads",
                    work,
                )
                + [PROMPT + "ls demo-downloads", *tree(work / "demo-downloads")],
            )
        )
        steps.append(
            (
                "05-dry-run",
                "Step 5: dry run (nothing changes)",
                run(
                    [*tool, "organise", "demo-downloads"],
                    "downloads-organiser demo-downloads",
                    work,
                ),
            )
        )
        steps.append(
            (
                "06-apply",
                "Step 6: apply the moves",
                run(
                    [*tool, "organise", "demo-downloads", "--apply"],
                    "downloads-organiser demo-downloads --apply",
                    work,
                )
                + [PROMPT + "ls -R demo-downloads", *tree(work / "demo-downloads")],
            )
        )
        steps.append(
            (
                "07-undo",
                "Step 7: undo the run",
                run(
                    [*tool, "undo", "demo-downloads"],
                    "downloads-organiser undo demo-downloads",
                    work,
                )
                + [PROMPT + "ls demo-downloads", *tree(work / "demo-downloads")],
            )
        )
        steps.append(
            (
                "08-tests",
                "Step 8: run the tests",
                run([python, "-m", "pytest", "-q"], "python -m pytest -q", ROOT),
            )
        )
        for name, title, lines in steps:
            render(title, lines, OUT / f"step-{name}.png")
            print(f"wrote step-{name}.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
