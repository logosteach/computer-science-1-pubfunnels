# **How to Start the IDLE Shell on Windows 10 & 11**

> **IDLE** is Python’s built-in code editor and interactive shell — perfect for testing code quickly!

---

## **Method 1: Start Menu (Easiest)**

| Windows 10 | Windows 11 |
|------------|------------|
| 1. Click **Start** → type `IDLE` <br> 2. Click **IDLE (Python 3.12)** | 1. Click **Start** → type `IDLE` <br> 2. Click **IDLE (Python 3.12 64-bit)** |

→ The **IDLE Shell** window opens instantly!

---

## **Method 2: Run Command (Fast for Pros)**

1. Press **Win + R**  
2. Type:  
   ```bash
   python -m idlelib
   ```  
3. Press **Enter**

→ IDLE opens!

> **Tip**: Use `python -m idlelib -n` to open **without** the startup dialog.

---

## **Method 3: From Command Prompt**

1. Open **Command Prompt** (`cmd`)  
2. Type:
   ```bash
   python -m idlelib
   ```
3. Press **Enter**

---

## **Method 4: Desktop Shortcut (Optional)**

1. Right-click Desktop → **New → Shortcut**  
2. Location:
   ```text
   pythonw.exe -m idlelib
   ```
   *(Find `pythonw.exe` in: `C:\Users\YourName\AppData\Local\Programs\Python\Python312\`)*  
3. Name: `IDLE Shell`  
4. Click **Finish** → Double-click to launch!

---

## **What You’ll See**

```
Python 3.12.6 | packaged by python.org | ...
Type "help", "copyright", "credits" or "license()" for more information.
>>>
```

→ Type Python code here and press **Enter** to run it instantly!

```python
>>> print("Hello, World!")
Hello, World!
```

---

## **Troubleshooting**

| Problem | Fix |
|---------|-----|
| `IDLE` not found in Start | Python not in PATH → Reinstall with **"Add to PATH"** checked |
| Nothing happens when clicking | Use **Run as administrator** or fix App Execution Aliases |
| Two IDLEs appear | You have **Store + python.org** → follow clean install guide |

---

**Pro Tip for Students:**  
> **Pin IDLE to your taskbar!** Right-click the IDLE icon → **Pin to taskbar** → one-click coding!

---
