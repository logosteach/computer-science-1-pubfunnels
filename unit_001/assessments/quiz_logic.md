# Python Booleans & Conditionals Quiz  
**Topics:** Boolean values, comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`), `if` / `elif` / `else`, logical operators (`and`, `or`, `not`), bitwise XOR (`^`)  
**Level distribution:** 14 Beginner • 6 Intermediate  
**Instructions:** Choose the single best answer unless otherwise stated.

### Beginner Level (Questions 1–14)

1. What are the two possible Boolean values in Python?  
   A) `true` and `false`  
   B) `True` and `False`  
   C) `1` and `0`  
   D) `yes` and `no`  

2. What is the result of `5 > 3`?  
   A) `5`  
   B) `True`  
   C) `False`  
   D) Error  

3. Which comparison operator checks for inequality?  
   A) `=`  
   B) `==`  
   C) `!=`  
   D) `><`  

4. What does this expression evaluate to?  
   ```python
   10 == 10.0
   ```  
   A) `False`  
   B) `True`  
   C) Error  
   D) `10`  

5. What is printed by this code?  
   ```python
   x = 7
   if x > 5:
       print("Big")
   else:
       print("Small")
   ```  
   A) Big  
   B) Small  
   C) Nothing  
   D) Error  

6. Which block will execute in this code?  
   ```python
   score = 85
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   else:
       print("C")
   ```  
   A) A  
   B) B  
   C) C  
   D) Nothing  

7. What does `not True` evaluate to?  
   A) `True`  
   B) `False`  
   C) `None`  
   D) Error  

8. What is the result of `True and False`?  
   A) `True`  
   B) `False`  
   C) `None`  
   D) Error  

9. What is printed?  
   ```python
   age = 16
   if age >= 18 or age <= 12:
       print("Special")
   else:
       print("Normal")
   ```  
   A) Special  
   B) Normal  
   C) Error  
   D) Nothing  

10. What is the value of this expression?  
    ```python
    not (5 > 10 or 3 < 1)
    ```  
    A) `True`  
    B) `False`  
    C) `None`  
    D) Error  

11. Which is **true**?  
    A) `""` is `True`  
    B) `0` is `True`  
    C) `[]` is `False`  
    D) `"False"` is `False`  

12. What is printed?  
    ```python
    temperature = 25
    if temperature > 30:
        print("Hot")
    elif temperature > 20:
        print("Warm")
    elif temperature > 10:
        print("Cool")
    else:
        print("Cold")
    ```  
    A) Hot  
    B) Warm  
    C) Cool  
    D) Cold  

13. What does `True ^ False` evaluate to? (`^` is bitwise XOR)  
    A) `True`  
    B) `False`  
    C) `1`  
    D) Error  

14. What is the result?  
    ```python
    print(7 < 10 and 3 != 3)
    ```  
    A) `True`  
    B) `False`  
    C) `None`  
    D) Error  

### Intermediate Level (Questions 15–20)

15. What is printed by this code?  
    ```python
    x = 4
    if x > 0 and x < 10:
        print("A")
    elif x > 0 or x < 10:
        print("B")
    else:
        print("C")
    ```  
    A) A  
    B) B  
    C) C  
    D) Nothing  

16. Which expression is **True**?  
    A) `not 0`  
    B) `"" or 0`  
    C) `not [] and 5 > 2`  
    D) `False ^ True ^ False`  

17. What is the final output?  
    ```python
    a = 10
    b = 5
    if a > b:
        if b != 0:
            print("Divisible")
        else:
            print("Zero")
    else:
        print("Small")
    ```  
    A) Divisible  
    B) Zero  
    C) Small  
    D) Nothing  

18. What does `True ^ True` evaluate to?  
    A) `True`  
    B) `False`  
    C) `1`  
    D) `0`  

19. Which of these evaluates to **False**?  
    A) `bool("False")`  
    B) `0 or "" or []`  
    C) `not (False or True)`  
    D) `5 <= 5 and 3 >= 4`  

20. What is printed?  
    ```python
    value = -3
    if value > 0:
        print("Positive")
    elif value < 0:
        print("Negative")
    elif value == 0:
        print("Zero")
    print("Done")
    ```  
    A) Positive Done  
    B) Negative Done  
    C) Zero Done  
    D) Negative (and nothing else)  

---

**End of Quiz**