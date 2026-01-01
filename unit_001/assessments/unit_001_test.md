# Unit 001 - Test

## Multiple-Choice Questions

*Directions: Choose the best answer from the five options (A–E) provided for each question.*

1. IDLE, the integrated development environment that comes with Python, provides two primary ways to interact with Python code. How many main modes (or windows) does IDLE have?  

   A) 1  
   B) 2  
   C) 3  
   D) 4  
   E) 40 (like the days and nights of rain during Noah's flood)

2. Python variable names must follow specific naming conventions. Which of the following is a **valid** variable name that would **not** cause a syntax error?  

   A) 2score  
   B) my-score  
   C) my score  
   D) my_score  
   E) fred#37

3. In Python, the conventional style for naming ordinary variables (as recommended by PEP 8) is called snake_case.  

Which of the following variable names correctly uses snake_case?  

   A) `studentName`  
   B) `StudentName`  
   C) `student_name`  
   D) `STUDENT_NAME`  
   E) `studentname#1`

4. Dustin wants to use the variable name `hit points for my hero player` in his Python code.  
   
This name will cause an immediate error when he tries to run the program.  
What is the **main reason** it will cause a syntax error?
    
A) Variable names cannot contain spaces  
B) Variable names must start with a capital letter  
C) Variable names should be kept reasonably short and concise  
D) Variable names cannot be longer than 20 characters  
E) Variable names must include at least one number

5. In the IDLE interactive shell, the symbol that appears before the cursor (where you type Python commands) looks like three consecutive greater-than signs (>>>).  
   
In this class, what do we call this symbol? 

A) The triple arrow  
B) The shell indicator  
C) Chevrons  
D) The input marker  
E) The "ready to code" blinker

6. Given the following variable assignments:  
   
```python
x = 5
y = 6
z = 7
```

Consider this line of code:  
   
```python
w = xy + z   # This line will cause an error
```

   What will happen when Python tries to execute this line?  
   A) It will calculate 5 × 6 + 7 and store 37 in w  
   B) It will calculate 5 + 6 × 7 and store 47 in w  
   C) It will produce a NameError because "xy" is not defined  
   D) It will automatically treat "xy" as multiplication and store 37 in w  
   E) It will treat "xy" as a new variable and add the value of z to it (resulting in an unpredictable number)

7. In the IDLE editor window (the window used for writing and editing Python scripts), does IDLE allow the user to display line numbers along the left margin to show which line of code they are on?  
   A) Yes  
   B) No  
   C) Only in the shell window, not the editor  
   D) Only if you install a special extension  
   E) Only if you manually type the numbers yourself at the start of each line

8. Given the following variable assignment:  
```python
name = "Henry"
```
   Which of the following `print()` statements would produce the exact output:  
   `Hello my name is Henry`  
   A) `print("Hello my name is " + name)`  
   B) `print("Hello my name is " name)`  
   C) `print("Hello my name is ", name)`  
   D) `print("Hello my name is " + "name")`  
   E) `print("Hello my name is Henry")`

::: page-break :::

9.  Does IDLE allow the user to configure it so that, when you launch the program, it opens directly to either the shell window or the editor window (instead of always opening the shell first)? 
     
A) Yes  
B) No  
C) Yes, but only on Windows  
D) Yes, but only if you create a custom shortcut  
E) No, it always opens a blank editor window with no shell

10. Given the following variable assignments:  
```python
x = 3
y = 8
```

Which of the following Python expressions would correctly calculate **two x squared minus y**  
(that is, 2 × x² − y, which equals 10)?  
A) `2 * x ** 2 - y`  
B) `2 * x * 2 - y`  
C) `2 x ** 2 - y`  
D) `2 * x * x - y`  
E) `2 x squared minus y`

11.   Students have learned that the `print()` function has a default setting that controls what is placed at the end of the printed output, but that setting can be changed using the `end` parameter.  

Consider the following Python code:  

```python
print("Apple", end="&")
print("Banana", end="&")
print("Cherry", end="&")
```

When this code is run, what will the exact output look like?  

A) Apple Banana Cherry  
B) Apple&Banana&Cherry&  
C) Apple  
    Banana  
    Cherry  
D) Apple&  
    Banana&  
    Cherry&  
E) Apple&Banana&Cherry (each on a separate line with ampersands)

