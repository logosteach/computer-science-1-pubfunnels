# Unit 3 - Test

This section is worth **10 points total**.

**Part A: Multiple Choice & Short Answer**  
**10 points total**

**Question 1** (2 points)  
What is the output of the following Python code?

```python
age = 14
weight = 120

if age >= 13 and weight < 210:
    print("You can ride.")
elif age < 13:
    print("Too young for this ride.")
else:
    print("Sorry, you do not meet the requirements.")
```

A) You can ride.  
B) Too young for this ride.  
C) Sorry, you do not meet the requirements.  
D) No output (the code has a syntax error)

**Question 2** (2 points)  
What is printed when the following Python code runs?

```python
is_employee = True
has_id = False
owner = True

if is_employee and has_id or owner:
    print("Access granted")
else:
    print("Access denied")
```

A) Access granted  
B) Access denied  
C) SyntaxError (invalid logic)  
D) Nothing is printed

**Question 3** (2 points)  
Consider the compound boolean expression: `(A ^ B) and (B ^ C)`

**Part A** (1 point)  
What is the value of the expression when `A = False`, `B = True`, `C = False`?  
A) True  
B) False  
C) SyntaxError (invalid operator for booleans)  
D) The result cannot be determined without more information

**Part B** (1 point)  
Complete the missing value in this partial truth table for the expression `(A ^ B) and (B ^ C)`:

| A     | B     | C     | A ^ B | B ^ C | (A ^ B) and (B ^ C) |
|-------|-------|-------|-------|-------|----------------------|
| True  | False | True  | True  | True  | True                 |
| False | True  | False | True  | True  | ???                  |
| True  | True  | True  | False | False | False                |
| False | False | False | False | False | False                |

What value belongs in the ??? spot? ________________ (True or False)

**Question 4** (1 point)  
What is the output of the following Python code? (Select the correct sequence of boolean values printed)

```python
members = ["Josiah", "Ellen", "Mark", "Martha", "Thomas"]
leaders = ["Josiah", "Martha"]

print("Josiah" in members)
print("Ellen" not in leaders)
print("Martha" in leaders)
print("Thomas" in leaders)
print("Mark" in members)
print("Ellen" not in members)
print("Josiah" in leaders)
```

A) True True True False True True True  
B) True True True False True False True  
C) True False True True False True False  
D) False True False True True False True

**Question 5** (1 point)  
What is the output of the following Python code?

```python
names = ["Jared", "Pippin", "Jay", "Abby", "Ellyn", "Eden"]

print(names[2])
print(names[-1])
print(names[6])
print(names[-3])
print(len(names))
```

A) Jay  
   Eden  
   IndexError  
   Abby  
   6  

B) Jay  
   Eden  
   Eden  
   Abby  
   6  

C) Pippin  
   Ellyn  
   IndexError  
   Ellyn  
   6  

D) Jay  
   Abby  
   IndexError  
   Eden  
   6  

**Question 6** (2 points)  
What is the output of the following print statements? Select the option that shows the correct sequence of sliced lists.

```python
names = ["Jared", "Pippin", "Jay", "Abby", "Ellyn", "Eden"]

print(names[1:4])
print(names[:3])
print(names[::2])
print(names[-4:-1])
print(names[::-1])
```

A)  
['Pippin', 'Jay', 'Abby']  
['Jared', 'Pippin', 'Jay']  
['Jared', 'Jay', 'Ellyn']  
['Jay', 'Abby', 'Ellyn']  
['Eden', 'Ellyn', 'Abby', 'Jay', 'Pippin', 'Jared']  

B)  
['Pippin', 'Jay', 'Abby']  
['Jared', 'Pippin']  
['Jared', 'Jay', 'Ellyn']  
['Abby', 'Ellyn']  
['Jared', 'Pippin', 'Jay', 'Abby', 'Ellyn', 'Eden']  

C)  
['Jay', 'Abby']  
['Jared', 'Pippin', 'Jay']  
['Jared', 'Abby', 'Eden']  
['Jay', 'Abby', 'Ellyn', 'Eden']  
['Eden', 'Ellyn', 'Abby', 'Jay', 'Pippin', 'Jared']  

