
# Step 5: Finish Setting Up Your New Python

You have successfully compiled and installed Python 3.13.14.  
Now we will check that everything works, create convenient shortcuts, and install the most common packages that normally come with a full Python installation on Windows or macOS.

---

## 5.1 Check the Python Version

Type this command:

```bash
python3.13 --version
```

You should see:

```
Python 3.13.14
```

This confirms that the new version is installed correctly.

---

## 5.2 Create a Convenient Shortcut

Right now you have to type `python3.13` every time.  
Let’s make a shorter command so you can just type `python3`.

```bash
sudo ln -sf /usr/local/bin/python3.13 /usr/local/bin/python3
```

**What this does:**  
It creates a shortcut (called a symbolic link) so that when you type `python3`, the system uses your new Python 3.13.14.

Test it:

```bash
python3 --version
```

---

## 5.3 Make Sure pip Is Installed and Updated

`pip` is the tool used to install extra Python packages.  
Even though we just installed Python, we should make sure pip is ready.

```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

---

## 5.4 Install Common Packages

A full Python installation on Windows or macOS usually includes (or makes it easy to get) several popular packages.  
We will install the ones most beginners need right away:

```bash
python3 -m pip install requests numpy matplotlib pandas pillow
```

**What these packages are used for:**

| Package      | Common Use                              |
|--------------|-----------------------------------------|
| `requests`   | Downloading data from the internet      |
| `numpy`      | Working with numbers and arrays         |
| `matplotlib` | Creating graphs and charts              |
| `pandas`     | Working with tables and data            |
| `pillow`     | Working with images                     |

### Optional but useful packages

If you want a few more commonly used tools, you can also install these:

```bash
python3 -m pip install scipy sympy pytest
```

---

## 5.5 Final Check

Run this command to make sure the main packages work:

```bash
python3 -c "import requests, numpy, matplotlib, pandas, PIL; print('All common packages imported successfully!')"
```

If you see the success message, everything is working correctly.

---

You now have a complete Python 3.13.14 installation that is very similar to a full installation on Windows or macOS.
