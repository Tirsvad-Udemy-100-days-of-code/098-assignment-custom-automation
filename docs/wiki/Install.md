**English** · [Dansk](Install-da) · [Bahasa Malaysia](Install-ms)

# Install and run

You need Python 3.14 or later. Create a local virtual environment, upgrade pip and install the project:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Then try the tool on a demo folder. Without `--apply` it only shows a plan:

```powershell
downloads-organiser demo demo-downloads
downloads-organiser demo-downloads
downloads-organiser demo-downloads --apply
downloads-organiser undo demo-downloads
```

Run the tests:

```powershell
python -m pytest
```
