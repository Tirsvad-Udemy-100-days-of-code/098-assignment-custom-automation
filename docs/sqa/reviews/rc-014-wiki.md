# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [d8f815e] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (12 pages and the sidebar; a wiki has no ID)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da and ms / it (the wiki is reviewed for structure here; it is documentation, not an artifact of a PO-language type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, then one list of the four English pages, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Home, Install, Lecture-Steps and Reflection are listed and exist. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so it has no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is last: English, Dansk, Bahasa Melayu, each linking to its Home page. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is a hand-written page, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Each page has a language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English, plus Danish and Bahasa Malaysia on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Each of the four English pages has a -da and a -ms page. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Suffixes -da and -ms; English has none. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, code, file names and IDs are in English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | Can be checked only after the merge publishes the wiki; recorded as an action item. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No change to the layout rules. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All pages are directly in docs/wiki/; no subfolder. |

## Overall Verdict

Go-with-conditions: every checkable criterion passes; criterion 14 can be checked only on the published wiki, after the merge. Not independent: S01 is author and reviewer.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published sidebar, every page and every link on the git host, and record the result (criterion 14) | S01 | 2026-12-02 |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[d8f815e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/commit/d8f815e4557112acf4dcdd2af30ef6142ee22541
