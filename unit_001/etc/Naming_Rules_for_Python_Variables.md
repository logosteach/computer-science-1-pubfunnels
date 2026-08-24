# Naming Rules for Python Variables

There are two kinds of rules when you create a variable name.

**Syntax rules** are language rules. If you break them, Python raises a `SyntaxError` and the program will not run.

**Convention rules** are community rules, especially those in PEP 8. If you break them, Python will usually still run the program. Other people (and your future self) will have a harder time reading it. This course follows the conventions below, even when Python would accept a sloppier name.

Work at home or in class the same way: decide whether a name is *legal*, then decide whether it is *a good name for this course*.

## Syntax Rules

Python will reject a name that breaks any of these rules.

1. A name may contain only letters (`a-z`, `A-Z`), digits (`0-9`), and underscores (`_`).

2. A name must begin with a letter or an underscore. It cannot begin with a digit.

3. A name cannot contain spaces.

4. A name cannot contain special characters such as `@`, `#`, `$`, `%`, or a hyphen (`-`).

5. Names are case-sensitive. `myVar`, `myvar`, and `MYVAR` are three different names.

6. A name cannot be a reserved word (keyword). Words such as `if`, `else`, `for`, `while`, `class`, `def`, `import`, `True`, `False`, and `None` already belong to the language.

This course also uses ASCII letters only (`a-z` and `A-Z`). Python 3 can accept some accented or non-English letters in names. Do not use those in this course.

To see the current keyword list in Python, run:

```python
help("keywords")
```

## Convention Rules

Python will often accept these names. This course still treats them as incorrect style.

1. Use `snake_case` for ordinary variables and functions: lowercase words separated by underscores. Write `total_sum`, not `totalSum` or `TotalSum`.

2. Use `UPPER_SNAKE_CASE` for values that should not change, such as `MAX_SCORE` or `USER_NAME`.

3. Keep names short enough to type and long enough to describe what they store. Prefer `first_name` over `fn` or `x1`.

4. Do not use a built-in name such as `print`, `input`, `list`, `str`, `int`, or `len` for your own variables. This is legal, but it hides the built-in and causes confusing errors later.

5. A single leading underscore, as in `_hidden`, is legal. By convention it means “internal.” Do not use that pattern until a lesson asks for it.

6. Do not use the names `l`, `O`, or `I`. They are too easy to confuse with the digits `1` and `0`.

7. Do not invent names that look like Python’s special dunder names (`__init__`, `__name__`). Those belong to the language.

## Legal, Poor Style, and Illegal Names

| Kind | Example | Why |
| --- | --- | --- |
| Legal and conventional | `my_variable` | Letters and underscore; `snake_case` |
| Legal and conventional | `count123` | Digits are allowed after the first character |
| Legal and conventional | `first_name` | Underscore replaces a space |
| Legal constant style | `USER_NAME` | `UPPER_SNAKE_CASE` for a constant |
| Legal but poor style | `totalSum` | Camel case. Course form: `total_sum` |
| Legal but poor style | `print` | Shadows the built-in `print()` |
| Legal but advanced style | `_hidden` | Leading underscore is a later convention |
| Illegal | `123count` | Starts with a digit |
| Illegal | `my-var` | Hyphen is a special character |
| Illegal | `user name` | Spaces are not allowed |
| Illegal | `my@var` | `@` is not allowed |
| Illegal | `for` | Reserved keyword |

## SyntaxError and NameError

A **SyntaxError** means the line broke a language rule. Python stops before that program can run and reports the line number. Illegal names cause a `SyntaxError`. Breaking PEP 8 does *not*.

```python
for = 10
```

```console
SyntaxError: invalid syntax
```

```python
user name = "Ada"
```

```console
SyntaxError: invalid syntax
```

A **NameError** means Python reached a name that has not been created yet. In Python, creating a variable means assigning it a value. A misspelled name, including the wrong capitalization, is also a `NameError`.

```python
score = 100
print(Score)
```

```console
NameError: name 'Score' is not defined
```

A built-in name is different. This line is legal and does **not** raise a `SyntaxError`:

```python
print = 10
```

The trouble shows up later, when you try to use the real `print()` function. That is why shadowing built-ins is a convention rule, not a syntax rule.

For every error, learn two things: the **name of the error** and the **line number** Python reports.

## Vocabulary

**Syntax**
The strict rules that define how code must be written. If you break them, the program will not run.

**Convention**
A recommended practice the community agrees on. The computer does not require it. Readers do.

**Interpreter**
The program that reads and runs Python code. Python uses an interpreter rather than a traditional compiler.

**Case-sensitive**
Uppercase and lowercase letters are treated as different. `total` and `Total` are two names.

**Reserved word / keyword**
A word that already has a meaning in Python, such as `if`, `for`, `while`, and `def`. You may not use it as a variable name.

**Built-in function**
A function Python already provides, such as `print()` or `input()`. You *can* reuse that name. You should not.

**PEP 8**
The official style guide for Python code. It is convention, not syntax.

**snake_case**
The PEP 8 style for variable and function names: `player_score`, `first_name`.

**SyntaxError**
An error that occurs when code breaks a language rule. The program will not run until the line is fixed.

**NameError**
An error that occurs when code uses a name that has not been assigned yet, or that is spelled differently from the name that was assigned.

## First-Lab Checklist

1. Start with a letter or `_`, never a digit.
2. Use only letters, digits, and underscores.
3. Use `snake_case` for ordinary variables.
4. Do not use a keyword.
5. Do not reuse `print`, `input`, or other built-in names.
6. If Python stops, read the error name and the line number.

---

Copyright 2026 LogosTeach - All Rights Reserved
