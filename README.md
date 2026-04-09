# text_crawler
A text based simple dungeon crawler game made as a school project

## Building a Windows executable locally

### Requirements
- Windows 10/11
- Python 3.11 (or newer) — download from https://www.python.org/downloads/

### Steps

```powershell
# 1. Clone the repo and enter its directory
git clone https://github.com/Mando328/text_crawler.git
cd text_crawler

# 2. (Optional but recommended) Create a virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install PyInstaller
pip install pyinstaller

# 4. Build the executable using the provided spec file
pyinstaller game.spec
```

The finished executable will be placed at:
```
dist\TextCrawler.exe
```

Run it by double-clicking `dist\TextCrawler.exe` or from a Command Prompt:
```powershell
.\dist\TextCrawler.exe
```

> **Note:** `PYTANIA.txt` (the quiz questions file) is bundled automatically
> by the spec file — you do **not** need to copy it next to the `.exe`.

## CI builds

Every push and pull request to `main` automatically builds the `.exe` via
GitHub Actions (Windows runner, Python 3.11). The artifact `TextCrawler-windows`
containing `TextCrawler.exe` can be downloaded from the **Actions** tab of this
repository after the workflow finishes.
