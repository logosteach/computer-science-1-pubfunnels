# Python Loops Quiz  
**Topics:** for / while loops, break, continue, range(), infinite loops, nested loops  
**Level distribution:** 14 Beginner • 6 Intermediate  
**Instructions:** Choose the single best answer unless otherwise stated. Assume all code runs without syntax errors unless stated otherwise.

### Beginner Level (Questions 1–14)

1. What does the `range(5)` function produce?  
   A) Numbers from 0 to 5 (inclusive)  
   B) Numbers from 0 to 4  
   C) Numbers from 1 to 5  
   D) An empty sequence  

2. How many times does this loop run?  
   ```python
   for i in range(3):
       print("Hello")
   ```  
   A) 2 times  
   B) 3 times  
   C) 4 times  
   D) Never  

3. What is printed by this code?  
   ```python
   for i in range(2, 7, 2):
       print(i, end=" ")
   ```  
   A) 2 3 4 5 6  
   B) 2 4 6  
   C) 2 4 6 8  
   D) 2 5  

4. Which loop is guaranteed to run at least once? (in typical usage)  
   A) `for` loop  
   B) `while` loop  
   C) Neither — both can have zero iterations  
   D) Both always run at least once  

5. What does this while loop do?  
   ```python
   count = 0
   while count < 4:
       print(count)
       count += 1
   ```  
   A) Prints 0 1 2 3 4  
   B) Prints 0 1 2 3  
   C) Infinite loop  
   D) Prints nothing  

6. What keyword immediately stops the current loop iteration and moves to the next one?  
   A) `break`  
   B) `continue`  
   C) `pass`  
   D) `exit`  

7. What keyword completely exits the loop (even if the condition is still true)?  
   A) `break`  
   B) `continue`  
   C) `return`  
   D) `stop`  

8. What is printed?  
   ```python
   for i in range(6):
       if i == 3:
           continue
       print(i, end=" ")
   ```  
   A) 0 1 2 3 4 5  
   B) 0 1 2 4 5  
   C) 0 1 2  
   D) 3  

9. What is printed?  
   ```python
   for i in range(1, 6):
       if i == 4:
           break
       print(i, end=" ")
   ```  
   A) 1 2 3 4  
   B) 1 2 3  
   C) 1 2 3 4 5  
   D) Infinite  

10. Which is the correct way to create an infinite loop?  
    A) `while True:`  
    B) `for i in range(-1):`  
    C) `while i < 10:` (with no update to i)  
    D) Both A and C can create infinite loops  

11. How many lines are printed?  
    ```python
    i = 1
    while i <= 3:
        print("Line")
        i += 1
    ```  
    A) 2  
    B) 3  
    C) 4  
    D) Infinite  

12. What is a common use of `range(len(s))`?  
    A) To loop over characters of string `s` by index  
    B) To create numbers from 0 to length of `s`  
    C) Both A and B are correct  
    D) To reverse the string  

13. What does this nested loop print (just count the * characters)?  
    ```python
    for i in range(3):
        for j in range(2):
            print("*", end="")
        print()
    ```  
    A) 3 stars total  
    B) 6 stars total (3 lines of 2)  
    C) 2 stars total  
    D) Triangle shape  

14. Which loop will **not** finish normally?  
    A) `for i in range(10): pass`  
    B) `while False: print("hi")`  
    C) `i=0; while i<5: i+=1`  
    D) `for i in []: print(i)`  

### Intermediate Level (Questions 15–20)

15. What is printed?  
    ```python
    for i in range(4):
        if i == 2:
            continue
        print(i, end=" ")
    else:
        print("Done")
    ```  
    A) 0 1 3 Done  
    B) 0 1 Done  
    C) 0 1 2 3 Done  
    D) 0 1 3  

16. What is printed?  
    ```python
    n = 0
    while n < 5:
        n += 1
        if n == 3:
            break
        print(n, end=" ")
    else:
        print("Loop finished")
    ```  
    A) 1 2 Loop finished  
    B) 1 2  
    C) 1 2 3 Loop finished  
    D) 1 2 3  

17. How many times is "x" printed?  
    ```python
    for i in range(1, 4):
        for j in range(1, i+1):
            print("x", end="")
        print()
    ```  
    A) 6  
    B) 10  
    C) 1+2+3 = 6  
    D) Infinite  

18. Which code creates an **infinite loop**?  
    A) `while True: pass`  
    B) `i = 0; while i < 10: i -= 1`  
    C) `for _ in iter(int, 1): pass`  
    D) All of the above  

19. What is the final value of `total`?  
    ```python
    total = 0
    for i in range(10):
        if i % 3 == 0:
            continue
        total += i
    print(total)
    ```  
    A) 45 (sum 0–9)  
    B) 30 (skips 0,3,6,9)  
    C) 36 (skips 3,6,9)  
    D) 0  

20. What does this nested loop with break do? (how many * printed?)  
    ```python
    count = 0
    for i in range(5):
        for j in range(5):
            count += 1
            print("*", end="")
            if j == 2:
                break
        if i == 3:
            break
    print("\nTotal:", count)
    ```  
    A) 15 stars  
    B) 20 stars  
    C) 3 rows × 3 = 9 stars  
    D) 4 rows × 3 = 12 stars  

---

**End of Quiz**