D)  
['Pippin', 'Jay', 'Abby', 'Ellyn']  
['Jared', 'Pippin', 'Jay']  
['Jared', 'Jay', 'Ellyn']  
['Jay', 'Abby']  
['Eden', 'Ellyn', 'Abby', 'Jay', 'Pippin', 'Jared']

Here is **Part B: Predict the Output / Find the Error** section of the assessment, fully written out with all 7 questions.

This section is worth **28 points total** (4 points each question).

**Part B: Predict the Output / Find the Error**  
**28 points total** (7 questions × 4 points each)

**Question 1** (4 points)  
Consider the following Python code:

```python
score = 85
grade = "unknown"

if score = 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)
```

a) (1 point) What is the actual output when the code runs? (Or describe the error if it does not run.)

b) (2 points) Explain exactly why the code behaves that way (what is the mistake?).

c) (1 point) Rewrite the first line of the `if` statement so the code works correctly (i.e., assigns "A" when score is 90 or higher).

**Question 2** (4 points)  
A simple Python program is written to help someone check their credit score category based on the standard FICO model (ranges from 300 to 850):

```python
score = 720

if score >= 800:
    print("Exceptional")
elif score >= 740:
    print("Very Good")
elif score >= 670:
    print("Good")
elif score >= 580:
    print("Fair")
else:
    print("Poor")
```

a) (2 points) What is printed when `score = 720`?  
   A) Exceptional  
   B) Very Good  
   C) Good  
   D) Fair  
   E) Poor

b) (2 points) Explain in 1–2 sentences why the order of the `elif` statements is important in this code. What would happen if the `elif score >= 670` line was moved to the top?

**Question 3** (4 points)  
Consider the following Python code:

```python
authors = ["Jane Austen", "J.R.R. Tolkien", "C.S. Lewis", "John Owen", "Agatha Christie", "Sinclair Ferguson"]

for index, author in enumerate(authors):
    print(f"{index}: {author}")
```

a) (3 points) What exact output is produced when this code runs?  
   (Select the best matching option)

A)  
0: Jane Austen  
1: J.R.R. Tolkien  
2: C.S. Lewis  
3: John Owen  
4: Agatha Christie  
5: Sinclair Ferguson  

B)  
1: Jane Austen  
2: J.R.R. Tolkien  
3: C.S. Lewis  
4: John Owen  
5: Agatha Christie  
6: Sinclair Ferguson  

C)  
Jane Austen 0  
J.R.R. Tolkien 1  
C.S. Lewis 2  
John Owen 3  
Agatha Christie 4  
Sinclair Ferguson 5  

D) IndexError: list index out of range  
E) The code has a syntax error and does not run.

b) (1 point) Rewrite the loop **without using `enumerate()`** so that it produces the exact same output.

**Question 4** (4 points)  
Consider the following Python code:

```python
frame = 1
game_running = True

while game_running:
    print(f"Frame is now: {frame}")
    
    if frame >= 5:
        game_running = False
    
    frame = frame + 1

print("Loop finished!")
```

What is the **exact output** produced when this code runs?  
(Select the option that shows the complete printed result, including the final message.)

A)  
Frame is now: 1  
Frame is now: 2  
Frame is now: 3  
Frame is now: 4  
Frame is now: 5  
Loop finished!

B)  
Frame is now: 1  
Frame is now: 2  
Frame is now: 3  
Frame is now: 4  
Loop finished!

C)  
Frame is now: 1  
Frame is now: 2  
Frame is now: 3  
Frame is now: 4  
Frame is now: 5  
Frame is now: 6  
Loop finished!

D) The code runs forever (infinite loop) and never prints "Loop finished!"

E) SyntaxError: invalid syntax

**Question 5** (4 points)  
Consider the following Python code:

```python
authors = ["Jane Austen", "J.R.R. Tolkien", "C.S. Lewis", "John Owen", "Agatha Christie", "Sinclair Ferguson"]

for author in authors:
    print(author)
    if author == "C.S. Lewis":
        authors.remove(author)

print("Final list:", authors)
```

a) (2 points) What exact output will this code produce?  
   (Choose the option that matches both the printed names **and** the final list.)

A)  
Jane Austen  
J.R.R. Tolkien  
C.S. Lewis  
John Owen  
Agatha Christie  
Sinclair Ferguson  
Final list: ['Jane Austen', 'J.R.R. Tolkien', 'John Owen', 'Agatha Christie', 'Sinclair Ferguson']

