# How to Start the IDLE Shell on macOS

> **IDLE** is Python’s built-in editor and interactive shell — great for testing code quickly!

---

## Method 1: Spotlight Search (Fastest)

1. Press **Cmd + Space** to open Spotlight  
2. Type: `IDLE`  
3. Press **Enter** when **IDLE.app** appears  

→ The IDLE shell window opens!

---

## Method 2: Applications Folder

1. Open **Finder**  
2. Go to **Applications**  
3. Open the **Python 3.12** folder (or similar)  
4. Double-click **IDLE.app**

---

## Method 3: Terminal (For Advanced Users)

1. Open **Terminal** (from Spotlight: type `Terminal`)  
2. Run:
   ```bash
   python3 -m idlelib
   ```
3. Press **Enter**

> **Tip**: Use `python3 -m idlelib -n` to skip the startup dialog.

---

## Method 4: Create a Desktop/Alias Shortcut

1. Go to **Applications → Python 3.12 → IDLE.app**  
2. **Right-click** → **Make Alias**  
3. Drag the alias to your **Desktop** or **Dock**  
4. Click it anytime to launch IDLE!

---

## What You’ll See

```
Python 3.12.6 (main, ...)
Type "help", "copyright", "credits" or "license()" for more information.
>>>
```

→ Type code and press **Enter** to run it instantly!

```python
>>> print("Hello from macOS!")
Hello from macOS!
```

---

## Troubleshooting

| Problem | Fix |
|--------|-----|
| `IDLE` not found | Python not installed → [Download from python.org](https://www.python.org/downloads/macos/) |
| `python3: command not found` | Reinstall Python and **check "Install for all users"** |
| IDLE opens but shell is blank | Restart your Mac or reinstall Python |

---

**Pro Tip:**  
> **Add IDLE to your Dock!** Drag **IDLE.app** from Applications → Python folder into the Dock for one-click access.

--- 

**You're ready to code in IDLE on macOS!**
