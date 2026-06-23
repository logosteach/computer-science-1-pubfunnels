# Unit 004B Assessment – Answer Key

**Unit:** 4B – Loop Control Statements (`break` and `continue`)  
**Total Points:** 100 (suggested)

---

## Section 1: Knowledge & Understanding – Answer Key

**1.** B  
**Explanation:** Using a loop is the most efficient and scalable way to process a large number of similar items (campers’ medical forms).

**2.** b  
**Explanation:** `range(0, 15)` generates numbers from 0 up to (but not including) 15.

**3.** b  
**Explanation:** The loop prints `1`, then `3`. When `count` becomes `5`, the condition `count != 5` becomes false and the loop stops.

**4.** b  
**Explanation:** This is the correct `while` loop implementation that safely iterates through the list using an index.

**5.** b  
**Explanation:** `range(3, 5, 2)` only produces `3`. The `stop` value needs to be increased (e.g., `range(3, 12, 2)`) to generate five odd numbers.

**6.** b  
**Explanation:** Since Samantha doesn’t know in advance how many bills/coins are in the bag, a `while` loop is the appropriate choice.

**7.** b  
**Explanation:** `message.split()` breaks the string into words. Looping over the result prints each word on its own line.

**8.** c  
**Explanation:** The loop prints the message 1001 times (counter goes from 0 to 1000, then breaks when `counter > 1000`).

**9.** b  
**Explanation:** The code strips whitespace and uses `continue` to skip empty strings, so only real prayer requests are printed.

**10.** b  
**Explanation:** `break` immediately exits the loop entirely.

**11.** b  
**Explanation:** Searching until a match is found and then stopping is a classic and practical use of `break`.

**12.** b  
**Explanation:** `continue` skips the rest of the current iteration and moves to the next one.

**13.** b  
**Explanation:** All multiples of 3 are skipped by `continue`, so the output is: `1 2 4 5 7 8 10`

**14.** b  
**Explanation:** In nested loops, `break` only exits the innermost loop where it is written.

**15.** b  
**Explanation:** `continue` in a nested loop only affects the innermost loop — it skips to the next iteration of the inner loop.

---

## Section 2: Short Answer & Explanation – Sample Answers

**1.**  
`break` immediately exits the loop. `continue` skips the rest of the current iteration and moves to the next one.

**Example:**
```python
for num in range(10):
    if num == 5:
        break          # stops the loop completely
    if num % 2 == 0:
        continue       # skips even numbers
    print(num)
```

**2.**  
A common misconception is that `continue` restarts the loop from the beginning. In reality, it only skips the remaining code in the current iteration and proceeds to the next iteration.

**3.**  
Forgetting to update the loop variable inside a `while` loop is a common cause of infinite loops.

**Example (buggy):**
```python
count = 0
while count < 5:
    print(count)
    # count is never increased → infinite loop
```

**Fix:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**4.**  
An off-by-one error occurs when the loop runs one time too many or one time too few.

**Buggy example:**
```python
for i in range(5):          # prints 0,1,2,3,4  (5 times)
    print(i)
```

**Corrected (if we wanted 1–5):**
```python
for i in range(1, 6):       # prints 1,2,3,4,5
    print(i)
```

**5.**  
You might use `while True` when you want the loop to continue until a specific condition is met inside the loop (e.g., waiting for valid user input or a game loop).

**Example:**
```python
while True:
    answer = input("Enter password: ")
    if answer == "faith":
        print("Access granted")
        break
```

---

## Section 3: Coding Problems – Sample Solutions

**1. Filtering names with the letter 'J'**

```python
names = ["John", "Alice", "James", "Emily", "Jack", "Sophia", "Benjamin"]

for name in names:
    if 'j' not in name.lower():
        continue
    print(name)
```

**2. Prime Number Guessing Game**

```python
import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_number = random.choice(primes)
print("A secret prime number has been chosen...")

correct_guesses = 0

for attempt in range(5):
    try:
        guess = int(input(f"Attempt {attempt + 1}/5 - Enter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess % prime_number == 0:
        print("You entered a multiple of the secret prime. You lose!")
        break
    else:
        correct_guesses += 1
        print("Good guess!")

if correct_guesses == 5:
    print("Congratulations! You win!")
```

**3. Nested Loop to Print Word Groups**

```python
word_groups = [
    ["faith", "hope", "love"],
    ["pray", "serve", "give"],
    ["trust", "obey", "follow", "share"],
    ["grace", "mercy", "peace"]
]

for group in word_groups:
    line = " ".join(group)
    print(line)
```

---

## Biblical Integration & Reflection – Sample Answers

**1.**  
Two biblical examples that help us understand loops:
- The repeating cycles of day and night, seasons, and years (Genesis 8:22) illustrate consistent, repeated processes.
- The idea of perseverance and pressing forward (Philippians 3:13-14) can be compared to using `continue` to keep moving ahead despite obstacles.

**2.**  
God’s promise in Genesis 8:22 that “seedtime and harvest, cold and heat, summer and winter, day and night shall not cease” brings great comfort. It reminds us that even in a chaotic and uncertain world, God is faithful and maintains order. We can trust that the basic rhythms of life will continue because He sustains them.

**3.** Possible illustration of a `for` loop in John 2 (Wedding at Cana):

```python
# Rough sketch (not exact syntax)
servants = ["servant1", "servant2", "servant3", "servant4", "servant5", "servant6"]

for servant in servants:
    # Each servant fills jars with water as instructed
    fill_jars_with_water(servant)

# Then Jesus turns the water into wine
```

This represents the servants going through a repeated action (filling jars) one by one.

---

**End of Answer Key**

© 2026 LogosTeach – All Rights Reserved