::: page-break :::

12.   Given the following variable assignment:  

```python
age = 21
```

Consider this line of code:  

```python
print("I am " + age + " years old.")
```

What will happen when Python tries to execute this line?  
A) It will print: I am 21 years old.  
B) It will print: I am 21 years old. (but with extra spaces)  
C) It will produce a TypeError because you cannot concatenate a string and an integer  
D) It will automatically convert the number to a string and print the message correctly  
E) It will crash the entire computer (because numbers and words don't mix)

13.   Danielle wants to write a short Python script that produces the following exact output:  

```
Hello Everyone! My name is Danielle
I am 17 years old
```

She decides to use variables to store her name and age.  
Which of the following sets of Python statements accomplishes this goal in the **best and most minimal way**?  

A)  
```python
name = "Danielle"
age = 17
print("Hello Everyone! My name is " + name)
print("I am " + str(age) + " years old")
```  
B)  

```python
print("Hello Everyone! My name is Danielle")
print("I am 17 years old")
```  
C)  

```python
name = "Danielle"
age = 17
print("Hello Everyone! My name is ", name)
print("I am ", age, " years old")
```  

D)  
```python
name = "Danielle"
age = 17
print("Hello Everyone! My name is " + name)
print("I am " + age + " years old")
```  

E)  
```python
name = "Danielle"
age = 17
print("Hello Everyone! My name is Danielle")
print("I am 17 years old")
```

14. In Python, when you run a script or type a command and Python responds with an error message that starts with **SyntaxError**, what does this mean?  
    
A) The code ran successfully, but the output was not what you expected  
B) Python found a problem with the "grammar" or structure of the code itself, making it invalid Python before it even tries to run it  
C) There is a logical mistake in the code that causes the wrong mathematical result  
D) Python could not find a variable or function that was referenced  
E) Python ran out of memory while trying to execute the code

15.  In Python, **SyntaxError** and **NameError** are two common types of errors students encounter. 
 
What is the **key difference** between a SyntaxError and a NameError? 

A) SyntaxError happens when you use the wrong math operator (+ instead of -); NameError happens when you forget quotes around text  
B) SyntaxError occurs before Python tries to run the code (invalid structure/grammar); NameError occurs during execution (variable or name not defined)  
C) SyntaxError is only in the IDLE shell; NameError is only in saved scripts  
D) SyntaxError crashes IDLE completely; NameError just prints a warning  
E) SyntaxError means "name is too long"; NameError means "name is too short"

16.  Students have learned how to use the square root function by importing it from Python’s built-in `math` module.  

Which of the following import statements is the **correct** way to make the `sqrt` function available for use?  

A) `import sqrt from math`  
B) `from math import sqrt`  
C) `import math.sqrt`  
D) `from math import *`  
E) `sqrt = math.sqrt`

17.  Maria is building a square garden in her backyard. She has decided that the area of the garden will be exactly 144 square feet.
    
To find the length of each side, she remembers from math class that:  
**side length = the square root of the area**  
(On paper, this is written as: side = √144)  
She wants to use Python to calculate and print this value.  
Which of the following complete Python scripts correctly imports the `sqrt` function and prints the exact side length of Maria’s garden?  

A)  
```python
import math
print(math.sqrt(144))
```  
B)  
```python
from math import sqrt
print(sqrt(12))
```  
C)  
```python
from math import sqrt
print(sqrt(144 * 144))
```  
D)  
```python
from math import sqrt
print(sqrt(144))
```  
E)  
```python
import sqrt
print(sqrt(144))
```

18.  In VS Code, when browsing the Extensions Marketplace to add a Python extension for your project, you notice two similar extensions.  
    
**Extension A** has 2.5 million downloads, 4,847 reviews averaging 4.8 stars, and is published by "Microsoft".  
**Extension B** has 1,200 downloads, 3 reviews averaging 5.0 stars, and is published by "QuickCode LLC".  

Which extension should you **primarily choose**, and why?  

A) Extension A, because high download count and many reviews indicate widespread use and trustworthiness  
B) Extension B, because 5.0 stars is a perfect rating  
C) Extension A, because Microsoft is a well-known publisher you can trust  
D) Extension B, because fewer reviews mean less bias in the ratings  
E) Flip a coin between them (or choose the one with the prettiest icon)

