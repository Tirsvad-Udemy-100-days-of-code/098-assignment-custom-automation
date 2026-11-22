# MIL-002 Core organiser

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide that the sorting rules work safely: planning, applying, undoing and name-clash handling are correct and tested.

## Deliverable

The package modules `domain`, `application` and `infrastructure` of `downloads_organiser` with unit tests for each rule.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | All tests of this milestone pass on Python 3.14 | 100 % pass | any failure |
| 2 | A dry run moves 0 files | 0 moved | any file moved |
| 3 | Apply then undo restores the start state | identical | any difference |
| 4 | No existing file is overwritten | 0 overwritten | any overwrite |
| 5 | opengrep reports no finding of high severity | 0 high findings | any high finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Configuration and constants must exist first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4, success criteria 1 to 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-26 — within the course assignment time box of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Classify a file by extension | Implement the pure rule that maps a file name to its target folder using the map in `constants.py`, case-insensitive, with an `Other` folder for unknown extensions. This is the core business rule (Objective 1) and has no I/O. | No | |
| 2 | Plan the moves | Build a list of planned moves for one folder: top-level files only, skipping hidden files, the undo log and the skip list. The plan is the data shown in the dry run (Objective 2). | No | |
| 3 | Resolve name clashes | When the target path exists, add a numeric suffix (`photo (1).jpg`) so no file is overwritten (Objective 4, risk: file lost). | No | |
| 4 | Apply the moves with an undo log | Move the files and write a JSON undo log of every source and target in the organised folder (Objective 3). The file system access sits behind a port in the infrastructure layer. | No | |
| 5 | Undo the last run | Read the undo log and move each file back, refusing to overwrite and removing empty sub-folders the run created. Completes Objective 3. | No | |
| 6 | Unit tests for the core | Write pytest tests on temporary folders for classification, plan, clash, apply and undo, including the dry run that must change nothing (success criteria 1 to 4). | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
