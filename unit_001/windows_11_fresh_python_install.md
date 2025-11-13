```markdown
---
title: Python Clean Install – SAFE CHECKLIST (Windows 11)
subtitle: Rename, Don’t Delete – Easy to Undo!
author: Your Instructor
date: November 2025
geometry: margin=1in
---

> **DISCLAIMER**  
> **The author and instructor are NOT responsible for any issues, data loss, or system problems from following these steps.**  
> Always **back up important files** before changing system settings.  
> These instructions are for educational use. **Proceed at your own risk.**

---

# **GOAL**  
Install **Python from python.org** cleanly on Windows 11  
**NO DELETING** — just **renaming** old folders with `-old` so you can undo in seconds!

---

## **STEP 1: Uninstall All Python Apps**

| Step | Action |
|------|--------|
| 1 | Press **Win + I** → **Settings** |
| 2 | Click **Apps** → **Installed apps** |
| 3 | Search: `Python` |
| 4 | Click each result → **Uninstall** (including: Python 3.12, Python Launcher, etc.) |
| 5 | **Restart computer** when done |

---

## **STEP 2: Rename (Don’t Delete!) Old Python Folders**

> **This keeps your old setup safe — just in case!**

1. Press **Win + R** → type `%appdata%` → press **Enter**  
2. Go **up one level** → open the **Local** folder  
3. **Right-click** each folder below → **Rename** → add `-old` at the end:

| Original Folder | → Rename To |
|------------------|-------------|
| `C:\Users\YourName\AppData\Local\Programs\Python` | → `Python-old` |
| `C:\Users\YourName\AppData\Local\Programs\Python312` | → `Python312-old` *(if exists)* |
| `C:\Users\YourName\AppData\Local\pip` | → `pip-old` |

> **Tip**: If a folder says “in use”, close all Python apps (IDLE, VS Code, CMD) and try again.

---

## **STEP 3: Turn OFF Windows Python Hijacks**

1. Open **Settings** → **Apps** → **App execution aliases**  
   *(Search “aliases” in Start menu if you can’t find it)*
2. Find and **TURN OFF**:
   - [ ] `python.exe` → **OFF**
   - [ ] `python3.exe` → **OFF**

> This stops Windows from using its hidden “fake” Python.

---

## **STEP 4: Install Python from python.org**

1. Go to: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click **“Download Python 3.12.x”** (latest version)
3. **Save** the `.exe` file
4. **Right-click the file** → **Run as administrator**
5. **CHECK THESE BOXES**:
   - [x] **Add Python to PATH**
   - [x] **Install launcher for all users** *(recommended)*
6. Click **“Install Now”**
7. Wait → Click **Close**

---

## **STEP 5: Restart Computer**

> **Required!** Windows needs a full reboot to update PATH and clear old links.

---

## **STEP 6: Test Your New Python**

Open **Command Prompt** (search “cmd” in Start):

```bash
python --version
# → Should show: Python 3.12.x

pip --version
# → Should point to: ...AppData\Local\Programs\Python\...

where python
# → Should show ONLY the python.org path (NOT WindowsApps)
```

---

## **STEP 7: Test Pygame in a Virtual Environment**

```bash
# Make a test folder
mkdir pygame-test
cd pygame-test

# Create safe sandbox
python -m venv venv

# Turn it on
venv\Scripts\activate

# Install pygame
pip install pygame

# Test it!
python -c "import pygame; print('Pygame is ready!')"
```

---

## **IF SOMETHING GOES WRONG – UNDO IN 30 SECONDS!**

Just **rename the folders back**:

```
Python-old → Python
pip-old → pip
```

Then **restart** → old Python returns like magic!

> After 1 week (and everything works), you can **delete** the `-old` folders.

---

## **PRINTABLE CHECKLIST (Copy & Paste)**

```txt
SAFE PYTHON CLEAN INSTALL CHECKLIST
-----------------------------------
[ ] Uninstall ALL Python (Settings > Apps)
[ ] RENAME (don’t delete):
    → Python → Python-old
    → Python312 → Python312-old
    → pip → pip-old
[ ] Settings → App execution aliases → OFF: python.exe & python3.exe
[ ] Download python.org installer
[ ] Run as admin → CHECK "Add to PATH"
[ ] Install → Restart PC
[ ] Test: python --version
[ ] Test: pip install pygame
[ ] IF BROKEN: Rename -old folders back → restart
```

---

**You now have a clean, safe, professional Python setup — with a safety net!**

---
