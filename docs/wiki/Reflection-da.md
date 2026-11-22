[English](Reflection) · **Dansk** · [Bahasa Malaysia](Reflection-ms)

# Refleksion

## Hvordan projektet blev grebet an

Vi planlagde først: en business case, en interessentanalyse, en projektplan og fem milepæle, hver gennemgået, før koden blev skrevet. Koden blev derefter bygget i små lag (domæne, applikation, infrastruktur, kommandolinje), hvert med tests.

## Hvad der var svært

At gøre hvert trin sikkert. Et værktøj, der flytter filer, kan miste data, så navnesammenfald, filer der er flyttet væk før en fortrydelse, og ufærdige downloads krævede hver en regel og en test. Wikien på tre sprog tager også tid.

## Hvad der var nemt

Standardbiblioteket klarer næsten alt: `pathlib`, `shutil`, `json` og `argparse`. Der skulle ingen pakker fra tredjepart til.

## Største læring

En prøvekørsel og en fortryd-log gør et risikabelt script til et værktøj, man kan stole på. Automatisering handler ikke kun om at spare tid, men om at kunne se og fortryde det, scriptet gjorde.

## Hvad vi vil gøre anderledes næste gang

Tilføje flere regler, for eksempel sortering efter dato, og en indstillingsfil til brugerens egne mapper. Tage skærmbillederne fra begyndelsen, mens koden vokser, i stedet for til sidst.
