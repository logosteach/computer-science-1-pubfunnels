# How to Start the IDLE Shell on Debian Linux

> **IDLE** is Python’s built-in editor and interactive shell — perfect for learning and testing code!

---

## Method 1: Applications Menu (Easiest)

1. Click the **Applications** menu (or **Activities** in GNOME)  
2. Go to **Programming** or search: `IDLE`  
3. Click **IDLE** (or **IDLE 3**)  

→ The IDLE shell opens!

---

## Method 2: Terminal (Recommended)

1. Open **Terminal**  
2. Type:
   ```bash
   idle
   ```
   or for Python 3:
   ```bash
   idle3
   ```
3. Press **Enter**

> **Tip**: Use `idle3 -n` to skip the startup dialog.

---

## Method 3: Run from Python

1. Open **Terminal**  
2. Run:
   ```bash
   python3 -m idlelib
   ```
3. Press **Enter**

---

## Method 4: Create a Desktop Launcher

1. Right-click Desktop → **Create Launcher**  
2. Fill in:
   - **Name**: `IDLE Shell`
   - **Command**: `idle3`
   - **Icon**: (optional) browse to `/usr/share/pixmaps/python3.xpm`
3. Click **OK** → Double-click to launch!

---

## What You’ll See

```
Python 3.11.2 (main, ...) on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>>
```

→ Type code and press **Enter** to run!

```python
>>> print("Hello from Debian!")
Hello from Debian!
```

---

## Install IDLE (If Missing)

Run in **Terminal**:

```bash
sudo apt update
sudo apt install idle3
```

> This installs IDLE for Python 3.

---

## Troubleshooting

| Problem | Fix |
|--------|-----|
| `idle3: command not found` | Run: `sudo apt install idle3` |
| IDLE opens but no shell | Try: `python3 -m idlelib` |
| Wrong Python version | Use `idle3.11` or `idle3.12` if multiple versions exist |

---

**Pro Tip:**  
> **Pin IDLE to your panel!** Right-click the IDLE icon in the menu → **Add to Favorites**.

---

**You're ready to code in IDLE on Debian!**
