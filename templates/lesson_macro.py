import os, subprocess
from pathlib import Path

MODULE_DIR = Path(__file__).parent.resolve()
FILE_NAME = MODULE_DIR / "times_run.txt"
# ======================
# TIMES RUN TRACKER
# ======================


def get_run_count():
    """Read how many times the program has run"""
    if not os.path.exists(FILE_NAME):
        # First time ever - create file with 0
        with open(FILE_NAME, "w") as f:
            f.write("0")
        return 0

    with open(FILE_NAME, "r") as f:
        try:
            count = int(f.read().strip())
            return count
        except:
            return 0  # if file is corrupted


def save_run_count(count):
    """Save the updated count back to the file"""
    with open(FILE_NAME, "w") as f:
        f.write(str(count))


def reset_count():
    """Reset the run counter back to 0"""
    save_run_count(0)


def clear_screen():
    if os.name == "nt":  # Windows
        subprocess.run("cls", shell=True)
    else:  # macOS and Linux
        subprocess.run("clear", shell=True)