B)  
Jane Austen  
J.R.R. Tolkien  
C.S. Lewis  
Agatha Christie  
Sinclair Ferguson  
Final list: ['Jane Austen', 'J.R.R. Tolkien', 'John Owen', 'Agatha Christie', 'Sinclair Ferguson']

C)  
Jane Austen  
J.R.R. Tolkien  
C.S. Lewis  
John Owen  
Agatha Christie  
Sinclair Ferguson  
Final list: ['Jane Austen', 'J.R.R. Tolkien', 'C.S. Lewis', 'John Owen', 'Agatha Christie', 'Sinclair Ferguson']

D) The code raises an error (IndexError or RuntimeError)

b) (2 points) Explain briefly (2–4 sentences) **why** "John Owen" is missing from the final list even though the code only tried to remove "C.S. Lewis". What happens during loop execution?

**Question 6** (4 points)  
Consider the following Python code:

```python
numbers = [82, 15, 4, 95, 36, 32, 29, 18, 95, 67]

print("Processing numbers:")
for num in numbers:
    if num % 2 == 0:
        continue
    if num > 51:
        print(f"Found large odd number: {num} → stopping")
        break
    print(f"Odd number: {num}")

print("Loop ended")
```

a) (2 points) What is the **exact output** produced by this code?  
   (Select the option that matches the printed lines exactly.)

A)  
Processing numbers:  
Odd number: 15  
Found large odd number: 95 → stopping  
Loop ended

B)  
Processing numbers:  
Odd number: 15  
Odd number: 95  
Odd number: 29  
Odd number: 67  
Loop ended

C)  
Processing numbers:  
Odd number: 15  
Found large odd number: 95 → stopping  
Odd number: 29  
Loop ended

D)  
Processing numbers:  
Odd number: 15  
Odd number: 95  
Odd number: 29  
Odd number: 67  
Loop ended

b) (2 points) Explain briefly (in 2–4 sentences) what `continue` and `break` do in this loop, and why the number **67** is **not** printed even though it is odd.

**Question 7** (4 points)  
Consider the following Python code that demonstrates a common list copying mistake:

```python
# Original list of authors
original_authors = ["Jane Austen", "J.R.R. Tolkien", "C.S. Lewis"]

# "Copy" the list (common beginner mistake)
copied_authors = original_authors

# Modify the "copy"
copied_authors.append("Agatha Christie")
copied_authors[0] = "John Owen"

print("Original list:", original_authors)
print("Copied list:", copied_authors)
```

a) (2 points) What is the **exact output** produced by this code?  
   (Select the option that matches both printed lists exactly.)

A)  
Original list: ['Jane Austen', 'J.R.R. Tolkien', 'C.S. Lewis']  
Copied list: ['John Owen', 'J.R.R. Tolkien', 'C.S. Lewis', 'Agatha Christie']

B)  
Original list: ['John Owen', 'J.R.R. Tolkien', 'C.S. Lewis', 'Agatha Christie']  
Copied list: ['John Owen', 'J.R.R. Tolkien', 'C.S. Lewis', 'Agatha Christie']

C)  
Original list: ['Jane Austen', 'J.R.R. Tolkien', 'C.S. Lewis']  
Copied list: ['John Owen', 'J.R.R. Tolkien', 'C.S. Lewis', 'Agatha Christie']

D)  
Original list: []  
Copied list: ['John Owen', 'J.R.R. Tolkien', 'C.S. Lewis', 'Agatha Christie']

b) (2 points) Explain briefly (2–4 sentences) **why** both lists end up identical and modified, even though only `copied_authors` was changed. How would you fix this to create a **true independent copy** of the original list?

Here is **Part C: Short Coding Tasks** section of the assessment, fully written out with all 6 questions.

This section is worth **38 points total** (re-balanced distribution).

**Part C: Short Coding Tasks**  
**38 points total**

**Question 1** (6 points)  
**Task: Ride Eligibility Checker**

Write a small program that asks the user for two inputs:

- Their **age** (integer)  
- Their **weight** in pounds (integer)  

Then use conditionals to print **exactly one** of the following messages:

