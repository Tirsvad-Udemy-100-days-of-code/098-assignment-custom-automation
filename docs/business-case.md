# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [7e8885e] |

---

## Executive Summary

Moving files out of a cluttered Downloads folder by hand is a recurring, tedious chore. This project delivers `downloads-organiser`, a small command line tool that sorts the files of a folder into sub-folders by file type. It runs as a dry run by default, records every move in an undo log and never overwrites a file. It is the solution to Day 98 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" (assignment: Custom Automation), written so other course participants can read, run and compare it.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: plan first, review each artifact against its QC checklist, then code. Quality is described with ISO/IEC 25010:2023 characteristics. Code follows the framework's Python conventions and Clean Architecture layering (`domain`, `application`, `infrastructure`, `presentation`).

## Problem Statement

- The Downloads folder fills up with mixed files (images, documents, archives, installers) and becomes hard to search.
- Sorting by hand is repetitive, and a mistake (an overwritten or lost file) is hard to notice.
- The course assignment asks for a real automation of an everyday task, delivered as readable, runnable code.

## Business Opportunity

A safe, dependency-free organiser turns a ten-minute chore into one command. As a public repository it also serves as a worked example for other course participants.

## Objectives

1. Provide an `organise_folder()` function that moves each file into a sub-folder chosen by its extension.
2. Make the default run a dry run that shows the planned moves and changes nothing.
3. Write an undo log on every applied run and provide an `undo` command that restores the files.
4. Never overwrite an existing file; resolve a name clash with a numeric suffix.
5. Document the project in the README and in a wiki in English, Danish and Bahasa Malaysia, with a screenshot for each lecture step.

## Scope

### In Scope

- Sorting the top-level files of one folder by extension (rules held in `constants.py`).
- Dry run, apply, undo and a name clash rule.
- Command line interface, unit tests with pytest, Doxygen comments and a `Doxyfile`.
- README, wiki (en, da, ms), screenshots, repository description and topics.

### Out of Scope

- Selenium or any browser automation (no runtime dependency is needed).
- Recursive sorting of nested folders, scheduling, a graphical interface, cloud storage.
- Content inspection of files (only the extension is used).

## Expected Benefits

### Tangible Benefits

- One command replaces manual sorting.
- No file is lost or overwritten, and every run can be undone.
- A runnable example with tests that course participants can copy.

### Intangible Benefits

- Practice of automation, file handling and testing from the course.
- A documented example of the framework's plan-first workflow.

## Strategic Alignment

The project completes the Day 98 assignment of the course and adds a documented, reviewed example to the author's public course repository.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Organise a folder in dry run | 0 files moved, all planned moves printed | pytest test and screenshot |
| 2 | Apply then undo | Folder identical to the start state | pytest test |
| 3 | Name clash | 0 files overwritten | pytest test |
| 4 | Test suite | 100 % of tests pass on Python 3.14 | `python -m pytest` exit code 0 |
| 5 | Runtime dependencies | 0 | `pyproject.toml` has an empty `dependencies` list |
| 6 | Documentation | README plus wiki in 3 languages, 1 screenshot per lecture step | file check before the pull request |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| A file is overwritten or lost | High: user data lost | Never overwrite; dry run by default; undo log |
| Tool moves files a user wants to keep in place | Medium | Dry run first; only top-level files; a skip list in `constants.py` |
| Secret committed by mistake | High | `.env` is gitignored, never imported; opengrep scan before every push |
| Screenshots show private file names | Medium | Screenshots are taken on a generated demo folder only |
| Python 3.14 not available to a reader | Low | README states the requirement and how to create the venv |

## Assumptions

- The Product Owner, developer and reviewer is S01; S01 can be reached in chat.
- Python 3.14 or later is installed on the machine that runs the project.
- Sorting by extension is enough for the assignment.

## Constraints

- Python 3.14 or later; a local `venv`; `pytest` for tests; no runtime dependencies.
- Folder structure `src/`, `tests/`, `docs/`; constants in `constants.py`.
- The word for artificial intelligence is not used in any artifact.
- Time box of the course assignment: about 120 minutes of coding effort.

## Cost–Benefit Assessment

Qualitative, because the project is a free learning exercise with no revenue; a figure would be invented.

| Costs | Benefits |
| --- | --- |
| About two hours of S01's time for the code, plus documentation time | Reusable tool, tested and documented example, completed assignment |
| Maintenance of a small repository | No runtime dependencies to maintain |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer: completes the assignment and wants a tool that is safe to use |
| S02 | Course participants: want readable, runnable code with the assignment's function names |
| S03 | Repository viewers: want a clear description, topics and README, with no dependencies |

## Recommendation

Proceed — the scope is small, the risk is controlled by dry run and undo, and the result completes the assignment.

---

[SA-001]: ./stakeholder-analysis.md
[7e8885e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/commit/7e8885e982ea8d7edaf1e9ef37b1154799251620
