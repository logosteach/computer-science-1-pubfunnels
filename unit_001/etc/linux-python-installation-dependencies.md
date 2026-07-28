
# Installing the Required Tools Before Compiling Python

Before you can compile Python from source, your Linux system needs some special tools and libraries.  
These are called **build dependencies**.

Think of them like the tools a carpenter needs before building a house — without them, the building process will fail.

---

## Step 1: Update Your System

Open the Terminal and type this command, then press **Enter**:

```bash
sudo apt update
```

---

## Step 2: Install All the Required Packages

Copy and paste the entire command below into the Terminal and press **Enter**:

```bash
sudo apt install -y build-essential libssl-dev zlib1g-dev \
libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev \
libffi-dev uuid-dev tk-dev
```

### What these packages do (simple explanation)

| Package                  | Purpose                                      |
|--------------------------|----------------------------------------------|
| `build-essential`        | Includes the basic tools (`make`, `gcc`, etc.) needed to compile software |
| `libssl-dev`             | Needed for secure connections (HTTPS)        |
| `zlib1g-dev`             | Helps with compression                       |
| `libncurses5-dev` + `libncursesw5-dev` | Needed for text-based interfaces   |
| `libreadline-dev`        | Makes the interactive Python shell nicer     |
| `libsqlite3-dev`         | Allows Python to work with SQLite databases  |
| `libgdbm-dev`            | Supports certain database features           |
| `libdb5.3-dev`           | Another database library                     |
| `libbz2-dev`             | Helps with `.bz2` compression                |
| `libexpat1-dev`          | Needed for XML processing                    |
| `liblzma-dev`            | Helps with `.xz` compression                 |
| `libffi-dev`             | Allows Python to talk to other languages     |
| `uuid-dev`               | Generates unique IDs                         |
| `tk-dev`                 | Needed so IDLE (Python’s editor) can work    |

---

## Step 3: Wait for the Installation to Finish

You will see a lot of text scrolling by. This is normal.  
When it finishes and you see your command prompt again, you are ready for the next step (unpacking and compiling Python).

You only need to do this ONCE!

&copy; 2026 LogosTeach - All Rights Reserved