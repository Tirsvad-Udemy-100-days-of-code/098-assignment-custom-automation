[English](Install) · [Dansk](Install-da) · **Bahasa Malaysia**

# Pemasangan dan larian

Anda memerlukan Python 3.14 atau lebih baharu. Cipta persekitaran maya setempat, naik taraf pip dan pasang projek:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kemudian cuba alat ini pada folder demo. Tanpa `--apply`, ia hanya menunjukkan pelan:

```powershell
downloads-organiser demo demo-downloads
downloads-organiser demo-downloads
downloads-organiser demo-downloads --apply
downloads-organiser undo demo-downloads
```

Jalankan ujian:

```powershell
python -m pytest
```
