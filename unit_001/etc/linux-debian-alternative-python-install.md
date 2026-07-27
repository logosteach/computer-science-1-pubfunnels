
# Installing Python from python.org on Linux

These instructions work on almost any Linux distribution and any architecture (x86_64, arm64, etc.). Follow the steps in order.

---

## 1. Download Python from the Official Website

1. Open your web browser and go to:  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Click the big yellow button that says **Download Python 3.x.x**  
   (It will automatically choose the correct version for your system.)

3. Save the file (it will be a `.tar.xz` file).

---

## 2. Install the Required Build Tools

Open a terminal and run:

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev \
libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev \
libffi-dev uuid-dev tk-dev
```

---

## 3. Compile and Install Python

1. Go to the folder where you downloaded the file (usually `~/Downloads`):

```bash
cd ~/Downloads
```

2. Extract the file (replace the filename with the one you actually downloaded):

```bash
tar -xf Python-3.*.tar.xz
cd Python-3.*/
```

3. Configure, compile, and install:

```bash
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

> **Note:** We use `altinstall` so we don’t overwrite the system Python.

---

## 4. Verify the Installation

```bash
python3.13 --version
```

(You should see something like `Python 3.13.x`)

You can also create a convenient shortcut:

```bash
sudo ln -s /usr/local/bin/python3.13 /usr/local/bin/python3
```

---

## 5. Install pip and IDLE

```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

# Install IDLE
sudo apt install -y idle3
```

Test IDLE:

```bash
idle3
```

---

## 6. Install Popular Python Packages

```bash
python3 -m pip install requests numpy matplotlib pandas pillow
```

Optional extra packages:

```bash
python3 -m pip install scipy sympy pytest
```

---

## 7. Install Visual Studio Code

The easiest cross-architecture method is to download the official `.deb` package:

1. Go to: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click **Download for Linux**
3. Choose the **.deb** package
4. Once downloaded, install it with:

```bash
cd ~/Downloads
sudo apt install ./code_*.deb
```

---

## 8. Install the Python Extension in VS Code

1. Open VS Code
2. Click the **Extensions** icon (or press `Ctrl+Shift+X`)
3. Search for **Python**
4. Install the official extension by **Microsoft**

---

## 9. Final Check

Run these commands to confirm everything works:

```bash
python3 --version
python3 -c "import requests, numpy, matplotlib, pandas; print('All packages imported successfully!')"
idle3
code --version
```