# Why Pygame Only Worked After Switching to Microsoft Store Python on Windows 11

The issue you're describing is a **classic Python-on-Windows PATH and environment problem**, caused by **two conflicting Python installations** — one from **python.org** (the official installer) and one from the **Microsoft Store** — fighting for control over the `python` and `pip` commands.

Here's exactly what happened and why the Microsoft Store version "fixed" it:

---

## Root Cause: **Two Pythons, One Command**

1. **You installed Python from python.org**  
   → This installs Python in a folder like:  
   `C:\Users\<YourName>\AppData\Local\Programs\Python\Python312\`

   → It *should* add itself to your system **PATH**, but **sometimes fails** (especially if not run as admin or if "Add to PATH" is unchecked).

2. **Windows 11 also has a built-in "Python" app in the Microsoft Store**  
   → This is **not** full Python — it's a **stub/launcher** that redirects `python` commands to install Python **from the Store** if needed.

   → When you type `python` in CMD/PowerShell **before** installing from python.org, Windows may have already "reserved" the `python` command for the **Store version**.

3. **Result: Command-line confusion**
   ```bash
   > python --version
   Python 3.12.6   # ← This might show python.org version
   > pip --version
   pip 24.0 ... (from C:\Users\...\AppData\Local\Programs\Python\...)  # python.org
   ```
   But when you run `python -m pip install pygame`, it might fail with:
   ```
   'python' is not recognized...
   ```
   or
   ```
   No module named pygame
   ```
   ...even though it *should* work.

   **Why?** Because **some tools (like VS Code, PyCharm, or even `python -m pygame`) use the wrong Python executable** due to **PATH precedence** or **Windows App Execution Aliases**.

---

## The Real Culprit: **App Execution Aliases** (Windows 11 Feature)

Windows 11 has a hidden feature called **App Execution Aliases** that **reserves** `python.exe` and `python3.exe` for the **Microsoft Store** version — **even if you never installed it**.

- Go to: **Settings > Apps > Apps & features > App execution aliases**
- You'll likely see:
  ```
  [x] python.exe      → Microsoft Store
  [x] python3.exe     → Microsoft Store
  ```

These **override** your python.org installation in many contexts (especially in **VS Code**, **Windows Terminal**, or when double-clicking `.py` files).

So even though `python --version` works in CMD, **pygame can't find the right environment** because:
- The editor or script runner is using the **Store stub**
- The Store version has **no `pip` or site-packages** until fully installed
- Your `pygame` was installed to the **python.org** Python, not the Store one

---

## Why Microsoft Store Python "Fixed" It

When you:
1. **Uninstalled python.org Python**
2. **Installed Python from Microsoft Store**

You now have:
- A **single, consistent** Python environment
- `python`, `pip`, and `pygame` all point to the **same** installation
- No alias conflicts
- Full integration with Windows (Start menu, file associations, etc.)
- `pip install pygame` installs to the **correct** `site-packages`

> **Microsoft Store Python is *not* inferior** — it's actually a **full, official CPython** build, just packaged differently.

---

## Best Practice Going Forward

| Option | Recommendation |
|--------|----------------|
| **Use Microsoft Store Python** | **Yes, for students & beginners** — simpler, fewer PATH issues |
| **Use python.org** | Only if you need advanced control (multiple versions, virtualenvs, etc.) — but **disable App Execution Aliases** |

### If you must use python.org:
1. Uninstall **both** Pythons
2. Go to **Settings > Apps > App execution aliases**
3. **Turn OFF** `python.exe` and `python3.exe`
4. Install Python from **python.org** → **Check "Add to PATH"**
5. Restart terminal/IDE

---

## TL;DR: Why It Broke & Fixed

| Step | What Happened |
|------|---------------|
| Installed python.org | Added Python, but **blocked by Windows aliases** |
| `pip install pygame` | Installed to wrong/hidden Python |
| Scripts/IDE failed | Used **Store stub**, not real Python |
| Uninstalled + used Store | **One clean Python** → everything works |

---

## Pro Tip for Teachers

Tell students:

> **"On Windows 11, install Python from the Microsoft Store — it's easier and avoids headaches."**

Or create a simple checklist:

```txt
✅ Uninstall all Python
✅ Settings → Turn OFF python.exe & python3.exe aliases
✅ Install from python.org + check "Add Python to PATH"
✅ Restart computer
```

---

