**English** · [Dansk](Lecture-Steps-da) · [Bahasa Malaysia](Lecture-Steps-ms)

# Lecture steps

Each step shows a screenshot made from the real output of the tool, and what we gained in that step.

## Step 1: Plan the project

![Step 1: Plan the project](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-01-plan.png)

**What we gained:** We chose a task that is worth automating: sorting a cluttered Downloads folder. We learned to decide the safety rules before writing code: a dry run first, an undo log, and never overwriting a file. We also wrote down who the code is for and what could go wrong.

## Step 2: Set up the environment

![Step 2: Set up the environment](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-02-setup.png)

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

**What we gained:** A local `.venv` keeps the project apart from the rest of the system, and `python -m pip install --upgrade pip` keeps the installer current. One `pyproject.toml` holds the whole configuration, and the project needs no runtime dependencies because the standard library is enough.

## Step 3: Keep the rules in constants.py

![Step 3: Keep the rules in constants.py](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-03-rules.png)

```python
EXTENSION_FOLDERS: Final[dict[str, tuple[str, ...]]] = {
    "Images": (".jpg", ".png", ...),
    "Documents": (".pdf", ".txt", ...),
}
```

**What we gained:** We separated data from logic. The table of folders and extensions lives in one place, so a new file type is a one-line change and the code does not need to be touched.

## Step 4: Make a demo folder

![Step 4: Make a demo folder](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-04-demo.png)

```powershell
downloads-organiser demo demo-downloads
```

**What we gained:** Safe test data is part of good automation. The `demo` command creates made-up files with `pathlib`, so we can try the tool and take screenshots without ever showing private file names.

## Step 5: Dry run

![Step 5: Dry run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-05-dry-run.png)

```powershell
downloads-organiser demo-downloads
```

**What we gained:** Planning and doing are two different things. The tool first builds a list of moves and prints it; nothing changes. This is why the tool is trusted: you see the result before you accept it. The command line was built with `argparse` from the standard library.

## Step 6: Apply the moves

![Step 6: Apply the moves](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-06-apply.png)

```powershell
downloads-organiser demo-downloads --apply
```

**What we gained:** With `--apply` the files are moved with `shutil.move`, folders are created when needed, and a name clash gets a number (`photo (1).jpg`) instead of an overwrite. Every move is written to a JSON undo log.

## Step 7: Undo the run

![Step 7: Undo the run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-07-undo.png)

```powershell
downloads-organiser undo demo-downloads
```

**What we gained:** Automation should be reversible. Undo reads the log and moves each file back, reports a file that has gone missing, and still refuses to overwrite a file that took the old place.

## Step 8: Run the tests

![Step 8: Run the tests](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-08-tests.png)

```powershell
python -m pytest
```

**What we gained:** Tests on temporary folders (`tmp_path`) are the safety net for a tool that moves files. We also learned to check the code with ruff, mypy in strict mode, Doxygen comments and an opengrep scan before every push.
