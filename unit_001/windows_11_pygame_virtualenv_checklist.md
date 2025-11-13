# **Pygame-Ready + Virtual Environments Checklist**  
*For Windows 11 Students – Clean, Reliable, Teacher-Approved*

---

## GOAL  
Set up **Python + Pygame + Virtual Environment** so every project is isolated, portable, and **100% reproducible**.

---

## OPTION 1: **EASIEST – Microsoft Store Python (Recommended)**

| Step | Action |
|------|--------|
| 1 | Open **Microsoft Store** |
| 2 | Search: `Python 3.12` → Click **Get** |
| 3 | Wait for install → Open **Command Prompt** |
| 4 | Verify: `python --version` → *shows 3.12.x* |
| 5 | Upgrade pip: `python -m pip install --upgrade pip` |

---

## OPTION 2: **python.org (For Virtual Env Control)**  
*(Only if you need multiple Python versions)*

| Step | Action |
|------|--------|
| 1 | **Uninstall all Python** (Settings > Apps) |
| 2 | **Settings → Apps → App execution aliases** |
| 3 | **Turn OFF**: `python.exe` & `python3.exe` |
| 4 | Go to [python.org/downloads](https://www.python.org/downloads/) |
| 5 | Download **Windows installer** |
| 6 | Run → **CHECK**: `Add Python to PATH` |
| 7 | Click **Install Now** |
| 8 | **Restart computer** |

---

## STEP 2: Create a Pygame Project with Virtual Environment

> **Do this for *every new project*** (e.g., `space-game`, `platformer`)

```bash
# 1. Open Command Prompt (or PowerShell)
# 2. Navigate to your projects folder
cd Desktop\PythonProjects

# 3. Create project folder
mkdir my-pygame-game
cd my-pygame-game

# 4. Create virtual environment
python -m venv venv

# 5. ACTIVATE it
venv\Scripts\activate
# → You’ll see (venv) in prompt

# 6. Install Pygame
pip install pygame

# 7. Test it!
python -c "import pygame; print('Pygame ready!')"
```

---

## Project Folder Structure (What You Should See)

```
my-pygame-game/
│
├── venv/                  ← Virtual environment (DO NOT SHARE)
├── main.py                ← Your game code
└── README.md              ← Optional instructions
```

---

## Daily Workflow (Quick Checklist)

| When You Start | Command |
|----------------|---------|
| Open project folder | `cd Desktop\PythonProjects\my-pygame-game` |
| Activate venv | `venv\Scripts\activate` |
| Run game | `python main.py` |
| Install new package | `pip install <package>` |
| Save requirements | `pip freeze > requirements.txt` |

---

## Share Project with Others (requirements.txt)

```bash
# Inside activated venv
pip freeze > requirements.txt
```

→ Share the **entire folder** (except `venv/`)  
→ Others install with:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## VS Code Setup (Optional but Awesome)

1. Open folder in **VS Code**
2. `Ctrl+Shift+P` → **"Python: Select Interpreter"**
3. Choose: `.\venv\Scripts\python.exe`
4. Install **Pylance** + **Python** extensions
5. Run: `F5` or `python main.py`

---

## Troubleshooting Cheat Sheet

| Problem | Fix |
|-------|-----|
| `pygame` not found | Did you **activate** `venv\Scripts\activate`? |
| `python` not recognized | Use **Microsoft Store** or fix PATH + disable aliases |
| `pip` installs globally | You forgot to activate the venv |
| VS Code uses wrong Python | Select interpreter: `.\venv\Scripts\python.exe` |

---

## Printable One-Page Checklist (Copy & Paste)

```txt
PYGAME + VENV CHECKLIST
-----------------------
[ ] Install Python (Store = easy, python.org = advanced)
[ ] IF python.org: Disable App Execution Aliases
[ ] Open CMD → cd to project folder
[ ] python -m venv venv
[ ] venv\Scripts\activate
[ ] pip install pygame
[ ] python -c "import pygame; print('Ready!')"
[ ] Code in main.py → Run with python main.py
[ ] Save: pip freeze > requirements.txt
```
