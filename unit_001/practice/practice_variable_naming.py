# =============================================================================
# Practice: Variable Naming Rules in Python
# =============================================================================
# Goal: Help you understand, remember, and *apply* the rules for naming
# variables so you can write clean, readable, and error-free code.
#
# THE OFFICIAL RULES (what Python requires):
#   1. A variable name must start with a letter (a-z, A-Z) or an underscore (_)
#   2. The rest of the name can only contain letters, numbers, and underscores
#   3. Variable names are case-sensitive (age, Age, and AGE are three different variables)
#   4. You cannot use a Python keyword (if, for, while, class, def, return, True, False, None, etc.)
#
# STRONGLY RECOMMENDED STYLE (PEP 8 – the Python community standard):
#   - Use snake_case for variable and function names (lowercase with underscores)
#   - Choose descriptive names that explain the purpose
#   - Avoid single-letter names except for very short loops (i, j, k)
#   - Constants are often written in UPPER_SNAKE_CASE
#
# Tip: Good names make your code easier for you (and others) to understand later!
# =============================================================================

print("=" * 70)
print("PART 1: Valid Variable Names")
print("=" * 70)

# These names follow the rules and are valid:
student_name = "Hannah"
age = 13
_total_score = 95
score2 = 88
is_passing = True
MAX_ATTEMPTS = 3          # common style for a constant

print("student_name  =", student_name)
print("age           =", age)
print("_total_score  =", _total_score)
print("score2        =", score2)
print("is_passing    =", is_passing)
print("MAX_ATTEMPTS  =", MAX_ATTEMPTS)


print("\n" + "=" * 70)
print("PART 2: Invalid Variable Names (These will cause errors)")
print("=" * 70)
print("""
The following names break the rules. They are shown as comments
because Python would refuse to run them:

# 2nd_place = "silver"     ← cannot start with a number
# student-name = "Alex"    ← hyphens are not allowed (use underscore instead)
# class = "Algebra"        ← 'class' is a reserved keyword
# for = 10                 ← 'for' is a reserved keyword
# $price = 19.99           ← special characters (except _) are not allowed
# my variable = 5          ← spaces are not allowed
""")


print("=" * 70)
print("PART 3: Case Sensitivity Demonstration")
print("=" * 70)

score = 85
Score = 92
SCORE = 100

print("score =", score)   # 85
print("Score =", Score)   # 92
print("SCORE =", SCORE)   # 100
print("These are three completely different variables!")


print("\n" + "=" * 70)
print("PART 4: Practice – Identify Valid or Invalid")
print("=" * 70)
print("For each name below, decide: Valid or Invalid?")
print("Then check the answer that follows.\n")

# 1
print("1.  total_points")
print("    → Valid  (starts with letter, only letters + underscore)")
print()

# 2
print("2.  3rd_attempt")
print("    → Invalid (starts with a number)")
print()

# 3
print("3.  user-name")
print("    → Invalid (contains a hyphen)")
print()

# 4
print("4.  _hidden_value")
print("    → Valid   (may start with underscore)")
print()

# 5
print("5.  while")
print("    → Invalid (while is a Python keyword)")
print()

# 6
print("6.  finalScore")
print("    → Valid   (technically allowed, but snake_case is preferred)")
print()

# 7
print("7.  my var")
print("    → Invalid (contains a space)")
print()

# 8
print("8.  PI")
print("    → Valid   (all caps is fine, often used for constants)")
print()


print("=" * 70)
print("PART 5: Practice – Fix the Broken Names")
print("=" * 70)
print("Each line below has an invalid name. Rewrite it as a valid,")
print("readable name. (Answers are shown afterward for checking.)\n")

print("Original (broken)          →  Suggested fix")
print("-" * 50)
print("1.  1st_place              →  first_place")
print("2.  student-grade          →  student_grade")
print("3.  class                  →  course_name  (or class_name)")
print("4.  total$                 →  total")
print("5.  final score            →  final_score")
print("6.  2x_value               →  double_value  (or value_times_two)")
print()


print("=" * 70)
print("PART 6: Practice – Choose Better Names")
print("=" * 70)
print("The names below are valid but poor. Suggest a clearer name.\n")

print("Poor name          →  Better name (examples)")
print("-" * 50)
print("x                  →  width  (or height, score, etc.)")
print("n                  →  number_of_students")
print("temp               →  temperature  (or temporary_value)")
print("a1                 →  average_score")
print("data               →  student_scores  (be specific!)")
print("flag               →  is_complete  (or has_passed)")
print()


print("=" * 70)
print("PART 7: Synthesis Challenge")
print("=" * 70)
print("""
Create good variable names for the situations below.
Write them as real Python assignment statements and add a
short comment explaining why the name is good.

Example:
number_of_correct_answers = 17   # clear, descriptive, snake_case
""")

print("\nSituation A: The number of hours a student studied this week")
# Write your variable here:
# ________________ = ______

print("\nSituation B: Whether a quiz has been submitted or not")
# Write your variable here:
# ________________ = ______

print("\nSituation C: The maximum number of points possible on a test")
# Write your variable here:
# ________________ = ______

print("\nSituation D: A student’s first and last name combined")
# Write your variable here:
# ________________ = ______

print("\nSituation E: The remainder when total points are divided by 10")
# Write your variable here:
# ________________ = ______


print("\n" + "=" * 70)
print("PART 8: Quick Self-Check")
print("=" * 70)
print("""
Before you finish, answer these in your mind (or on paper):

1. Can a variable name start with an underscore?          (Yes)
2. Can a variable name contain a hyphen?                  (No)
3. Are 'total' and 'Total' the same variable?             (No)
4. Is 'for' a legal variable name?                        (No – keyword)
5. Which is better style: finalScore  or  final_score ?   (final_score)
""")

print("=" * 70)
print("Excellent work!")
print("Good variable names are one of the simplest ways to make your")
print("code readable and professional. Keep practicing them until they")
print("feel natural.")
print("=" * 70)
