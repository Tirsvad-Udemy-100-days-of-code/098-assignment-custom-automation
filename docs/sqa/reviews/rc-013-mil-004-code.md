# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [d8f815e] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004] (the code it delivers under `src/` and `tests/`: the screenshot tool docs/tools/make_screenshots.py)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked by ruff rule set N (pep8-naming). |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names come from the PO vocabulary (organise, plan, undo, folder, extension). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check` report no finding; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` reports no error. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; no exception swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; ruff rule B passes. |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are opened with `with` or pathlib one-shot calls. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a Doxygen docstring; `doxygen Doxyfile` has no warning. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | User output goes through the presentation layer; no secret is read or printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: all tasks are plain technical tasks (PP-001, Planning Assumptions). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | pytest tests named for behaviour, using tmp_path, no network, no order dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Runtime dependencies: none; dev tools declared in `pyproject.toml`. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Rules and names live once in constants.py and the domain module. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports only the standard library and constants; application imports domain; infrastructure and presentation import inward. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One responsibility per module; the file system sits behind a port. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | The script is a development tool under docs/tools, not part of the product source, so the layer layout does not apply. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Names are lower snake_case or kebab, no spaces. |

## Overall Verdict

Go: every applicable criterion passes, and the tools named in the evidence were run. The review is not independent: S01 is author and reviewer.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[MIL-004]: ../../milestones/mil-004-documentation.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[d8f815e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/commit/d8f815e4557112acf4dcdd2af30ef6142ee22541
