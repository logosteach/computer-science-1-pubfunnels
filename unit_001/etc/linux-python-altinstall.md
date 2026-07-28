
# Step 4: Unpack and Install Python 3.13.14 from Source

You have already downloaded the Python 3.13.14 file.  
Now we will unpack it and install it.

---

## 4.1 Go to the Downloads Folder

Most browsers save files in the `Downloads` folder.  
Type this command and press **Enter**:

```bash
cd ~/Downloads
```

This moves you into the Downloads folder.

---

## 4.2 Unpack (Decompress) the File

The file you downloaded is compressed (like a zip file).  
We need to unpack it first.

Type this command:

```bash
tar -xf Python-3.13.14.tar.xz
```

**What this command does:**
- `tar` = the tool that works with compressed files
- `-xf` = extract the file
- `Python-3.13.14.tar.xz` = the name of the file you downloaded

After this finishes, a new folder named `Python-3.13.14` will appear.

---

## 4.3 Enter the New Folder

Move into the folder that was just created:

```bash
cd Python-3.13.14
```

---

## 4.4 Configure the Installation

Before we can install Python, we must prepare it for your computer.  
This is called **configuring**.

Type this long command carefully (you can copy and paste it):

```bash
./configure --enable-optimizations --with-tcltk-includes="-I/usr/include" --with-tcltk-libs="-L/usr/lib"
```

**Simple explanation:**
- `./configure` = checks your system and gets Python ready to be built
- `--enable-optimizations` = makes Python run a little faster
- The `--with-tcltk...` parts = make sure IDLE (the Python editor) will work

This step may take 1–2 minutes. Just wait until you see your command prompt again.

---

## 4.5 Compile Python

Now we actually build (compile) Python.  
This is the longest step.

Type:

```bash
make -j$(nproc)
```

**What this means:**
- `make` = the command that builds the software
- `-j$(nproc)` = uses all the processor cores on your computer so it finishes faster

This can take **5 to 15 minutes** depending on your computer.  
You will see a lot of text scrolling by — this is normal. Just let it finish.

---

## 4.6 Install Python (Altinstall)

Finally, we install the new Python.

Type:

```bash
sudo make altinstall
```

**Important note:**  
We use `altinstall` instead of `install` so we do **not** replace the system’s original Python. This is the safe way.

You will be asked for your password. Type it and press Enter (you will not see the letters as you type).

---

## 4.7 Check That It Worked

After the installation finishes, test it:

```bash
python3.13 --version
```

You should see:

```
Python 3.13.14
```

You can also create a shortcut so you can just type `python3`:

```bash
sudo ln -sf /usr/local/bin/python3.13 /usr/local/bin/python3
```

---

**Congratulations!**  
You have successfully compiled and installed Python 3.13.14 from source.