- "You can ride."                  if age >= 13 **and** weight < 210  
- "Too young for this ride."       if age < 13  
- "Sorry, weight limit exceeded."  if weight >= 210 (and age >= 13)  

Assume the user always enters valid integers (no need for input validation or try/except).

**Example runs:**

```
Enter your age: 14
Enter your weight in pounds: 120
You can ride.
```

```
Enter your age: 12
Enter your weight in pounds: 150
Too young for this ride.
```

```
Enter your age: 16
Enter your weight in pounds: 215
Sorry, weight limit exceeded.
```

Write your complete code below.

**Question 2** (6 points)  
**Task: Demonstrate the difference between reference assignment and true copying of a list**

Write a short Python program that does the following steps **exactly**:

1. Create a list called `books` with these four strings:  
   `"The Hobbit"`, `"Mere Christianity"`, `"Pride and Prejudice"`, `"The Lion, the Witch and the Wardrobe"`

2. Create **two** new variables:  
   - `reference_copy = books`  (using simple assignment)  
   - `true_copy = books.copy()`  (using the correct method to make an independent copy)

3. Modify **only the `true_copy` list** by doing these two changes:  
   - Change the first book to `"The Silmarillion"`  
   - Add `"The Screwtape Letters"` to the end of the list

4. Finally, print **all three lists** with clear labels, for example:  
   ```
   Original books list: ['The Hobbit', 'Mere Christianity', 'Pride and Prejudice', 'The Lion, the Witch and the Wardrobe']
   Reference copy: ['The Silmarillion', 'Mere Christianity', 'Pride and Prejudice', 'The Lion, the Witch and the Wardrobe', 'The Screwtape Letters']
   True independent copy: ['The Silmarillion', 'Mere Christianity', 'Pride and Prejudice', 'The Lion, the Witch and the Wardrobe', 'The Screwtape Letters']
   ```

Your output must clearly show that:  
- the **original** `books` list **and** the `reference_copy` are identical and both changed  
- the `true_copy` reflects the modifications you made, while the original remains unaffected

Write your complete code below.

**Question 3** (7 points)  
**Task: Filter and print authors containing a specific letter or substring**

Use the following list of authors:

```python
authors = ["Jane Austen", "J.R.R. Tolkien", "C.S. Lewis", "John Owen", "Agatha Christie", "Sinclair Ferguson"]
```

Write a program that does the following:

1. Ask the user to enter **a single letter or short substring** to search for.  
   Prompt:  
   `Enter a letter or substring to search for in author names: `

2. Use a **for loop** to iterate over the `authors` list.

3. For each author name, check if the user's entered text appears **anywhere** in the name (case-insensitive — so "j" should match "Jane" and "J.R.R.").

4. If the name contains the searched text, **print** that author's name (one per line).

5. After checking all authors, print a final summary line in this exact format:  
   `Found X author(s) containing "[search_term]".`  
   (Replace X with the actual number of matches and [search_term] with exactly what the user typed)

**Example run (input: j)**  
```
Enter a letter or substring to search for in author names: j
Jane Austen
J.R.R. Tolkien
John Owen
Found 3 author(s) containing "j".
```

Write your complete code below.

**Question 4** (7 points)  
**Task: Process a list of scores, skip negatives, stop on invalid high scores**

Use the following list:

```python
scores = [45, 82, 19, 100, 67, -5, 88, 33, 91, 72, 0, 55]
```

Write a program that:

1. Initializes two variables:  
   - `total = 0` (running sum of valid scores)  
   - `count = 0` (number of valid scores processed)

2. Uses a **for loop** to iterate over each number in `scores`.

3. For each number, apply these rules **in this order**:
   - If the number is **negative** → use `continue` to skip it (do not add or count it)  
   - If the number is **greater than 100** → print  
     `"Invalid score found: {number} → stopping processing"`  
     and use `break` to exit the loop immediately  
   - Otherwise (valid score: 0 to 100 inclusive) → add it to `total` and increment `count`

4. After the loop ends (either normally or by `break`), print:  
   ```
   Processed {count} valid scores.
   ```
   Then, **if** `count > 0`, also print:  
   ```
   Average score: {average:.1f}
   ```
   (where average = total / count, formatted to 1 decimal place)  
   If `count == 0`, print instead:  
   ```
   No valid scores were found.
   ```

Write your complete code below.

