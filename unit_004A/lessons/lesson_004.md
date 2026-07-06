# Short-Circuit Evaluation in Python

In this lesson, you will learn how Python uses short-circuit evaluation with the logical operators `and` and `or`. Understanding this behavior helps you write safer and more efficient code.

## Example 1: Understanding Short-Circuit Evaluation with `and`

```python
x = 5
y = 10

# Python stops evaluating as soon as the result is known
result = (x > 10) and (y > 5)
print(result)
```

**Output:**

```console
False
```

**Explanation:**  
Because `x > 10` is `False`, Python does not check `y > 5`. It already knows the entire expression must be `False`.

## Example 2: Short-Circuit Evaluation with `or`

```python
age = 17
has_permission = True

can_enter = (age >= 18) or has_permission
print(can_enter)
```

**Output:**

```console
True
```

**Explanation:**  
Because `has_permission` is `True`, Python stops and does not evaluate `age >= 18`.

## Example 3: Using Short-Circuit Evaluation to Avoid Errors

```python
username = ""

# Safe check before using len()
if username and len(username) > 5:
    print("Username is long enough")
else:
    print("Username is missing or too short")
```

**Output:**

```console
Username is missing or too short
```

**Explanation:**  
If `username` is empty (falsy), Python stops immediately and never runs `len(username)`. This prevents potential problems.

## Example 4: Preventing Division by Zero

```python
numerator = 20
denominator = 0

# Safe way to check before dividing
if denominator != 0 and numerator / denominator > 2:
    print("Result is greater than 2")
else:
    print("Cannot divide or result is not greater than 2")
```

**Output:**

```console
Cannot divide or result is not greater than 2
```

**Explanation:**  
Because `denominator != 0` is `False`, Python never attempts to divide by zero.

## Example 5: Order of Conditions Matters

```python
has_ticket = False
is_vip = True

can_watch = has_ticket or is_vip
print(can_watch)
```

**Output:**

```console
True
```

**Explanation:**  
With `or`, Python stops as soon as it finds a `True` value. The order of your conditions can affect both safety and efficiency.

## Biblical Reflection

Just as short-circuit evaluation allows us to stop checking once we have enough information, God has given us foundational truths in Scripture that are always reliable. When we know that we are loved and accepted in Christ Jesus, we do not need to keep evaluating our performance to find security. As Jesus said:

> **“If the Son sets you free, you will be free indeed.”**  
> — John 8:36

---

© 2026 LogosTeach - All Rights Reserved.