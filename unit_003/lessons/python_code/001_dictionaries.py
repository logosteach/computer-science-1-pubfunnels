import subprocess
import os


def clear_screen():
    if os.name == "nt":  # Windows
        subprocess.run("cls", shell=True)
    else:  # macOS and Linux
        subprocess.run("clear", shell=True)


clear_screen()

# Dictionary
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

person = dict(name="David", age=30, city="Jerusalem", hair_color="brown")
