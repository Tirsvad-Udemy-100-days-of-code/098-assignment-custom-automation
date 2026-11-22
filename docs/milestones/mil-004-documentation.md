# MIL-004 Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [7e8885e] |

---

## Purpose

Decide that S02 and S03 can understand, run and learn from the project without asking.

## Deliverable

README from the framework template, Doxygen comments with generated HTML, a wiki in English, Danish and Bahasa Malaysia, and one screenshot for each lecture step.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README passes `check-readme.sh` | pass | failure |
| 2 | Wiki exists in en, da and ms with the same pages | 3 languages | a language missing |
| 3 | One screenshot per lecture step in README and each wiki language | all present | a screenshot missing |
| 4 | `doxygen Doxyfile` ends without warnings | 0 warnings | any warning |
| 5 | The word for artificial intelligence appears in no artifact | 0 hits | any hit |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Screenshots show the finished command line |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5; concerns CN-004 and CN-005 | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-30 — within the course assignment time box of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Doxygen comments | Document every module, class and function in `src/` with Doxygen comments (`@brief`, `@param`, `@return`) and check that `doxygen Doxyfile` runs without warnings (Objective 5). | No | |
| 2 | Write the README | Create `README.md` from `framework/templates/README-template.md`: what it does, requirements, `.venv` setup, how to run the tool and the tests, the lecture steps with screenshots. Check with `check-readme.sh`. | No | |
| 3 | Capture lecture step screenshots | Render the output of each lecture step (plan, setup, dry run, apply, undo, tests) on the demo folder into PNG files in `docs/screenshots/` with a small drawing script, so no host desktop is used and no private names appear. | No | |
| 4 | Write the English wiki | Write the wiki pages in `docs/wiki/en/`: home, the lecture steps with screenshots, and what was gained in each step, as `framework/process/wiki.md` requires. | No | |
| 5 | Write the Danish wiki | Write the same pages in Danish in `docs/wiki/da/`, with the same structure and screenshots as the English pages. | No | |
| 6 | Write the Bahasa Malaysia wiki | Write the same pages in Bahasa Malaysia in `docs/wiki/ms/`, with the same structure and screenshots as the English pages. | No | |
| 7 | Write the reflection | Add the course reflection (approach, what was hard and easy, biggest learning, what to do differently) to the wiki in three languages, as the assignment asks. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[7e8885e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/commit/7e8885e982ea8d7edaf1e9ef37b1154799251620
