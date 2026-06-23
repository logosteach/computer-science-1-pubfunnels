# Unit 004B Assessment

**Student Name:** _______________________________  
**Date:** _______________________________  
**Unit:** 4B  
**Total Points Possible:** ______

### Instructions
Review all learning objectives from the lessons in this unit before beginning.  
You may use your IDE to write and test your code. Please minimize the use of AI tools during this assessment — the goal is to develop independent thinking, creativity, and problem-solving skills. Write all code as clearly and cleanly as possible, and test your solutions thoroughly before submitting.

---

## Section 1: Knowledge & Understanding

**1.** David has 150 campers coming to camp this summer... What problem solving strategy best represents the process that David is about to do? (__ points)

- A) Writing one giant block of code that manually checks every single camper’s file without any repetition.
- B) Using a loop to repeat the process of reviewing medical information for each camper.
- C) Asking each camper to email their own information directly to the nurse so he doesn’t have to do anything.
- D) Praying really hard that all the medical forms magically sort themselves.
- E) Hiring 150 trained squirrels to sort the paperwork while he takes a nap.

**Your Answer:** 

**2.** Which answer BEST describes the given loop? (__ points)

```python
for i in range(0, 15):
    print(i)
```

- a) The result will be 0 through 15.
- b) The result will be 0 through 14.
- c) IndentationError
- d) The result will be i=0, i=1, ... i=15.
- e) The letter 'i' is not in the word range.

**Your Answer:** 

**3.** What is the output of the following code? (__ points)

```python
count = 1
while count != 5:
    print(count)
    count += 2
```

- a) 1 2 3 4 5
- b) 1 3
- c) 1 3 5
- d) 1 2 3 4
- e) The program will run forever (infinite loop)

**Your Answer:** 

**4.** Janice has a Python list named `books` ... Which is the correct implementation of this? (__ points)

a) 
```python
for i in range(len(books)):
    print(i+1, books[i])
```

b) 
```python
i = 0
while i < len(books):
    print(i+1, books[i])
    i += 1
```

c) 
```python
for book in books:
    print(book)
```

<div style="page-break-before: always;"></div>

d) 
```python
i = 0
while i <= len(books):
    print(i+1, books[i])
    i += 1
```

e) 
```python
while True:
    print(books)
```

**Your Answer:** 

**5.** Daniel wants to print out the first 5 odd numbers beginning with 3... Will this code achieve what Daniel wants...? (__ points)

```python
for i in range(3, 5, 2):
    print(i)
```

- a) The code is correct and will print 3, 5, 7, 9, 11.
- b) The code needs a different `stop` value (e.g. `range(3, 12, 2)`).
- c) The code needs a different `step` value.
- d) The code has a capitalization error with the variable `I` vs `i`.
- e) The code is correct but needs `print(i, end=" ")` to print on one line.

**Your Answer:** 

**6.** Samantha is given a bag full of money... What type of loop would best be used...? (__ points)

- a) A `for` loop, because she knows exactly how much money is in the bag.
- b) A `while` loop, because she doesn’t know how many bills or coins there are until she counts them all.
- c) A `for` loop with `range(100)` because there are usually around 100 items.
- d) Neither — she should just use `print("Count the money")` once.
- e) A nested loop because there are bills and coins.

**Your Answer:** 

**7.** Dallas has the following string variable... Which of the following loops will print each word exactly once...? (__ points)

- a) `for word in message: print(word)`
- b) `for word in message.split(): print(word)`
- c) `for i in range(len(message)): print(message[i])`
- d) `while message: print(message); message = ""`
- e) `for letter in message: print(letter)`

**Your Answer:** 

**8.** What will happen when the following code is run? (__ points)

```python
counter = 0
while True:
    print("Game is running...")
    counter += 1
    if counter > 1000:
        break
```

- a) The message "Game is running..." will print exactly 1000 times and then stop.
- b) The message "Game is running..." will print forever (infinite loop).
- c) The message "Game is running..." will print 1001 times and then stop.
- d) The code will cause an error because `break` is not allowed in a `while` loop.
- e) The message will print once and then stop.

**Your Answer:** 

<div style="page-break-before: always;"></div>

**9.** What is the output of the following code? (__ points)

```python
prayer_requests = ["Heal my mom", "", "Help with school", " ", "Strength for my dad", ""]
for request in prayer_requests:
    request = request.strip()
    if request == "":
        continue
    print("Praying for:", request)
```