**Question 5** (6 points)  
**Task: Use sets to remove duplicates, check membership, and perform basic set operations**

You are given two lists of book titles that students have read:

```python
group_a = ["The Hobbit", "Mere Christianity", "Pride and Prejudice", "The Lion, the Witch and the Wardrobe", "The Hobbit", "Mere Christianity"]
group_b = ["The Screwtape Letters", "Mere Christianity", "The Lion, the Witch and the Wardrobe", "Orthodoxy", "The Hobbit"]
```

Write a program that performs the following steps **in exact order**:

1. Convert both lists to **sets** (to remove duplicates) and store them as:  
   - `set_a`  
   - `set_b`

2. Print the unique books for each group, sorted alphabetically:  
   ```
   Unique books read by Group A: {sorted list of set_a}
   Unique books read by Group B: {sorted list of set_b}
   ```

3. Check membership (using `in`) and print whether each of these books was read by **at least one person** in either group:  
   - "The Hobbit"  
   - "Orthodoxy"  
   - "The Great Divorce"  

   Example format:  
   `"The Hobbit" was read by someone: True`

4. Compute and print (sorted):  
   - The **intersection** (books read by **both** groups):  
     `Books read by both groups: {sorted list}`  
   - The **union** (all unique books read by either group):  
     `All unique books read: {sorted list}`

Write your complete code below.

**Question 6** (6 points)  
**Task: Demonstrate tuple immutability and unpacking**

Write a short Python program that shows why tuples cannot be changed after creation and how tuple unpacking works.

Follow these exact steps in your code:

1. Create a tuple named `disciples` containing these six strings (in this order):  
   `"Peter"`, `"Andrew"`, `"James"`, `"John"`, `"Philip"`, `"Thomas"`

2. Print the original tuple with this label:  
   ```
   Original tuple: {disciples}
   ```

3. **Write the following line** in your code (but do NOT run it — include it only as a comment):  
   ```python
   # disciples[2] = "James the Greater"   # This line is NOT allowed!
   ```
   Then, immediately below it, add this comment explaining why:  
   ```python
   # Tuples are immutable — you cannot change, add, or remove items after creation.
   # If you try to run the line above, Python will give a TypeError.
   ```

4. Create a **new tuple** called `updated_disciples` that contains the same values as the original tuple **except** the third name is now `"James the Greater"`.  
   (Hint: You can do this by slicing the original tuple and combining parts with a new value using `+` — for example, `disciples[:2] + ("James the Greater",) + disciples[3:]`)

5. Print the new tuple:  
   ```
   Updated tuple (a completely new tuple): {updated_disciples}
   ```

6. Demonstrate **tuple unpacking** by unpacking the **original** `disciples` tuple into six separate variables:  
   ```python
   first, second, third, fourth, fifth, sixth = disciples
   ```

7. Print this sentence using the unpacked variables:  
   ```
   The first two disciples are {first} and {second}. The last one is {sixth}.
   ```

Write your complete code below.

Here is **Part D: Binary, Bits, Bytes, and Data Sizes** — fully written out.

This section is worth **14 points total**.

**Part D: Binary, Bits, Bytes, and Data Sizes**  
**14 points total**

**Question D1** (2 points)  
Which of the following is the correct number of **bits** in one **byte**?

A) 4  
B) 8  
C) 16  
D) 1024

**Question D2** (2 points)  
How many **bytes** are in 1 **kilobyte** (using the common computer storage definition — the one used in programming and memory contexts)?

A) 8  
B) 256  
C) 1000  
D) 1024

**Question D3** (3 points)  
Complete the table by filling in the missing values. Show your work (calculations) for partial credit.

| Size in bytes          | Size in kilobytes (KiB) | Size in megabytes (MiB) |
|------------------------|---------------------------|---------------------------|
| 4,096                  | ?                         | ?                         |
| ?                      | 512                       | ?                         |
| ?                      | ?                         | 3                         |

**Question D4** (2 points)  
True or False:  
1 kilobyte is exactly 1,000 bytes.

Explain your answer in 1–2 sentences.

**Question D5** (3 points)  
A small Python program uses approximately 2.5 megabytes of memory.

a) Convert 2.5 MiB to **kilobytes**. Show your calculation. (1.5 points)  
b) Convert 2.5 MiB to **bytes**. Show your calculation. (1.5 points)

