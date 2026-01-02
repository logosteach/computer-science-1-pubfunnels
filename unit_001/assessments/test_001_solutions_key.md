### Multiple-Choice Answers Key

| Question # | Correct Answer | Brief Explanation |
|------------|----------------|--------------------|
| 1 | B | IDLE has two main modes/windows: the interactive shell (>>> chevrons) and the script editor window. |
| 2 | D | `my_score` is valid: uses lowercase letters, numbers, and underscores; does not start with a number, contain spaces/hyphens, or use keywords. |
| 3 | C | snake_case uses all lowercase letters with underscores separating words (e.g., `student_name`). |
| 4 | A | Spaces are not allowed in variable names; Python treats them as syntax errors (separate tokens). Brevity is a style guideline, not the cause of the immediate error. |
| 5 | C | In this class, the >>> symbol in the IDLE shell is called "chevrons". |
| 6 | C | Python interprets `xy` as a variable name; since no variable named `xy` exists, it raises a NameError. Implicit multiplication from math notation is not supported. |
| 7 | A | Yes, IDLE's editor window can display line numbers via configuration in Options → Configure IDLE. |
| 8 | A | Concatenation with `+` joins the string and variable directly, producing the exact output without extra spaces. Commas add automatic spaces. |
| 9 | A | Yes, IDLE can be configured (Options → Configure IDLE → General) to open directly to the editor or shell on launch. |
| 10 | A | `**` is the exponentiation operator; `2 * x ** 2 - y` correctly computes 2 × x² − y. |
| 11 | B | Setting `end="&"` replaces the default newline with "&", so all prints appear on the same line joined by ampersands. |
| 12 | C | You cannot directly concatenate a string and an integer with `+`; Python requires `str()` conversion first, otherwise a TypeError occurs. |
| 13 | A | Uses variables, correct `str(age)` conversion, concatenation, and produces exact two-line output. Other options either hard-code values, cause errors, or add unwanted spaces. |
| 14 | B | SyntaxError means Python cannot parse the code due to invalid structure/grammar before attempting to run it. |
| 15 | B | SyntaxError is detected during parsing (before running); NameError occurs during execution when a name/variable is undefined. |
| 16 | B | `from math import sqrt` is the correct import syntax students learned to use `sqrt()` directly. |
| 17 | D | Uses the exact import taught (`from math import sqrt`) and correctly prints √144 = 12.0 using the Pythagorean theorem context. |
| 18 | A | High downloads + many reviews + reputable publisher (Microsoft) indicate the extension is widely used, tested, and trustworthy. |
| 19 | B | Create the folder on the file system first, then open it in VS Code via File → Open Folder. |
| 20 | B | The simplest mouse-only method is drag-and-drop in the Explorer sidebar; no keyboard shortcuts or extra steps needed. |

### Free-Response Answers Key / Grading Guidance

**Important Reminder for Grading:**  
Answers may vary in wording, but all responses must be written in **complete, clear sentences** with sufficient detail to demonstrate understanding. One- or two-word answers, bullet points without full sentences, or vague responses should receive little to no credit.

Below are sample acceptable answers, variations that are still acceptable, and examples of unacceptable answers for each question.

**Question 1**  
Describe... the exact steps to configure IDLE so that line numbers are displayed...

**Acceptable Answer Example:**  
I am using Windows. After opening IDLE, I click on the "Options" menu at the top, then select "Configure IDLE". In the settings window that appears, I click on the "General" tab. Under the "Editor" section, I check the box that says "Show line numbers in new windows" and then click "Apply" or "OK" to save the change.

**Acceptable Variations:**  
- Mentioning keyboard shortcut Alt+O to open Options.  
- Saying "Fonts/Tabs" tab instead of General (some versions differ slightly).  
- Describing clicking "OK" then restarting IDLE for the change to take effect.

**Unacceptable Answers:**  
- "Go to configure IDLE and turn on line numbers." (too vague, not step-by-step)  
- Bullet list without full sentences.  
- "Check the box for line numbers." (missing all menu navigation)  
- Forgetting to state the operating system.

**Question 2**  
Explain... why it is important to carefully check the number of downloads, reviews, and publisher...

**Acceptable Answer Example:**  
Checking the number of downloads tells me how widely used and tested the extension is — a high number means many people trust it. The number and content of reviews show whether users find it reliable and helpful; many positive reviews with detailed comments are a good sign. The publisher is important because well-known companies like Microsoft are less likely to release harmful code. Together, these factors help protect my computer from malicious extensions and ensure I install a high-quality tool that works well.

**Acceptable Variations:**  
- Mentioning that low downloads might indicate a new or untrusted extension.  
- Noting that a reputable publisher often provides updates and support.  
- Adding that reading actual review content can reveal bugs or issues.

**Unacceptable Answers:**  
- "Because it's important." or "To be safe." (no explanation)  
- Listing only one factor without explaining the others.  
- "Downloads show it's popular." (partial, lacks depth on all three factors)

