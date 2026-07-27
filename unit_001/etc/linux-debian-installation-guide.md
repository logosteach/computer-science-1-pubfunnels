
# Installing Python, IDLE, Common Packages, and VS Code on Debian 13 (Trixie)

These step-by-step instructions are written for beginners. Follow them in order. Open the **Terminal** application first (you can search for “Terminal” in the application menu).

---

## 1. Update Your System

Copy and paste each command, then press **Enter**. Enter your password when asked (you will not see characters as you type).

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 2. Install Python, IDLE, and Essential Tools

Debian 13 comes with Python 3.13. This command installs everything needed for beginners:

```bash
sudo apt install -y python3 python3-pip python3-venv python3-tk idle idle-python3.13 python3-full
```

**What this installs:**

- `python3` – the Python interpreter
- `python3-pip` – package installer
- `python3-venv` – virtual environments
- `python3-tk` + `idle` / `idle-python3.13` – IDLE (the simple Python editor)
- `python3-full` – extra standard library modules

**Verify the installation:**

```bash
python3 --version
idle --version
```

You should see something like `Python 3.13.x`.

---

## 3. Install Popular Python Packages (Recommended for Beginners)

These are the most useful packages for a first course. Install them with `apt` (the safest method on Debian):

```bash
sudo apt install -y python3-requests python3-numpy python3-matplotlib python3-pandas python3-pillow
```

**Optional extra useful packages:**

```bash
sudo apt install -y python3-scipy python3-sympy python3-pytest
```

**Note:** On modern Debian, using `pip install` system-wide is blocked by default (PEP 668). Prefer `apt` packages when available. For project-specific packages later, use a virtual environment.

---

## 4. Install Visual Studio Code (Official Microsoft Version)

This method adds Microsoft’s repository so VS Code stays updated automatically.

```bash
# Install required tools
sudo apt install -y wget gpg apt-transport-https

# Add Microsoft’s signing key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/packages.microsoft.gpg

# Add the VS Code repository
echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list

# Update and install
sudo apt update
sudo apt install -y code
```

**Launch VS Code** from the application menu or by typing:

```bash
code
```

---

## 5. Install the Python Extension Inside VS Code

1. Open VS Code.
2. Click the **Extensions** icon on the left sidebar (or press `Ctrl+Shift+X`).
3. Search for **Python**.
4. Install the official extension by **Microsoft** (it is usually the first result).
5. (Optional but recommended) Also install **Pylance** if it is not already included.

---

## 6. Final Verification

In the Terminal, run these checks:

```bash
python3 --version
python3 -c "import requests, numpy, matplotlib, pandas; print('All packages imported successfully!')"
idle &          # Opens IDLE
code --version  # Shows VS Code version
```

---

## Quick Tips for Students

- To open IDLE later: type `idle` in the terminal or search for “IDLE” in the menu.
- Always use `python3` (not just `python`) on Debian.
- For future projects, create a virtual environment:

  ```bash
  python3 -m venv myproject
  source myproject/bin/activate
  ```

- Keep your system updated regularly with:

  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

You now have a complete beginner-friendly Python development environment on Debian 13.

&copy; 2026 LogosTeach - All Rights Reserved