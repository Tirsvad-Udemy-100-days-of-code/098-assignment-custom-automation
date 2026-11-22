[English](Lecture-Steps) · **Dansk** · [Bahasa Malaysia](Lecture-Steps-ms)

# Kursustrin

Hvert trin viser et skærmbillede lavet af værktøjets rigtige output og det, vi lærte i trinnet.

## Trin 1: Planlæg projektet

![Trin 1: Planlæg projektet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-01-plan.png)

**Det lærte vi:** Vi valgte en opgave, der er værd at automatisere: at sortere en rodet Downloads-mappe. Vi lærte at bestemme sikkerhedsreglerne, før vi skriver kode: først en prøvekørsel, en fortryd-log og aldrig overskrive en fil. Vi skrev også ned, hvem koden er til, og hvad der kan gå galt.

## Trin 2: Opsæt miljøet

![Trin 2: Opsæt miljøet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-02-setup.png)

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

**Det lærte vi:** Et lokalt `.venv` holder projektet adskilt fra resten af systemet, og `python -m pip install --upgrade pip` holder installationsprogrammet opdateret. Én `pyproject.toml` rummer hele konfigurationen, og projektet har ingen afhængigheder ved kørsel, fordi standardbiblioteket er nok.

## Trin 3: Hold reglerne i constants.py

![Trin 3: Hold reglerne i constants.py](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-03-rules.png)

```python
EXTENSION_FOLDERS: Final[dict[str, tuple[str, ...]]] = {
    "Images": (".jpg", ".png", ...),
    "Documents": (".pdf", ".txt", ...),
}
```

**Det lærte vi:** Vi adskilte data fra logik. Tabellen over mapper og filendelser ligger ét sted, så en ny filtype er en ændring på én linje, uden at koden skal røres.

## Trin 4: Lav en demomappe

![Trin 4: Lav en demomappe](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-04-demo.png)

```powershell
downloads-organiser demo demo-downloads
```

**Det lærte vi:** Sikre testdata er en del af god automatisering. Kommandoen `demo` laver opdigtede filer med `pathlib`, så vi kan prøve værktøjet og tage skærmbilleder uden nogensinde at vise private filnavne.

## Trin 5: Prøvekørsel

![Trin 5: Prøvekørsel](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-05-dry-run.png)

```powershell
downloads-organiser demo-downloads
```

**Det lærte vi:** At planlægge og at udføre er to forskellige ting. Værktøjet bygger først en liste over flytninger og udskriver den; intet ændres. Derfor kan man stole på værktøjet: man ser resultatet, før man accepterer det. Kommandolinjen er lavet med `argparse` fra standardbiblioteket.

## Trin 6: Udfør flytningerne

![Trin 6: Udfør flytningerne](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-06-apply.png)

```powershell
downloads-organiser demo-downloads --apply
```

**Det lærte vi:** Med `--apply` flyttes filerne med `shutil.move`, mapper oprettes efter behov, og et navnsammenfald får et nummer (`photo (1).jpg`) i stedet for en overskrivning. Hver flytning skrives til en JSON-fortryd-log.

## Trin 7: Fortryd kørslen

![Trin 7: Fortryd kørslen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-07-undo.png)

```powershell
downloads-organiser undo demo-downloads
```

**Det lærte vi:** Automatisering bør kunne fortrydes. Fortryd læser loggen og flytter hver fil tilbage, melder en fil, der er forsvundet, og nægter stadig at overskrive en fil, der har taget den gamle plads.

## Trin 8: Kør testene

![Trin 8: Kør testene](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-08-tests.png)

```powershell
python -m pytest
```

**Det lærte vi:** Tests på midlertidige mapper (`tmp_path`) er sikkerhedsnettet for et værktøj, der flytter filer. Vi lærte også at kontrollere koden med ruff, mypy i streng tilstand, Doxygen-kommentarer og en opengrep-scanning før hver push.
