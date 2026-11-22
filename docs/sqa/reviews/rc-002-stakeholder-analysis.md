# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [7e8885e] |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001], [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | All three stakeholders have power, interest and quadrant. |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | IDs S01 to S03, unique and stable. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Each role, organization and level is explicit. |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | Communication table CR-001 to CR-003 mapped to milestones. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | Two conflicts, each with a mitigation. |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | Business Goal Alignment table traces every concern to an objective of [BC-001]. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Concerns are in business language with a FURPS+ attribute. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Short table and plain prose; each entry is readable alone. |
| 9 | Every concern has a stable ID (`CN-NNN`) in the concern register, with the stakeholder who raised it; IDs are never renumbered or reused | Pass | CN-001 to CN-006, each with the stakeholder who raised it. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language and Domain rows present, none a placeholder: `Language | en`, `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Content is English, as the PO language is `en`. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is the one the registry gives for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms follow the Domain Model vocabulary of the IT domain; no dictionary exists yet, so no synonym can conflict. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists in `docs/`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version: no change of language since a previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Stand-in for S01 (Product Owner, reads English, knows the IT domain); not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (BC, SA, PP, MIL, QC, FURPS+) are defined by the framework catalog; spelled out where used in prose. |

## Overall Verdict

Go — every criterion passes. The review is not independent: S01 is author, Product Owner and reviewer, and the stand-in decision stays open to challenge in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/artifacts/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[7e8885e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/commit/7e8885e982ea8d7edaf1e9ef37b1154799251620
