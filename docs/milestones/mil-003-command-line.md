# MIL-003 Command line and demo

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide that the tool is usable by S01 and readable by S02: a command line interface and the assignment function names exist.

## Deliverable

The `presentation` layer (command line), the package entry point exporting `organise_folder`, `undo_last_run` and a demo folder generator.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `downloads-organiser --help` exits 0 | exit 0 | non-zero |
| 2 | Default run prints the plan and moves 0 files | 0 moved | any moved |
| 3 | `--apply` and `undo` work from the command line | pass | failure |
| 4 | All tests pass | 100 % pass | any failure |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The command line calls the core use cases |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 3; concerns CN-002 and CN-003 | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-28 — within the course assignment time box of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the command line | Add `presentation/cli.py` with argparse: a folder argument (default `~/Downloads`), `--apply`, and an `undo` sub-command. Dry run is the default (Objective 2); only the standard library is used (CN-006). | No | |
| 2 | Export the assignment function names | Export `organise_folder()` and `undo_last_run()` from the package so S02 finds the names the assignment uses (CN-003), keeping the layers behind them. | No | |
| 3 | Add the demo folder generator | Add a function and a `demo` sub-command that create a throw-away folder with sample files, so screenshots never show private file names (risk: private data in screenshots). | No | |
| 4 | Add command line tests | Test the argument handling, exit codes and the printed plan with pytest, calling `main(argv)` directly. | No | |
| 5 | Add the package entry point | Add `__main__.py` so `python -m downloads_organiser` works and register the console script in `pyproject.toml`. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
