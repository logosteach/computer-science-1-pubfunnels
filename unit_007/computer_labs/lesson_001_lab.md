# Python Lab: Using the `assert` Keyword

**Estimated time:** 15–20 minutes  

## Lab Objective

Learn how to use `assert` statements to check **pre-conditions** (valid inputs) and **post-conditions** (function behaved correctly).

---

### Part 1: Type Checking with `assert` (Preconditions)

1. Write a function named `my_multiply` that takes two parameters `a` and `b`.  
   The function should return the product of `a` and `b`.  
   Add **assert statements** at the beginning of the function to verify that both `a` and `b` are either **integers or floats**.

    ```python
    def my_multiply(a, b):
        # Your assert statements go here
        return a * b
    ```

2. Test your function with these calls:

    ```python
    print(my_multiply(3, 4))      # Expected: 12
    print(my_multiply(2.5, 4))    # Expected: 10.0
    print(my_multiply(5, 0.0))    # Expected: 0.0
    ```

3. **Question:** What **type** of assertion test did you use in question 1?

   - Comparison (`==`, `>`, etc.)
   - Membership (`in`)
   - Identity/Type Checking (`isinstance`)

### Part 2: Checking Function Behavior (Post-Conditions)

4. Write a function named `put_next` that:

- Takes and integer `n` and a set `S`.
- Adds `n + 1` to the set `S`.
- Returns the modified set `S`.

Add an **assert statement** to verify that `n + 1` is now in the set.

```python
def put_next(n, S):
    # Add n + 1 to the set here

    # Your assert statement goes here

    return S
```

5. Test your function.

```python
S = set()                   # empty set
result = put_next(5, S)
print(result)               # expected {6}
```

6. **Question:** What **type** of assertion test did you use in question 4?

   - Comparison (`==`, `>`, etc.)
   - Membership (`in`)
   - Identity/Type Checking (`isinstance`)

### Part 3: More Practice

7. Write a function named `my_sum` that takes two parameters `x` and `y` (integers or floats) and returns their sum.
   
Add **assert statements** at the top to check that both inputs are integers or floats.

```python
def my_sum(x, y):
    # Your assert statements go here.
    return x + y
```

8. Test it.

```python
print(my_sum(10, 20))           # Expected 30
print(my_sum(3.5, 2))           # Expected 5.5
```

9. **Question:** What **type** of assertion test did you use in question 7?

   - Comparison (`==`, `>`, etc.)
   - Membership (`in`)
   - Identity/Type Checking (`isinstance`)

### Bonus Challenge (if time remains)

Try calling one of the functions with an incorrect type, for example:

```python
my_multiply("hello", 5)
```

What happens? Why is this behavior useful during development?


### Quick Tips

- Place `assert` statements at the very beginning of a function for pre-conditions.
- You can add a helpful error message like `assert isinstance(a, (int, float)), "a must be an int or float"
- `assert` is great for catching bugs during development, but remember it can be disabled with `python -O`.

&copy; 2026 LogosTeach - All Rights Reserved