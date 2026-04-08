# Python Lab: Using the `assert` Keyword – Solutions Key

**Teacher Reference Only**

### Part 1: Type Checking with `assert` (Preconditions)

1. **Solution for `my_multiply`:**

   ```python
   def my_multiply(a, b):
       assert isinstance(a, (int, float)), "a must be an int or float"
       assert isinstance(b, (int, float)), "b must be an int or float"
       return a * b
   ```

2. **Expected test outputs:**
   - `my_multiply(3, 4)` → `12`
   - `my_multiply(2.5, 4)` → `10.0`
   - `my_multiply(5, 0.0)` → `0.0`

3. **Question answer:**  
   **Identity / Type checking** (`isinstance`)

---

### Part 2: Checking Function Behavior (Postconditions)

4. **Solution for `put_next`:**

   ```python
   def put_next(n, S):
       S.add(n + 1)
       assert (n + 1) in S, f"{n + 1} should be in the set after adding"
       return S
   ```

5. **Expected test output:**  
   `{6}`

6. **Question answer:**  
   **Membership** (`in`)

---

### Part 3: More Practice

7. **Solution for `my_sum`:**

   ```python
   def my_sum(x, y):
       assert isinstance(x, (int, float)), "x must be an int or float"
       assert isinstance(y, (int, float)), "y must be an int or float"
       return x + y
   ```

8. **Expected test outputs:**
   - `my_sum(10, 20)` → `30`
   - `my_sum(3.5, 2)` → `5.5`

9. **Question answer:**  
   **Identity / Type checking** (`isinstance`)

---

### Bonus Challenge

Calling `my_multiply("hello", 5)` (or any incorrect type) raises an **`AssertionError`**.

**Why this is useful:**  
It catches bugs early during development by immediately alerting the programmer when invalid inputs are passed.

---

### Quick Tips (Reminder)

- Place `assert` statements at the **very beginning** of a function for preconditions.
- Adding a helpful error message improves debugging:
  ```python
  assert isinstance(a, (int, float)), "a must be an int or float"
  ```
- `assert` is excellent for development and testing, but can be disabled with `python -O`.
