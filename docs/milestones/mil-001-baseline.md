# MIL-001 Project baseline and setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide that the repository is ready for code: configuration, tooling and the documented way to create a virtual environment exist.

## Deliverable

A repository with `pyproject.toml`, a Python `.gitignore`, `.editorconfig`, `constants.py`, a `Doxyfile`, an empty test suite that runs, and the setup instructions for `.venv`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` runs on Python 3.14 and exits 0 | pass | failure |
| 2 | `pyproject.toml` lists no runtime dependencies | empty list | any entry |
| 3 | `check-editorconfig.sh` passes | pass | failure |

## Dependencies

| Depends on | Reason |
| --- | --- |
| Business Case, Stakeholder Analysis and Project Plan accepted | The gate rule requires an accepted plan before code |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5 and success criteria 4 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-24 — within the course assignment time box of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Configure the project for Python 3.14 or later with an empty runtime dependency list, the `src/` layout, a console script `downloads-organiser` and a `dev` extra for pytest. This is the single configuration file the Business Case requires (S02 and S03 read it first). | No | |
| 2 | Add Python .gitignore and .editorconfig | Add the Python `.gitignore` (virtual environments, caches, `.env`, build output) and the root `.editorconfig` from the framework baseline template, then run `check-editorconfig.sh`. Keeps secrets and noise out of the repository (risk: secret committed). | No | |
| 3 | Add constants.py | Create `src/downloads_organiser/constants.py` with the extension-to-folder map, the folder name for unknown types, the undo log file name and the skip list. The requirements demand that constants live in one `constants.py`. | No | |
| 4 | Add Doxyfile | Add a `Doxyfile` that reads `src/` and writes to `docs/doxygen/`, so the Doxygen comments in the source can be turned into HTML (Business Case objective 5). | No | |
| 5 | Document venv setup | Describe how to create and use a local `.venv` and run `python -m pip install --upgrade pip` in the README setup section, for Windows (PowerShell) and Linux or macOS. Serves concern CN-004 of S02. | No | |
| 6 | Install git hooks and plan gate | Run `install-git-hooks.sh --enable-plan-gate` so main cannot be committed to and every change under `src/` or `tests/` carries a `Task: MIL-NNN#N` trailer. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
