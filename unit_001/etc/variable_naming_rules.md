# Variable Naming Conventions

There are some rules when you begin to create your own variable names. These rules should be carefully followed. Some of these rules are **syntax** rules that Python will generate an error for if they are not followed. The other rules are rules of **convention**. That is to say, they are rules developed by the community and should be followed, but the Python **interpreter** will not generate any errors if you violate them.

## Variable Naming Rules

1. A Python variable must contain valid characters.
   - Variable names can contain:
     - Letters (a-z, A-Z)
     - Digits (0-9)
     - Underscores (_)
   - Variables cannot contain any special characters like `@`, `#`, `$`, `%`, etc.
2. A variable name must start with a letter (a-z, A-Z) or an underscore (_).
3. A variable name cannot begin with a digit (0-9).
4. Variable names cannot contain spaces (white-space): Example: `first name` (spaces not allowed).
5. Python variables are **case-sensitive**. For example: `myVar`, `myvar`, and `MYVAR` are treated as different variables.
6. You may not use **reserved words** (also called **keywords**) for variable names. Words such as `if`, `else`, `for`, `while`, `class`, `def`, and `import` are reserved for specific uses in the language and may not be used for variable names. In addition, avoid using any **built-in function** names like `print` or `input` in your variable names.
7. Keep variable length concise yet descriptive. Following this rule takes practice, but it is worth it. Concise means “keep it short.” Descriptive means “the variable name should describe what it represents.”

## Valid and Invalid Names

Here is a table showcasing valid and invalid variable name examples for Python.

::: center-table
| **Valid Variable Names** | **Invalid Variable Names** | **Reason for Invalidity** |
|--------------------------|----------------------------|---------------------------|
| `my_variable`            | `123count`                 | Starts with a digit       |
| `_hidden`                | `my-var`                   | Contains a hyphen         |
| `count123`               | `for`                      | Reserved keyword          |
| `totalSum`               | `my@var`                   | Contains special character `@` |
| `USER_NAME`              | `user name`                | No spaces allowed in names |
:::

This table summarizes the examples, with valid names adhering to Python's naming rules and invalid names violating them, along with the specific reason for invalidity.

## Syntax and Name Errors

When a variable is not named correctly according to the rules defined in [**PEP 8**](https://peps.python.org/pep-0008/), Python will generate what is known as a **SyntaxError**. A SyntaxError is the type of error you get when you violate the rules of the language. The code will not run, and the Python interpreter will catch the error and display the error message for you. It will also tell you on which line the error occurred.

When a programmer tries to use a variable that has not been defined, the Python interpreter will display a **NameError**. A NameError means that the variable being used has not been declared or given a value. It does not yet exist in the program’s memory. A helpful feature is that the error message will tell you the line number where the error occurred.

The moral of the story is this: for any error you receive, know the name of the error and know the line number where the error occurs.

---

::: vocabulary

### Vocabulary

**Syntax**  
The set of strict rules that define how code must be written in a programming language. If you break these rules, the program will not run.

**Convention**  
A recommended practice that the programming community agrees on. Following conventions makes your code easier for other people (and your future self) to read and understand, even though the computer does not require them.

**Interpreter**  
The program that reads and runs your Python code line by line. Python uses an interpreter rather than a traditional compiler.

**Case-sensitive**  
Uppercase and lowercase letters are treated as completely different. For example, `total` and `Total` are two different variable names.

**Reserved words / Keywords**  
Special words that already have a meaning in Python (such as `if`, `for`, `while`, and `def`). You are not allowed to use them as variable names.

**Built-in function**  
A function that Python already provides for you (such as `print()` or `input()`). It is best not to use these names for your own variables.

**PEP 8**  
The official style guide for writing Python code. It contains the community’s recommended conventions for things like variable naming.

**SyntaxError**  
An error that occurs when your code breaks one of Python’s language rules. The program will not run until the problem is fixed.

**NameError**  
An error that occurs when you try to use a variable that has not yet been created (defined) in your program.

:::
