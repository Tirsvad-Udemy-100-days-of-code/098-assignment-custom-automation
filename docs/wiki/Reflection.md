**English** · [Dansk](Reflection-da) · [Bahasa Malaysia](Reflection-ms)

# Reflection

## How the project was approached

We planned first: a Business Case, a Stakeholder Analysis, a Project Plan and five milestones, each reviewed before code was written. The code was then built in small layers (domain, application, infrastructure, command line), each with tests.

## What was hard

Making every step safe. A file mover can lose data, so name clashes, files that were moved away before an undo, and unfinished downloads all needed a rule and a test. The three-language wiki also takes time.

## What was easy

The standard library does almost everything: `pathlib`, `shutil`, `json` and `argparse`. No third-party package was needed.

## Biggest learning

A dry run and an undo log turn a risky script into a tool that can be trusted. Automation is not only about saving time; it is about being able to see and reverse what the script did.

## What to do differently next time

Add more rules, for example sorting by date, and a setting file for the user's own folders. Take the screenshots from the start of the work, as the code grows, instead of at the end.
