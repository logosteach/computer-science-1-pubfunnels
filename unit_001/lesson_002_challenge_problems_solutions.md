# Unit 001 - Lesson 002

## Answer Key: Python Shell Challenge Problems

> **Note**: This key provides **complete, working code** to type line-by-line into the Python Shell (`>>>`).  
> Results shown are **exact expected outputs** (yours may vary slightly by Python version).

---

## Challenge 1: Version Check and Display

```python
>>> import sys
>>> print(sys.version)
3.12.6 (main, Oct 15 2024, 00:00:00) [GCC 13.2.0]
>>> python_version = sys.version.split()[0]
>>> print("My Python version is", python_version)
My Python version is 3.12.6
```

---

## Challenge 2: Advanced Arithmetic Expressions

```python
>>> part1 = (5**2 + 3**3)
>>> part2 = part1 / 4
>>> final = part2 - 10
>>> print("Final result:", final)
Final result: 6.25
```

---

## Challenge 3: String and Number Combinations

```python
>>> name = "Jordan"
>>> age = 16
>>> favorite = 7
>>> doubled = favorite * 2
>>> print(name, "is", age, "years old and their favorite number is", favorite)
Jordan is 16 years old and their favorite number is 7
>>> print("Doubled favorite:", doubled)
Doubled favorite: 14
```

> **Tip**: Use commas in `print()` to avoid `str()` conversion — Python adds spaces automatically.

---

## Challenge 4: Unit Conversion Calculator

```python
>>> inches = 72
>>> feet = inches / 12
>>> yards = inches / 36
>>> print(inches, "inches is", feet, "feet or", yards, "yards.")
72 inches is 6.0 feet or 2.0 yards.
```

---

## Challenge 5: Personal Budget Tracker

```python
>>> allowance = 50
>>> snacks = 12
>>> games = 18
>>> total_expenses = snacks + games
>>> remaining = allowance - total_expenses
>>> savings = remaining * 0.10
>>> print("Allowance:", allowance)
Allowance: 50
>>> print("Expenses:", total_expenses)
Expenses: 30
>>> print("Remaining:", remaining)
Remaining: 20
>>> print("Savings (10%):", savings)
Savings (10%): 2.0
```

> **Bonus Output (one line):**
```python
>>> print(f"Budget: ${allowance} allowance → ${total_expenses} spent → ${remaining} left → save ${savings}")
Budget: $50 allowance → $30 spent → $20 left → save $2.0
```

---

**All challenges complete!**  
You’ve mastered the Python Shell basics.  
Next step: Save your code into a `.py` file and run scripts!