19.  You are starting a new Python project in VS Code and want to keep your files organized.  
    
Which of the following sequences best describes the correct steps to create a dedicated project folder (named "MyPythonProject") and then open it in VS Code so you can start adding Python files inside it?  

A)  
1. In VS Code, go to File → New File  
2. Save the file as MyPythonProject.py  
3. VS Code automatically creates a folder for you  

B)  
1. On your computer, create a new folder named MyPythonProject (using File Explorer or Finder)  
2. Open VS Code  
3. In VS Code, go to File → Open Folder and select the MyPythonProject folder  

C)  
1. In VS Code, go to the Extensions view  
2. Install a special "Folder Creator" extension  
3.  Use that extension to make the folder  

D)  
1. Open VS Code first  
2. Click the Explorer icon  
3. Right-click and choose "New Project Folder" named MyPythonProject  

E)  
1. Open IDLE  
2. Save your script — VS Code will automatically detect and create the project folder


20. You have opened a project folder in VS Code and created several Python files and sub-folders inside it. Now you want to reorganize by moving a file named `hello.py` from the main project folder into a subfolder named `scripts`.  

    What is the **correct and simplest way** to move the file using your mouse in VS Code?  

    A) Right-click on `hello.py` in the Explorer, select "Cut", then right-click inside the `scripts` folder and select "Paste"  

    B) Click and drag `hello.py` from the Explorer and drop it directly onto the `scripts` folder  

    C) Double-click `hello.py` to open it, then drag the tab at the top of the editor into the `scripts` folder  

    D) Select `hello.py`, press Ctrl+C to copy, then open the `scripts` folder and press Ctrl+V to paste  

    E) Close VS Code, move the file using File Explorer/Finder on your computer, then reopen VS Code

## Free-Response Questions

For free-response questions, please provide your answers in complete, clear sentences. Explain your reasoning fully and thoughtfully. One- or two-word answers will not receive full credit. While grammar and spelling will not be graded, you are encouraged to write neatly and proofread your responses for clarity.

You are allowed (and encouraged) to use your computer and open IDLE to verify or explore the steps as you answer the questions in this section.

1. In your answer, begin by stating which operating system you are using (Windows, macOS, or Linux).  

   Then, assuming you have already opened IDLE on your computer, describe in complete sentences the exact steps you would take to configure IDLE so that line numbers are displayed in the editor window whenever you open or create a new script. Be specific about the menus, tabs, and options you select.

2. Explain, in complete sentences, why it is important to carefully check the number of downloads, the number (and content) of reviews, and the publisher when choosing a VS Code extension to install.  

   In your answer, describe what each of these factors tells you about the extension and how paying attention to them helps protect your computer and improve your programming experience.

3. Describe, in complete sentences, the step-by-step process to save a Python script you have written in the IDLE editor window and then run it.  

   In your answer, explain each step clearly, including the specific menu options or keyboard shortcuts you would use, and what happens after each step. Assume you already have your code typed in an open editor window in IDLE.

4. Describe, in complete sentences, the step-by-step process to create a new Python file (with a .py extension) inside a project folder that is already open in VS Code.  

   In your answer, explain each step clearly, including where you click and what you type. Assume the project folder is already visible in the Explorer sidebar on the left side of VS Code.

5. This question requires you to do some independent research online, as we have not yet discussed the `input()` function in class. You are allowed to use search engines, Python documentation, or other reliable online resources to learn about it.  

   First, in complete sentences, explain what the `input()` function in Python does, including how it works, what it returns, and an example of how to use it with a prompt message.  

   Then, write a brief Python script that:  
   - Uses the `input()` function to ask the user for their name (with a clear prompt like "Enter your name: ").  
   - Stores the user's input in a variable.  
   - Prints a greeting in the format: "Hello, [name]" (where [name] is the input provided by the user).  

   Finally, describe in complete sentences what happens when you run this script, step by step, assuming a user enters "Alex" as their name.

## Programming Questions

You may use any Python development environment (such as VS Code, IDLE, PyCharm, or an online editor like Replit) to write, test, and debug your code before submitting your final solution. Make sure your code runs correctly in standard Python 3. Testing your code thoroughly before submission is highly recommended.

