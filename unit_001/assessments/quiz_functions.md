# Python Functions Quiz  
**Topics:** Void vs fruitful functions, recursive vs iterative functions, correct base cases in recursion, hitting recursion limit, default parameters, variable arguments (*args / **kwargs), parameter ordering rules, argument count errors (too few / too many / wrong kinds)  
**Level distribution:** 14 Beginner • 6 Intermediate  
**Instructions:** Choose the single best answer unless otherwise stated.

### Beginner Level (Questions 1–14)

1. What does it mean for a function to be **void** in Python?  
   A) It must return a number  
   B) It returns `None` (either explicitly or implicitly)  
   C) It cannot accept parameters  
   D) It deletes its variables after running  

2. What is the value of `result` after this code runs?  
   ```python
   def say_hello(name):
       print("Hello " + name)
   
   result = say_hello("Alex")
   print(result)
   ```  
   A) `"Hello Alex"`  
   B) `None`  
   C) `"Alex"`  
   D) Error  

3. Which function is **fruitful** (returns a meaningful value rather than just printing)?  
   A) `def greet(): print("Hi!")`  
   B) `def square(n): return n * n`  
   C) `def countdown(n): while n > 0: n = n - 1`  
   D) `def log(msg): print("LOG:", msg)`  

4. What is printed by this code?  
   ```python
   print(print("test") == None)
   ```  
   A) `test` then `True`  
   B) `test` then `False`  
   C) Only `test`  
   D) Error  

5. Which approach is **iterative** (uses a loop instead of calling itself)?  
   A) A function that calls itself with a smaller number until it reaches 1  
   B) A `for` or `while` loop that multiplies numbers from 1 to n  
   C) A function that calls itself forever  
   D) Using `if` statements without any loop or recursion  

6. In a recursive function, the **base case** is:  
   A) The part that runs forever  
   B) The simplest case solved directly without making another recursive call  
   C) The first line of the function  
   D) Always `if n == 0`  

7. What will happen when someone calls this function?  
   ```python
   def bad_recursion(n):
       return n + bad_recursion(n - 1)
   ```  
   A) It returns a very large number instantly  
   B) It raises `RecursionError` after many calls (hits recursion depth limit)  
   C) It runs forever without error  
   D) It immediately returns 0  

8. What happens when you call this function without giving the second argument?  
   ```python
   def describe(name, age=20):
       print(name, "is", age, "years old")
   describe("Mia")
   ```  
   A) Error — missing argument  
   B) Prints: `Mia is 20 years old`  
   C) Prints: `Mia is None years old`  
   D) Prints nothing  

9. Which call is **valid** for this function?  
   ```python
   def info(title, year=2023, author="Unknown"):
       pass
   ```  
   A) `info("Book", author="Jane")`  
   B) `info(year=2024, "Book")`  
   C) `info("Book", 2024, "Jane", extra="data")`  
   D) `info()`  

10. What does `*args` let you do in a function definition?  
    A) Accept exactly two extra arguments  
    B) Accept any number of extra positional arguments (collected as a tuple)  
    C) Accept only keyword arguments  
    D) Force all arguments to be optional  

11. Which function definition follows Python's correct parameter order rules?  
    A) `def f(a, b=10, *args, **kwargs)`  
    B) `def f(*args, a, b=5)`  
    C) `def f(**kwargs, a)`  
    D) `def f(a, **kwargs, *args)`  

12. What happens if you call a function with **too few** required arguments (and no defaults for them)?  
    A) The missing ones become `None` automatically  
    B) Raises `TypeError: missing required positional argument`  
    C) The function runs anyway, ignoring the missing ones  
    D) Nothing — Python fills them silently  

13. What is printed by this code?  
    ```python
    def stats(first, second=0, *others):
        print(first, second, len(others))
    
    stats(100, 200, 300, 400, 500)
    ```  
    A) `100 0 4`  
    B) `100 200 3`  
    C) `100 200 4`  
    D) `TypeError`  

14. Which recursive function has a proper base case that prevents infinite recursion?  
    A) `def count(n): return count(n+1)`  
    B) `def count(n): if n <= 0: return 0; return 1 + count(n-1)`  
    C) `def count(n): return n + count(n)`  
    D) `def count(n): if n > 0: return count(n-1)`  

### Intermediate Level (Questions 15–20)

15. What happens when you run this recursive function?  
    ```python
    def down(n):
        print(n)
        down(n-1)
    down(4)
    ```  
    A) Prints: 4 3 2 1 0 and stops cleanly  
    B) Prints downward numbers until it hits the recursion limit → `RecursionError`  
    C) Prints nothing  
    D) Infinite printing without crashing  

16. Which parameter ordering is **not allowed** in Python?  
    A) required → default → *args → **kwargs  
    B) required → *args → default → **kwargs  
    C) *args → required parameters  
    D) default parameters → *args → **kwargs  

17. What value is returned by this call?  
    ```python
    def combine(x, y=1, *extra, z=99, **named):
        return (x, y, extra, z, named)
    
    combine(10, 20, 30, 40, z=50, color="blue")
    ```  
    A) `(10, 20, (30,40), 50, {'color':'blue'})`  
    B) `(10, 1, (20,30,40), 99, {'z':50, 'color':'blue'})`  
    C) `TypeError` (multiple values for z)  
    D) `(10, 20, (), 50, {'color':'blue'})`  

18. The most common reason Python raises `RecursionError: maximum recursion depth exceeded` is:  
    A) The function has too many parameters  
    B) The recursive calls go deeper than Python's default limit (~1000 levels)  
    C) The base case returns the wrong type  
    D) Too many keyword arguments were used  

19. What is printed by this recursive function?  
    ```python
    def echo(n=4):
        if n == 0:
            return
        print(n, end=" ")
        echo(n-1)
        print(n, end=" ")
    
    echo(3)
    ```  
    A) `3 2 1 1 2 3`  
    B) `3 2 1`  
    C) `1 2 3 3 2 1`  
    D) `3 2 1 0`  

20. Which function call raises a **TypeError**?  
    ```python
    def build(a, b, c=0, *more, **settings):
        pass
    ```  
    A) `build(5, 10)`  
    B) `build(5, 10, 15)`  
    C) `build(a=1, b=2, more=[3,4])`  
    D) `build(5, c=20, b=10)`  

---

**End of Quiz**