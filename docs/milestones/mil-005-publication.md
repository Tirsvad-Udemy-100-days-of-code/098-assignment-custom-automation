# MIL-005 Publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [7e8885e] |

---

## Purpose

Decide that the repository can be published: scanned, described and merged through pull requests.

## Deliverable

A scanned repository with a description and topics on the git host, and all pull requests merged.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | opengrep scan of the repository reports no finding | 0 findings | any finding |
| 2 | Repository description and topics are set on the git host | set | missing |
| 3 | `.env` is not tracked and no token appears in any commit | 0 hits | any hit |
| 4 | All milestones are Accepted with a Go review | all Go | any other |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Documentation is part of what is published |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Success criteria 5 and 6; concern CN-005 | [BC-001], [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-12-02 — within the course assignment time box of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Scan with opengrep before every push | Run `~\.opengrep\cli\latest\opengrep.exe` on the repository before each push and fix or justify every finding (risk: secret or insecure code published). | No | |
| 2 | Set repository description and topics | Set a short description and the topics (python, automation, file-organizer, udemy, 100-days-of-code, pytest) on `Tirsvad-Udemy-100_days_of_code` through the Gitea API, reading the token from `.env` without printing it or adding it to the project. | No | |
| 3 | Verify the closing of issues | After each merge check that every issue the pull request names is closed and that finished milestones are closed on the git host. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[7e8885e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/commit/7e8885e982ea8d7edaf1e9ef37b1154799251620