- a) It prints all 6 items including the empty ones.
- b) It prints only the non-empty prayer requests.
- c) It prints nothing because of the `continue` statement.
- d) It causes an error because `continue` cannot be used with a list.
- e) It prints the empty strings as blank lines.

**Your Answer:** 

**10.** What does the `break` statement do inside a loop? (__ points)

- a) Skips the rest of the current iteration and goes to the next one
- b) Immediately exits the entire loop
- c) Restarts the loop from the beginning
- d) Does nothing

**Your Answer:** 

**11.** Which of the following is the best real-world use case for using `break` in a loop? (__ points)

- a) Printing every other number in a sequence
- b) Searching through a list until you find a specific item, then stopping early
- c) Skipping over invalid input values but continuing to process the rest
- d) Repeating a block of code a fixed number of times

**Your Answer:** 

**12.** What is the primary purpose of the `continue` statement in a loop? (__ points)

- a) To immediately exit the loop entirely
- b) To skip the rest of the current iteration and proceed to the next iteration
- c) To restart the loop from the first value
- d) To pause the program and wait for user input

**Your Answer:** 

**13.** What will the following code print? (__ points)

```python
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
```

- a) 1 2 3 4 5 6 7 8 9 10
- b) 1 2 4 5 7 8 10
- c) 3 6 9
- d) 1 2 4 5 7 8 9 10

**Your Answer:** 

**14.** In a nested loop (a loop inside another loop), what does a `break` statement do? (__ points)

- a) It exits both the inner and outer loops
- b) It only exits the innermost loop where it is placed
- c) It skips the current iteration of the outer loop
- d) It has no effect on nested loops

**Your Answer:** 

**15.** In a nested loop, what does a `continue` statement do? (__ points)

- a) It exits both the inner and outer loops
- b) It skips the rest of the current iteration of the innermost loop and moves to the next iteration of that inner loop
- c) It skips the current iteration of the outer loop
- d) It restarts the entire nested loop structure

**Your Answer:** 

<div style="page-break-before: always;"></div>

## Section 2: Short Answer & Explanation

**1.** Explain the difference between `break` and `continue`. Give a short code example (not from class) for each to demonstrate your understanding. (__ points)

**2.** What is a common misconception students have about the `continue` statement? Explain why it is incorrect and what actually happens. (__ points)

**3.** How can a programmer accidentally create an infinite loop when using a `while` loop? Give one common example and explain how to fix it. (__ points)

**4.** What is an "off-by-one" error when using `range()` in a `for` loop? Give an example of code that has this error and show the corrected version. (__ points)

**5.** When might you intentionally use an infinite loop (such as `while True`)? Explain a practical situation and how you would safely exit it. (__ points)

---

## Section 3: Coding Problems

**1.** Write a program that takes the following list of names and prints only those names that contain the letter 'J' (case-insensitive). Use `continue` to skip names that do not meet the condition. (__ points)

```python
names = ["John", "Alice", "James", "Emily", "Jack", "Sophia", "Benjamin"]
```

**Your code here:**

---

**2.** Complete the program below... (__ points)

```python
import random

# Secret prime number (do not change this part)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_number = random.choice(primes)
print("A secret prime number has been chosen...")

# Your code goes here:
for attempt in range(5):
    pass   # Replace this with your code
```

**Rules:**
- If the user enters a number divisible by `prime_number`, the game ends immediately and they lose.
- If the user enters 5 numbers that are **not** divisible by `prime_number`, they win.

---

**3.** Write a program that uses a **nested loop** to print the words stored in the following list of lists. Each inner list should be printed on its own line, with the words separated by a single space. (__ points)

```python
word_groups = [
    ["faith", "hope", "love"],
    ["pray", "serve", "give"],
    ["trust", "obey", "follow", "share"],
    ["grace", "mercy", "peace"]
]
```

**Your code here:**

---

## Biblical Integration & Reflection

**Reflect on the following questions in your own words:**

**1.** Name two ways we have biblical examples that help us understand loops in this unit.

**2.** In what way does knowing God’s promise in Genesis 8:22 comfort and help us in the world we live in?

**3.** Read John chapter 2 regarding the wedding at Cana. Can you find a possible illustration of a `for` loop in this passage? If so, write out a rough sketch of what it would look like in Python code. (Syntax does not have to be perfect.)

---

**Deliverable:** Submit this completed assessment. Self-grade your work where possible and compare with provided solutions.

© 2026 LogosTeach - All Rights Reserved.
