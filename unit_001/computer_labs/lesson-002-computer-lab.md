# Python Shell Basics: Your First Steps in Interactive Coding

## Lesson 2 - Computer Lab

Welcome to the **Python Shell** (also called the **REPL** — Read-Eval-Print Loop)!  
This is where you can type Python code **one line at a time** and see results instantly.

## What Version of Python Do You Have?

When you open the Python Shell, the **first line** tells you your exact version:

```
Python 3.X.X (main, Oct  1 2024, 00:00:00) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>>
```

> **"3.X.X"** means **whatever version of Python 3 is currently installed on your computer** — for example:
> - `3.11.6`
> - `3.12.3`
> - `3.13.0`

**You can also check your version anytime** by typing this in the shell:

```python
>>> import sys
>>> print(sys.version)
```

Or just:

```python
>>> import sys; print(sys.version.split()[0])
```

This will show something like: `3.12.6`

::: page-break :::

## Step 1: Open the Python Shell

### On Windows 10/11:
1. Press **Start** → type `IDLE`  
2. Click **IDLE (Python 3.x)**  
→ The **Python Shell** window opens!

### On macOS:
1. Press **Cmd + Space** → type `IDLE`  
2. Press **Enter** when **IDLE.app** appears

### On Linux (Debian/Ubuntu):
1. Open **Terminal**  
2. Type: `idle3` → press **Enter**

---

## What Does `>>>` Mean?

The three chevrons `>>>` are the **Python prompt**.  
It means:  
> **“Python is ready! Type your code here and press Enter.”**

After you press **Enter**, Python runs your code and shows the result.

---

## Try It: Basic Math

Type each line in the shell and press **Enter**:

```python
>>> 5 + 3
8
>>> 10 - 4
6
>>> 6 * 7
42
>>> 20 / 5
4.0
>>> 2 ** 3
8
```

> `**` means **exponentiation** (2 to the power of 3 = 8)

---

## Challenge Problems (Try These!)

| # | Problem | Type This |
|---|--------|-----------|
| 1 | What is 15 + 27? | `15 + 27` |
| 2 | What is 100 - 37? | `100 - 37` |
| 3 | What is 8 × 9? | `8 * 9` |
| 4 | What is 56 ÷ 7? | `56 / 7` |
| 5 | What is 2¹⁰ (2 to the power of 10)? | `2 ** 10` |
| 6 | What is 3³ + 4²? | `3**3 + 4**2` |

---

## Store Information in a Variable

A **variable** is like a labeled box that holds data.

```python
>>> age = 14
>>> name = "Alex"
>>> height = 5.5
```

Now use them:

```python
>>> age + 1
15
>>> name + " is learning Python!"
'Alex is learning Python!'
>>> height * 12
66.0
```

---

## Print Results with `print()`

Use `print()` to show messages clearly:

```python
>>> score = 95
>>> print("Great job! Your score is:", score)
Great job! Your score is: 95
```

::: page-break :::

## Mini Project: Create a Simple Calculator

Type this step by step:

```python
>>> num1 = 12
>>> num2 = 8
>>> sum = num1 + num2
>>> product = num1 * num2
>>> print("Sum:", sum)
Sum: 20
>>> print("Product:", product)
Product: 96
```

---

## Final Challenge: Your Turn!

1. Create variables: `apples = 5`, `oranges = 3`
2. Calculate total fruit: `total = apples + oranges`
3. Print: `"I have X fruits in total!"` (replace X with the number)

**Type your solution below:**

```python
>>> apples = 5
>>> oranges = 3
>>> total = apples + oranges
>>> print("I have", total, "fruits in total!")
```

**You did it!** You’re now coding in the Python Shell like a pro!
