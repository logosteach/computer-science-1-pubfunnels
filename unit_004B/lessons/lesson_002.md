# Lesson 002 - The While Loop: Examples & Illustrations

Below are clear examples and illustrations for each learning objective in this lesson.

## 1. The syntax of the while loop

**Basic While Loop Syntax:**

```python
while condition:
    # code to repeat
    # must eventually make condition False
```

**Example:**

```python
i = 1
while i <= 5:
    print("Count:", i)
    i += 1        # Important: update the counter!
```

**Output:**  
`Count: 1` through `Count: 5`

## 2. Use a while loop with a counter or condition that eventually becomes false

**Example with Counter:**

```python
count = 0
while count < 10:
    print("Iteration", count)
    count += 1        # Counter increases → condition will become False
```

**Example with Condition:**

```python
password = ""
while password != "secret123":
    password = input("Enter password: ")
print("Access granted!")
```

## 3. Combine while loops with user input to create interactive programs

**Good Example - Interactive Menu:**

```python
choice = ""
while choice != "quit":
    print("\n1. Say Hello")
    print("2. Tell a joke")
    print("Type 'quit' to exit")
    choice = input("Enter your choice: ").lower()
    
    if choice == "1":
        print("Hello there!")
    elif choice == "2":
        print("Why do programmers prefer dark mode? Because light attracts bugs!")
```

**How this can go wrong (Bad Example):**

```python
while True:        # Dangerous!
    name = input("Enter your name: ")
    print("Hello", name)     # No way to exit!
```

*This program will run forever with no exit option.*

## 4. Infinite loops - How to identify, when to use intentionally, and how to avoid

**Accidental Infinite Loop (Common Mistake):**

```python
count = 0
while count < 10:
    print(count)        # Forgot to increment count!
```

**Intentional Infinite Loop (Useful with break):**

```python
while True:
    command = input("Enter command (or 'exit'): ")
    if command == "exit":
        break
    print("Processing:", command)
```

**Prevention Tips:**
- Always ensure the loop condition can become `False`
- Use a counter or progress variable
- Add a `break` statement for controlled exit

## 5. Biblical Reflection

> The while loop teaches us about persistence - continuing while a condition is true.  
> In the same way, Jesus taught us to pray persistently and not give up (Luke 18:1-8).  
> Yet we must also know when to stop and trust God's perfect timing (Ecclesiastes 3:1).

**Key Lesson:** Keep praying and remain faithful, but also learn to rest in God's sovereign timing.

---

*If you find any typos or errors, please let me know.*  

📧 [Send me an email](mailto:info@logosteach.com?subject=Examples%20for%20Lesson%20002)

---

© 2026 LogosTeach - All Rights Reserved.
