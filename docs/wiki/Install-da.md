[English](Install) · **Dansk** · [Bahasa Malaysia](Install-ms)

# Installation og kørsel

Du skal bruge Python 3.14 eller nyere. Opret et lokalt virtuelt miljø, opdater pip og installer projektet:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Prøv derefter værktøjet på en demomappe. Uden `--apply` viser det kun en plan:

```powershell
downloads-organiser demo demo-downloads
downloads-organiser demo-downloads
downloads-organiser demo-downloads --apply
downloads-organiser undo demo-downloads
```

Kør testene:

```powershell
python -m pytest
```