1. In a right triangle, the hypotenuse is the longest side and is opposite the right angle. The Pythagorean theorem states that for any right triangle with legs *a* and *b* and hypotenuse *c*:  

   c = √(a² + b²)  

   Written example (no code):  
   If one leg is 3 inches and the other leg is 4 inches, the hypotenuse is √(3² + 4²) = √(9 + 16) = √25 = 5 inches.  

   Write a complete Python program that calculates the hypotenuse of a right triangle with legs of 5 inches and 8 inches.  

   Your program must:  
   - Use the `from math import sqrt` statement to make the square root function available.  
   - Perform the calculation using the Pythagorean theorem.  
   - Print the result in **exactly** this format (including the period at the end):  

   ```
   The hypotenuse of a triangle with legs of 5 and 8 inches is: [answer].
   ```

   where `[answer]` is the floating-point value returned by the `sqrt` function (do not round it).

2. Write a complete Python script that produces the following **exact** output (a perfectly centered diamond made of `#` characters):  

   ```
      #
     ###
    #####
   #######
    #####
     ###
      #
   ```

   Notice that:  
   - The diamond has exactly 7 lines.  
   - The top and bottom lines have one `#` centered with 3 spaces on each side.  
   - Each line above and below the center increases/decreases the number of `#` by 2.  
   - The center line has 7 `#` characters with no leading spaces.  
   - All lines must end with a newline (standard `print()` behavior is fine).  

   Your script must:  
   - Use only the basic Python concepts you have learned so far (`print()`, the `end` parameter, string multiplication with `*`, spaces `" "`, and the `#` character).  
   - Not use loops (`for` or `while`), lists, or any other advanced topics.  

   You are encouraged to test your code thoroughly in VS Code or IDLE before submitting.

3. Write a complete Python script that introduces yourself using variables. The script must:  

   - Create a variable `name` with your full name as a string (e.g., "John Smith").  
   - Create a variable `age` with your age as an integer (e.g., 17).  
   - Print **exactly** two lines of output in this format:  
   ```
   Hello Everyone! My name is John Smith.
   I am 17 years old.
   ```  

   Requirements:  
   - Use string concatenation with the `+` operator (not commas).  
   - Use the `str()` function to properly convert the age integer for concatenation.  
   - Do not hard-code the name or age directly in the `print()` statements.  

   Test your script to ensure there are no extra spaces and the output matches exactly (including the period at the end of each line).

4. Write a complete Python script that produces the following **exact** output (a simple bordered label):  

   ```
   **************************
   *                        *
   *   Welcome to Python!   *
   *                        *
   **************************
   ```

   Your script must:  
   - Use `print()` statements with the `end` parameter and/or string multiplication (`*`) to build the borders and spacing.  
   - Use only the concepts you have learned (no loops or advanced features).  
   - Have exactly 5 lines of output with the correct number of `*` and spaces.  

   Test your code to ensure the alignment and spacing are perfect.

5. This question is about organizing your project files in VS Code — there is **no Python code to write**.  

   Follow the instructions below **exactly** to set up a project folder structure in VS Code. You will submit a screenshot (or screen recording) showing that you successfully completed the task.  

   1. Create a new folder on your computer named `test_1`.  
   2. Open this `test_1` folder in VS Code (File → Open Folder).  
   3. Inside `test_1`, create **three subfolders** named exactly:  
      - `multi`  
      - `free_rep`  
      - `prog`  

   4. Inside the `multi` folder, create **20 empty Python files** named:  
      `m1.py`, `m2.py`, `m3.py`, ..., up to `m20.py`  

   5. Inside the `free_rep` folder, create **5 empty Python files** named:  
      `f1.py`, `f2.py`, `f3.py`, `f4.py`, `f5.py`  

   6. Inside the `prog` folder, create **5 empty Python files** named:  
      `p1.py`, `p2.py`, `p3.py`, `p4.py`, `p5.py`  

   Requirements:  
   - All folder and file names must be spelled and numbered **exactly** as shown (lowercase, no extra spaces).  
   - Use VS Code’s Explorer sidebar to create the folders and files (right-click → New Folder / New File).  
   - You may use any method to create multiple files quickly (e.g., copy-paste and rename), as long as the final structure is correct.  

   **What to submit:**  
   - A clear screenshot of your VS Code Explorer sidebar showing the full `test_1` folder structure with all subfolders and all 30 Python files visible (you may need to scroll or expand folders).  