**Question 3**  
Describe... the step-by-step process to save a Python script... and then run it.

**Acceptable Answer Example:**  
To save the script, I go to the File menu in the IDLE editor window and choose "Save" (or press Ctrl+S). A dialog box appears where I choose a location and type a file name ending in .py, such as hello.py, then click Save. To run the script, I go to the Run menu and select "Run Module" (or press F5). The output then appears in the IDLE shell window.

**Acceptable Variations:**  
- Mentioning "Save As" for the first save.  
- Describing choosing a folder inside their project.  
- Noting that after running, the shell restarts with >>> if needed.

**Unacceptable Answers:**  
- "Click save and then run." (no detail on menus or shortcuts)  
- "Press F5 to run." only (misses entire saving process)  
- Confusing with VS Code steps (e.g., mentioning terminal)

**Question 4**  
Describe... the step-by-step process to create a new Python file... in VS Code.

**Acceptable Answer Example:**  
With my project folder already open and visible in the Explorer sidebar on the left, I click on the Explorer icon if it's not already active. I then right-click on the project folder name (or inside it if expanded), select "New File" from the menu, and type the desired name followed by .py, such as script.py, then press Enter. VS Code creates the empty file and opens it in the editor.

**Acceptable Variations:**  
- Mentioning clicking the "New File" icon (📄) at the top of the Explorer instead of right-click.  
- Describing first expanding the folder before right-clicking inside it.  
- Noting that the file appears with a Python icon once .py is used.

**Unacceptable Answers:**  
- "Click New File and type the name." (missing where to click or right-click context)  
- Describing steps in IDLE or File Explorer instead of VS Code Explorer.  
- "Go to File → New File and save as .py." (this creates an untitled file, not directly in the folder the way taught)

### Programming Questions Solutions / Sample Answers

**Important Reminder for Grading:**  
Solutions may vary in minor ways (e.g., extra spaces in variable names, different order of statements, or small stylistic differences), as long as the program meets **all** specified requirements, runs correctly in standard Python 3, and produces the **exact** required output. Partial credit can be given for code that is close but has small errors (e.g., missing period, extra space).

Below are correct sample solutions for each programming problem.

**Programming Question 1** – Hypotenuse using Pythagorean theorem

```python
from math import sqrt

# Legs of the triangle
a = 5
b = 8

# Calculate hypotenuse: sqrt(a² + b²)
hypotenuse = sqrt(a**2 + b**2)

# Print exactly as specified
print("The hypotenuse of a triangle with legs of 5 and 8 inches is: " + str(hypotenuse) + ".")
```

**Acceptable Variations:**  
- Using different variable names (e.g., `leg1`, `leg2`).  
- Computing directly in the print: `print("The hypotenuse... " + str(sqrt(5**2 + 8**2)) + ".")`  
- Adding comments or extra whitespace.

**Programming Question 2** – Diamond made of `#` characters

```python
print("   " + "#" * 1 + "   ")
print("  " + "#" * 3 + "  ")
print(" " + "#" * 5 + " ")
print("#" * 7)
print(" " + "#" * 5 + " ")
print("  " + "#" * 3 + "  ")
print("   " + "#" * 1 + "   ")
```

**Acceptable Variations:**  
- Using `end=""` with multiple prints per line (e.g., `print("   ", end=""); print("#", end=""); print("   ")`).  
- Building strings with variables or different spacing formulas, as long as output is exact.

**Programming Question 3** – Introduce yourself using variables and concatenation

```python
name = "John Smith"  # Replace with student's actual name
age = 17             # Replace with student's actual age

print("Hello Everyone! My name is " + name + ".")
print("I am " + str(age) + " years old.")
```

**Acceptable Variations:**  
- Different name and age values (must be the student's own).  
- Extra variables or comments.  
- Slight differences in spacing inside strings as long as final output has no extra/missing spaces.

**Programming Question 4** – Bordered label with stars

```python
print("*" * 26)
print("*" + " " * 24 + "*")
print("*" + "    Welcome to Python!    " + "*")
print("*" + " " * 24 + "*")
print("*" * 26)
```

**Acceptable Variations:**  
- Using `end=""` to build lines horizontally.  
- Calculating the number of spaces using variables or len().  
- Slight differences in internal spacing as long as visual alignment matches exactly.

**Programming Question 5** – VS Code folder/file organization (no code)

This is a hands-on task.  
**Correct Solution:** The submitted screenshot must show:  
- A folder named `test_1` open in VS Code  
- Three subfolders: `multi`, `free_rep`, `prog`  
- Inside `multi`: exactly `m1.py` through `m20.py` (20 files)  
- Inside `free_rep`: exactly `f1.py` through `f5.py` (5 files)  
- Inside `prog`: exactly `p1.py` through `p5.py` (5 files)  

All names must be lowercase and exactly as specified.  
Partial credit can be given for nearly complete structures (e.g., 18/20 files in multi).