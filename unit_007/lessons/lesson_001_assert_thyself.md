# Lesson 1 - Assert Thyself

## Introduction

Assertions give the developer a way to debug and test their code. In this lesson, we are going to learn what an assertion is, what they are good for and when you should not use them. Assertions are very useful for the _development_ phase of your project, but should be disabled when your project goes into _production_.

## Reading

> **Python with a Worldview <sup>2nd</sup> Edition**
> Chapter 7 - Putting Your Code To The Test
> Lesson 1 - Assert Thyself

## Reading Questions

> **_Helpful tip before you start reading:_**
> 
> These questions are closely connected to the key ideas in the text. To make your reading more active and purposeful, try creating a quick checklist of these questions. As you come across the answers while reading, check them off. This will help you stay focused and get more out of the material!

1. What is the definition of an assertion statement?
2. What type of error does an assertion statement throw?
3. How is the `assert` keyword used when the programmer want to develop their own custom error message?
4. What are the advantages to using assertion statements?
5. When should a programmer not use assertion statements?
6. What are the three basic types of assertion statements covered in this lesson?
7. Can you explain, in your own words, what is meant by _using assertion statements as documentation items?_

## Warm Up Session

Open the Python shell in your computer and type in the following statements.

#### Part 1

```python
x = 5
y = 3.4
z = "5.4"

assert isinstance(x, int)
assert isinstance(y,float)
assert isinstance(z ,float)
```

What happened? Can you explain why?

#### Part 2

```python
# Is it possible to check two things at once?
x = 5
y = 3.4
z = x + y
assert isinstance(z, (int, float))
```

Does this work? Change x to a floating point number and then check the code again. Next, change both to integers and see if it works.

## Video Examples

***Here is where links for the video sessions for this lesson will go.***

## Computer Lab

Welcome to the Python computer labs!  

Computer Labs are added in the **Attached Files** section on this page.

These labs are provided as **Markdown (.md) files**. Markdown is a simple formatting language that makes instructions, code examples, and questions easy to read. VS Code has excellent built-in support for Markdown, so you can view the nicely formatted version (with headings, code blocks, lists, etc.) while you work.

### How to Open and Preview a Markdown File in VS Code

1. **Open the lab file**
   - Launch **Visual Studio Code**.
   - Go to **File > Open Folder...** and select the folder containing your lab files (recommended), or simply **File > Open File...** and choose the specific `.md` file.

2. **Preview the Markdown (recommended way to read the lab)**
   Once the `.md` file is open in the editor:

   **On Windows or Linux:**
   - Press `Ctrl + Shift + V` (this opens the preview in a new tab)
   - Or press `Ctrl + K` then `V` (this opens a side-by-side preview — very useful!)

   **On macOS:**
   - Press `Cmd + Shift + V` (opens preview in a new tab)
   - Or press `Cmd + K` then `V` (opens side-by-side preview)

    **Alternative methods (work on all operating systems):**

   - Right-click the file tab at the top and choose **Open Preview** (or **Open Preview to the Side**).
   - Right-click the file in the Explorer sidebar and choose **Open Preview**.
   - Open the Command Palette (`Ctrl + Shift + P` on Windows/Linux or `Cmd + Shift + P` on macOS), type "Markdown: Open Preview", and select it.

The preview updates **live** as you make any changes (though you usually won't need to edit the instructions themselves).

### Working on the Lab

- You can keep the **preview** open on one side and write your Python code in a new `.py` file on the other side.
- Feel free to add notes directly in the Markdown file if it helps you.

You're all set! If you have any questions about using VS Code, just ask.

&copy; 2026 LogosTeach - All Rights Reserved