# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This analysis names the people who use or judge the Downloads organiser, how much power and interest each has, and what each needs from the project. It uses the Power/Interest grid and maps each concern to a FURPS+ attribute.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad (personal) | HIGH | HIGH | Manage Closely | A safe tool that completes the Day 98 assignment |
| S02 | Udemy course participants | Fellow learners who share code and compare solutions | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes the code, and reviews every artifact; power and interest are both high.
- **Keep Informed (S02):** cannot change the project but cares about the result; they are informed through the README and the wiki.
- **Monitor (S03):** casual visitors with little influence; the repository description, topics and README are enough.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | No file may be lost or overwritten | Reliability |
| CN-002 | S01 | A run can be previewed and undone | Functionality |
| CN-003 | S02 | The code uses the assignment's function names and is readable | Supportability |
| CN-004 | S02 | The README explains how to create a `.venv` and run the program and tests | Usability |
| CN-005 | S03 | The repository has a clear description, topics and README | Usability |
| CN-006 | S03 | The project has no runtime dependencies | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat | Per accepted plan and per pull request | Plan, review records, run summary | All milestones |
| CR-002 | README and wiki (en, da, ms) | Once per release | Run instructions, screenshots per lecture step, what was learned | Documentation milestone |
| CR-003 | Repository description and topics | Once | Short description and topic list | Publication milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants a useful tool (more rules); S03 wants no dependencies and a simple repository | S01, S03 | Use only the standard library; keep the rules in `constants.py` |
| S02 wants the assignment's plain function names; S01 wants a layered design | S01, S02 | Expose the plain names from the package entry point, keep the layers inside |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objective 4 in [BC-001] |
| S01 | CN-002 | Objectives 2 and 3 in [BC-001] |
| S02 | CN-003, CN-004 | Objectives 1 and 5 in [BC-001] |
| S03 | CN-005, CN-006 | Objective 5 and success criterion 5 in [BC-001] |

## Sign-Off

Reviewed by S01 (Product Owner and reviewer).

---

[BC-001]: ./business-case.md
