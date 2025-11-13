# **Complete Python Reset + Clean python.org Install (Windows 11)**  
*“Nuke & Rebuild” – Guaranteed to fix all PATH/alias conflicts*

---

> **⚠️ LEGAL DISCLAIMER**  
> **The author, instructor, and any affiliated parties are NOT responsible for any damage, data loss, system instability, or other issues that may occur as a result of following these instructions.**  
> These steps involve modifying system settings, uninstalling software, and deleting files. **Proceed at your own risk.**  
> Always **back up important data** before making system changes.  
> If you are unsure, consult a qualified IT professional.  
> **No liability is accepted for any outcome, direct or indirect.**

---

## STEP 1: **Uninstall ALL Python Versions**

| Action | How |
|--------|-----|
| 1 | Press **Win + I** → **Settings** |
| 2 | Go to **Apps** → **Installed apps** |
| 3 | Search: `Python` |
| 4 | **Uninstall** every entry: <br> • `Python 3.12` (or any version) <br> • `Python Launcher` |
| 5 | **Repeat** for any old versions (3.11, 3.10, etc.) |

> **Note**: Microsoft Store Python may show as **"Python 3.12"** with a Store icon.

---

## STEP 2: **Delete Leftover Python Folders (Manual Cleanup)**

Open **File Explorer** and **delete** these folders (if they exist):

| Folder | Path |
|--------|------|
| Python.org install | `C:\Users\<YourName>\AppData\Local\Programs\Python\` |
| Python cache | `C:\Users\<YourName>\AppData\Local\pip\` |
| Virtual envs | `C:\Users\<YourName>\.virtualenvs\` (if any) |
| Microsoft Store Python | `C:\Users\<YourName>\AppData\Local\Microsoft\WindowsApps\python*` |

> **Tip**: Press **Win + R** → type `%appdata%` → go up one level → `Local` → delete folders above.

---

## STEP 3: **Disable App Execution Aliases (CRITICAL!)**

This **blocks** Windows from hijacking `python` command.

1. **Settings** → **Apps** → **App execution aliases**  
   *(Search “aliases” in Start menu if lost)*
2. Find these two:
   - `python.exe` → **Turn OFF**
   - `python3.exe` → **Turn OFF**
3. **Close Settings**

> **If you skip this, python.org will be ignored!**

---

## STEP 4: **Download & Install Python from python.org**

1. Go to: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click **“Download Python 3.12.x”** (latest stable)
3. **Save** the `.exe` file
4. **Right-click → Run as administrator**
5. **CHECK THESE BOXES**:
   - [x] **Add Python to PATH**
   - [x] **Install launcher for all users** *(recommended)*
6. Click **“Install Now”**
7. Wait → **Close**

---

## STEP 5: **Restart Computer**

> **MANDATORY**: Windows needs a full reboot to clear PATH and aliases.

---

## STEP 6: **Verify Clean Install**

Open **Command Prompt** (or PowerShell):

```bash
python --version
# → Python 3.12.x

pip --version
# → pip 24.x from ...AppData\Local\Programs\Python\...

where python
# → Should show ONLY: C:\Users\<You>\AppData\Local\Programs\Python\Python312\python.exe
```

> If you see `WindowsApps\python.exe`, **aliases are still ON** → go back to Step 3.

---

## STEP 7: **Test Pygame in Virtual Environment**

```bash
# Create project
mkdir pygame-test
cd pygame-test

# Create venv
python -m venv venv

# Activate
venv\Scripts\activate

# Install pygame
pip install pygame

# Test
python -c "import pygame; print('Pygame works! Version:', pygame.version.ver)"
```

---

## FINAL CHECKLIST (Copy & Paste)

```txt
[ ] Uninstall ALL Python (Settings > Apps)
[ ] Delete folders: AppData\Local\Programs\Python\
[ ] Delete: AppData\Local\pip\
[ ] Settings → App execution aliases → OFF: python.exe & python3.exe
[ ] Download python.org installer
[ ] Run as admin → CHECK "Add to PATH"
[ ] Install → Restart PC
[ ] CMD: python --version → works
[ ] CMD: where python → only python.org path
[ ] python -m venv venv → works
[ ] pip install pygame → works
```

---

## Optional: VS Code Setup

1. Open folder in **VS Code**
2. `Ctrl+Shift+P` → **“Python: Select Interpreter”**
3. Pick: `.\venv\Scripts\python.exe`

---
