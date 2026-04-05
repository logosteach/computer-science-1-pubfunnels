# Study Guide for Test 2: Introduction to Python Basics

This study guide is designed to help you prepare for Test 2 in your Computer Science class. The test covers foundational Python concepts, including data types, strings, arithmetic operations, errors, and string slicing. It includes multiple-choice questions (20 total), free-response questions (4 total), and one programming problem.

Focus on understanding **why** things work (or don't) in Python, not just memorizing syntax. Practice by running code in IDLE, VS Code, or another editor to verify behaviors. Review your class notes, textbooks, or online Python documentation for basics like data types (`int`, `float`, `str`), operators, and common errors.

The test emphasizes:
- No loops or functions (as per class progress).
- Basic string operations: slicing, stripping, escape characters (`\n`, `\t`).
- Arithmetic: `/`, `//`, `%`, `**`.
- Errors: `SyntaxError`, `TypeError`, `NameError`, `RuntimeError` (e.g., `ValueError`, `IndexError`), and logical errors.

## Section 1: Key Concepts to Review

Organized by topic, with explanations, examples, and tips. Practice similar problems to those on the test.

### 1.1 What is Data?
- **Key Idea**: Data refers to information (facts, statistics) in digital form that can be collected, stored, processed, and analyzed.
- **Why It Matters**: Understand the difference between raw data and processed information. Avoid confusing it with unrelated concepts (e.g., sci-fi characters).
- **Practice**: Define data in your own words. Think: How is data represented in Python (e.g., numbers as `int` or `float`, text as `str`)?

### 1.2 String Literals and Representations
- **Key Idea**: Strings are sequences of characters enclosed in single (`' '`) or double (`" "`) quotes. Valid literals are direct text values, not variables or function calls.
- **Examples**:
  - Valid: `"Hello"`, `'World'`.
  - Invalid: `print("Hello")` (this is a statement, not a literal); `string` (this is a variable name, not a literal).
- **Tips**: Select all valid options in "select all" questions. Practice identifying literals vs. code snippets.
- **Practice**: Write 5 valid string literals and 2 invalid ones. Explain why each is valid/invalid.

### 1.3 Data Types and Conversions
- **Key Idea**: Python has types like `int` (whole numbers), `float` (decimals), `str` (text). Use `type()` to check. Conversions: `int()`, `float()`, `str()`.
  - `input()` always returns a `str`, even for numbers.
  - Statements like `5 / 1` result in `float` (5.0); `5 // 1` is `int` (5); `int(5.3)` is `int` (5).
- **Common Pitfalls**: Trying to convert non-numeric strings to `float` (e.g., `"one"` fails with `ValueError`).
- **Practice**: Predict the type of: `5 / 2`, `"5.0"`, `float("3.14")`. Which strings can be converted to `float`? (e.g., `"3.14"`, `"-4"`, but not `"pi"` or `"3.14a"`).

### 1.4 Arithmetic Operations and Formulas
- **Key Idea**: Operators: `+` (add), `-` (subtract), `*` (multiply), `/` (float divide), `//` (integer divide), `%` (modulo/remainder), `**` (exponent).
  - Perimeter of rectangle: `2 * (length + width)`.
  - Exponent vs. Multiply: `2 ** 3` is 8 (not multiplication; use `*` for that).
- **Examples**:
  - `12 // 8` = 1 (drops decimal).
  - `7 / 12` ≈ 0.583 (float).
  - `7 % 8` = 7 (remainder).
- **Tips**: For remainders, `%` is more efficient than manual subtraction (e.g., instead of `x - d * int(x / d)`, use `x % d`).
- **Practice**: Calculate perimeter for width=10, length=14. Find remainder of 103 % 17. Explain why `speed ** time` might not calculate distance (hint: it's exponent, not multiplication).

### 1.5 Printing and Formatting
- **Key Idea**: Use `print()` for output. f-strings for interpolation: `f"Hello, {name}"`.
  - Decimal precision: `f"{pi:.2f}"` for 2 decimals.
  - Escape characters: `\n` (newline), `\t` (tab) for formatting.
  - String multiplier: `"*" * 5` = "*****" (works with integers only).
- **Common Errors**: Missing `f` prefix in f-strings; incorrect format specifiers (e.g., `:.2f` for floats).
- **Practice**: Print "Line1\n\tLine2" (indented). Format π (3.14159) to 2 decimals. Fix invalid multipliers like `":-) *3"` (missing closing quote).

### 1.6 Variables and Assignment
- **Key Idea**: Assignment: `variable = value` (uses `=`, not symmetric like algebra's equality).
  - Multiple assignment: `x, y = 1, 2`.
  - Reassignment: Old value is overwritten (e.g., `x = 7; x = 5` → x is now 5; 7 is garbage-collected).
- **Tips**: In algebra, `5 = x` solves for x; in Python, it's a `SyntaxError` (can't assign to literal).
- **Practice**: Explain to a beginner why `5 = x` fails. Use terms: assignment operator, symmetric property of equality, reference.

### 1.7 Strings: Immutability, Methods, and Slicing
- **Key Idea**: Strings are immutable (can't change characters: `s[0] = 'A'` → `TypeError`).
  - Methods: `replace(old, new)`, `strip()` (remove whitespace), `lstrip()`, `rstrip()`.
  - Slicing: `string[start:end]` (end exclusive; 0-based index).
- **Examples**:
  - For `"I am the way, the truth, and the life - John 14:6a"`, slice "way" as `[5:8]`? Count indices carefully.
  - Replace: `"Hello, John.".replace("John", "Jimmy")` → "Hello, Jimmy." (includes period if not sliced).
- **Tips**: Slicing doesn't modify original. For negative indices or steps, but test focuses on positive basics.
- **Practice**: Slice "life." from the quote (find a, b for `[a:b]`). Fix code that tries to mutate a string.

### 1.8 Errors and Debugging
- **Key Idea**: Types:
  - `SyntaxError`: Invalid code (e.g., mismatched quotes, wrong assignment).
  - `TypeError`: Wrong type (e.g., arithmetic on str + int, item assignment on str).
  - `NameError`: Undefined variable.
  - `RuntimeError`: Runs but fails (e.g., `ValueError` in conversions, `IndexError` in slicing).
  - Logical Error: Runs but wrong output (e.g., using `**` instead of `*`).
- **Tips**: Test code runs without errors; identify why (e.g., input as str causes TypeError in math).
- **Practice**: Predict error in `2 * "5"` (TypeError). If code works but output wrong, it's logical.

## Section 2: Preparing for Free-Response Questions
- **General Tips**: Answer in complete sentences. Explain reasoning. Use editor to test ideas.
- **Question Types**:
  1. Explain syntax differences (Python vs. Algebra).
  2. Debug operator misuse (e.g., why `**` doesn't multiply).
  3. Suggest better operators (e.g., use `%` for remainder).
  4. Determine slicing indices for specific output.
- **Practice Strategy**: For each, write 2-3 sentences. Test code snippets provided.

## Section 3: Preparing for the Programming Problem
- **Overview**: Extract data from a string like `"Date: 2026-01-19\tTemp: 32.5F\tWind: 15mph\tNotes: Snowy day\n"` using slicing only (no `find()`).
  - Extract: date, temp (float), wind (int), notes.
  - Process: Reverse date (slice year/month/day), convert temp to Celsius, wind groups (// and %), strip notes.
  - Output exact format.
- **Key Skills**: Count indices precisely (e.g., date starts at 6, ends at 16).
- **Tips**:
  - Use `strip()` for units/spaces.
  - Comment slices (e.g., `# Date: log[6:16]`).
  - Test for errors: Wrong slice → `IndexError`; No strip → `ValueError`.
  - Edge Case: If format changes (extra spaces), slices fail logically.
- **Practice**: Hardcode the string. Slice parts manually. Run and debug. Try variations (e.g., different dates).

## Final Tips for the Exam
- Time Management: Multiple-choice ~1 min each; free-response ~5-10 min; programming ~20-30 min.
- Resources: Python docs on strings/operators. No internet during test.
- Mindset: Think like a debugger – predict outputs, identify errors.