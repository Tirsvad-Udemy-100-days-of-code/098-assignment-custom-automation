[English](Lecture-Steps) · [Dansk](Lecture-Steps-da) · **Bahasa Malaysia**

# Langkah kuliah

Setiap langkah menunjukkan tangkapan skrin daripada output sebenar alat ini dan apa yang kami pelajari dalam langkah itu.

## Langkah 1: Rancang projek

![Langkah 1: Rancang projek](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-01-plan.png)

**Apa yang kami pelajari:** Kami memilih tugas yang berbaloi diautomasikan: menyusun folder Downloads yang bersepah. Kami belajar menetapkan peraturan keselamatan sebelum menulis kod: larian percubaan dahulu, log buat asal, dan jangan sekali-kali menimpa fail. Kami juga mencatat untuk siapa kod ini dan apa yang boleh menjadi salah.

## Langkah 2: Sediakan persekitaran

![Langkah 2: Sediakan persekitaran](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-02-setup.png)

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

**Apa yang kami pelajari:** `.venv` setempat mengasingkan projek daripada sistem lain, dan `python -m pip install --upgrade pip` memastikan pemasang sentiasa terkini. Satu fail `pyproject.toml` memegang seluruh konfigurasi, dan projek ini tidak memerlukan kebergantungan masa larian kerana pustaka standard sudah mencukupi.

## Langkah 3: Simpan peraturan dalam constants.py

![Langkah 3: Simpan peraturan dalam constants.py](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-03-rules.png)

```python
EXTENSION_FOLDERS: Final[dict[str, tuple[str, ...]]] = {
    "Images": (".jpg", ".png", ...),
    "Documents": (".pdf", ".txt", ...),
}
```

**Apa yang kami pelajari:** Kami memisahkan data daripada logik. Jadual folder dan sambungan fail berada di satu tempat, jadi jenis fail baharu hanyalah perubahan satu baris tanpa menyentuh kod.

## Langkah 4: Cipta folder demo

![Langkah 4: Cipta folder demo](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-04-demo.png)

```powershell
downloads-organiser demo demo-downloads
```

**Apa yang kami pelajari:** Data ujian yang selamat ialah sebahagian daripada automasi yang baik. Arahan `demo` mencipta fail rekaan dengan `pathlib`, jadi kami boleh mencuba alat dan mengambil tangkapan skrin tanpa menunjukkan nama fail peribadi.

## Langkah 5: Larian percubaan

![Langkah 5: Larian percubaan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-05-dry-run.png)

```powershell
downloads-organiser demo-downloads
```

**Apa yang kami pelajari:** Merancang dan melaksanakan ialah dua perkara berbeza. Alat ini mula-mula membina senarai pemindahan dan mencetaknya; tiada apa yang berubah. Itulah sebabnya alat ini boleh dipercayai: anda melihat hasilnya sebelum menerimanya. Baris arahan dibina dengan `argparse` daripada pustaka standard.

## Langkah 6: Laksanakan pemindahan

![Langkah 6: Laksanakan pemindahan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-06-apply.png)

```powershell
downloads-organiser demo-downloads --apply
```

**Apa yang kami pelajari:** Dengan `--apply`, fail dipindahkan dengan `shutil.move`, folder dicipta apabila perlu, dan pertembungan nama mendapat nombor (`photo (1).jpg`) dan bukan ditimpa. Setiap pemindahan ditulis ke dalam log buat asal JSON.

## Langkah 7: Buat asal larian

![Langkah 7: Buat asal larian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-07-undo.png)

```powershell
downloads-organiser undo demo-downloads
```

**Apa yang kami pelajari:** Automasi sepatutnya boleh dibuat asal. Buat asal membaca log dan memindahkan setiap fail kembali, melaporkan fail yang telah hilang, dan masih enggan menimpa fail yang telah mengambil tempat lama.

## Langkah 8: Jalankan ujian

![Langkah 8: Jalankan ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/098-assignment-custom-automation/raw/branch/main/docs/screenshots/step-08-tests.png)

```powershell
python -m pytest
```

**Apa yang kami pelajari:** Ujian pada folder sementara (`tmp_path`) ialah jaringan keselamatan bagi alat yang memindahkan fail. Kami juga belajar menyemak kod dengan ruff, mypy dalam mod ketat, komen Doxygen dan imbasan opengrep sebelum setiap push.
