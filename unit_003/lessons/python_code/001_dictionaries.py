import subprocess
import os, sys
from pathlib import Path

# Add the templates folder to Python's search path
root_dir = Path(__file__).parent.parent.parent.parent  # Goes up to root_folder
templates_dir = root_dir / "templates"
sys.path.insert(0, str(templates_dir))

import lesson_macro

lesson_title = "Python Dictionaries"
description = ".keys(), .values(), .items()"
year = 2026
org = "LogosTeach"
url = "https://www.logosteach.com"


def print_copyright(year, org):
    print(f"Copyright {year} {org} - All rights reserved.")
    print(f"{url}")


def print_lesson_info(lesson_title, description):
    print(f"Lesson: {lesson_title}")
    print(f"Description: {description}")
    print("-" * 40)


lesson_macro.clear_screen()
times_run = lesson_macro.get_run_count()

if times_run == 0:
    print_copyright(year, org)
    print_lesson_info(lesson_title, description)

times_run += 1
lesson_macro.save_run_count(times_run)

############################################