**Question D6** (2 points)  
In binary (base-2), each **bit** can be either 0 or 1.  
Because there are 8 bits in a byte, one byte can represent 2⁸ = **___** different possible values (from 00000000 to 11111111).

Fill in the blank: ________________

Here is **Part E: Coding for Others – Mini Project**, fully written out as the final section of the assessment.

This section is worth **10 points** (as re-balanced).

**Part E: Coding for Others – Mini Project**  
**10 points**

**Task: To-Read List Helper Tool**

You have a friend who loves reading but often adds the same book multiple times or needs to remove books they've decided against or already read. Write a small Python program to help them manage their to-read list. The program should:

- Start with an empty list called `my_to_read_list` to store all entered book titles (which may include duplicates during input).
- Use a main loop to repeatedly show a menu with these options:
  - `a` = add book(s)
  - `r` = remove book(s)
  - `q` = quit and show final list
- For **adding**:
  - Prompt the user to enter book titles one by one.
  - They can enter as many as they want; when done with the batch, they press Enter on an empty line to stop adding for now.
  - Append each non-empty title to `my_to_read_list`.
- For **removing**:
  - Show the current unique books as a numbered list (sorted alphabetically, using `sorted(set(my_to_read_list))`).
  - If the list is empty, print a message like "Your list is empty — nothing to remove." and continue.
  - Ask the user to enter number(s) to remove (e.g., "1 3" or "2").
  - Remove all occurrences of the selected titles from `my_to_read_list`.
  - Ignore invalid numbers or non-numeric input (print a warning but continue).
  - If the user presses Enter without typing anything, cancel the removal.
- After every add or remove action (and before asking the menu again), optionally show the current unique sorted list (this helps the user see changes).
- When the user chooses `q`:
  - Print the final unique sorted list with numbers and the total count.
  - End the program with a goodbye message.

**Hints:**
- Use a `while` loop with a flag like `finished = False` for the main menu.
- For adding: Use a nested `while True` loop; break when `input()` is empty after `.strip()`.
- For removing: Use `sorted(set(...))` to display, but remove from the original list.
- Handle invalid menu choices by reprompting.
- No need for case-insensitivity unless you want bonus points.
- Keep code clean and readable (good indentation, comments optional but helpful).

**Starter Code Scaffold** (copy this and complete it):

```python
# To-Read List Helper Tool

print("Welcome to your To-Read List Helper!")
print("Add books, remove if needed, and see a clean list without duplicates.\n")

my_to_read_list = []  # start with empty list

finished = False

while not finished:
    # TODO: Print menu options: a=add, r=remove, q=quit
    # TODO: Get user choice (strip and lower) and handle invalid input
    
    if choice == 'a':
        print("\nEnter book titles (one per line). Press Enter on empty line to stop.")
        while True:
            book = input("Book title: ").strip()
            # TODO: Break if empty; else append to my_to_read_list
    
    elif choice == 'r':
        # TODO: Get unique sorted list
        # TODO: If empty, print message and continue
        # TODO: Print numbered unique list
        # TODO: Get numbers to remove (split input, convert to int, validate range)
        # TODO: Remove selected titles from my_to_read_list
    
    elif choice == 'q':
        # TODO: Set finished = True
    
    # TODO: After add or remove, optionally show current unique list here

# Final output
print("\n" + "="*60)
print("Final unique to-read list (duplicates removed):")
unique_final = sorted(set(my_to_read_list))
if unique_final:
    for i, title in enumerate(unique_final, 1):
        print(f"{i}. {title}")
    print(f"\nTotal unique books: {len(unique_final)}")
else:
    print("No books were added.")
print("="*60)
print("Goodbye!")
```

**Grading rubric**  
- Main menu loop & choice handling (including invalid input) – 3 pts  
- Adding books correctly (handles multiple, stops on empty line) – 2 pts  
- Removing books (shows numbered list, gets/validates numbers, removes correctly) – 3 pts  
- Displays unique sorted lists after actions and in final output – 1 pt  
- Edge cases (empty list, no removal, invalid numbers) & clean code – 1 pt  

Write your complete code below.

**End of Assessment**  
**Total: 100 points**

&copy; LogosTeach 2026 - All Rights Reserved