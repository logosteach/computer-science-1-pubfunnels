<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Link to your custom CSS -->
    <link rel="stylesheet" href="../../static/css/stylesheet.css">
</head>

<body class="lesson-body">
    <header class="document-header">
        <div class="header-content">
            <div class="header-left">
                Python with a Worldview
            </div>
            <div class="header-right">
                LogosTeach
            </div>
        </div>
    </header>

    <div
        style="line-height: 1.7; max-width: 1000px; margin: 40px auto; padding: 35px; background-color: #ffffff; color: #333333; border: 1px solid #e0e0e0; border-radius: 10px;">

        <h1
            style="font-size: 2.6em; margin-bottom: 25px; color: #1a3c5e; border-bottom: 5px solid #2c7a7b; padding-bottom: 18px; font-weight: 700;">
            <strong>Lesson Examples - Truthy and Falsy Values</strong>
        </h1>

        <p style="font-size: 1.1em; margin-bottom: 40px; color: #444444;">
            These examples explain how Python evaluates values in a Boolean context. You will learn to identify truthy and falsy values, use implicit Boolean checking for cleaner code, and understand the difference between explicit comparisons and truthy evaluation. This concept helps write more Pythonic and readable programs.
        </p>

        <!-- Example 1: Introduction to Truthy and Falsy Values -->
        <h2
            style="font-size: 1.85em; margin: 50px 0 18px 0; color: #2c7a7b; border-left: 6px solid #2c7a7b; padding-left: 16px;">
            Understanding Truthy and Falsy Values
        </h2>
        <div style="margin-bottom: 45px; padding-left: 28px;">
            <p>Every value in Python has a Boolean interpretation when used in an <code>if</code> statement, <code>while</code> loop, or with logical operators. Values that evaluate to <code>True</code> are called <strong>truthy</strong>. Values that evaluate to <code>False</code> are called <strong>falsy</strong>.</p>
            
            <p>Python uses the built-in <code>bool()</code> function to explicitly convert any value to its Boolean equivalent.</p>
            
            <pre><code class="language-python"># Falsy values
print("Falsy examples:")
print(bool(False))      # False
print(bool(None))       # False
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False (empty string)
print(bool([]))         # False (empty list)
print(bool({}))         # False (empty dict)
print(bool(set()))      # False (empty set)
print(bool(()))         # False (empty tuple)

# Truthy values
print("\nTruthy examples:")
print(bool(True))       # True
print(bool(1))          # True
print(bool(-5))         # True (non-zero)
print(bool(3.14))       # True
print(bool("hello"))    # True (non-empty string)
print(bool([1, 2, 3]))  # True (non-empty list)
print(bool({"key": "value"}))  # True
print(bool("0"))        # True (non-empty string, even though it looks like zero)</code></pre>
            
            <p><strong>Output:</strong></p>
            <pre><code class="language-console">Falsy examples:
False
False
False
False
False
False
False
False
False

Truthy examples:
True
True
True
True
True
True
True
True</code></pre>
            
            <div class="tip">
                <strong>Tip:</strong> Memorize the common falsy values: <code>False</code>, <code>None</code>, numeric zero, and empty collections/strings. Everything else is truthy.
            </div>
        </div>

        <!-- Example 2: Implicit Boolean Checking -->
        <h2
            style="font-size: 1.85em; margin: 50px 0 18px 0; color: #2c7a7b; border-left: 6px solid #2c7a7b; padding-left: 16px;">
            Implicit Boolean Checking (Pythonic Style)
        </h2>
        <div style="margin-bottom: 45px; padding-left: 28px;">
            <p>Instead of explicitly comparing to an empty value, Python allows direct use of the variable in a Boolean context. This is called <strong>implicit Boolean evaluation</strong> or <strong>truthy checking</strong>.</p>
            
            <pre><code class="language-python"># Explicit (less Pythonic)
name = input("Enter your name: ")
if name != "":
    print(f"Hello, {name}!")
else:
    print("Name cannot be empty.")

# Implicit / Truthy (more Pythonic and readable)
name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!")
else:
    print("Name cannot be empty.")</code></pre>
            
            <p><strong>Output (example with input "Alice"):</strong></p>
            <pre><code class="language-console">Hello, Alice!</code></pre>
            
            <p>This works because a non-empty string is truthy, while an empty string <code>""</code> is falsy.</p>
            
            <div class="tip">
                <strong>Tip:</strong> Use implicit checking for readability: <code>if items:</code> instead of <code>if len(items) &gt; 0:</code> or <code>if items != []:</code>.
            </div>
        </div>

        <!-- Example 3: Checking Collections and Numbers -->
        <h2
            style="font-size: 1.85em; margin: 50px 0 18px 0; color: #2c7a7b; border-left: 6px solid #2c7a7b; padding-left: 16px;">
            Checking Collections, Numbers, and Other Types
        </h2>
        <div style="margin-bottom: 45px; padding-left: 28px;">
            <p>Implicit checking is especially useful with lists, dictionaries, and numbers.</p>
            
            <pre><code class="language-python"># Shopping cart example
cart = []  # empty cart

if cart:
    print("You have items in your cart.")
    print(f"Total items: {len(cart)}")
else:
    print("Your cart is empty. Add some items!")

# Score validation
score = 0
if score:
    print(f"Your score is {score}. Great job!")
else:
    print("No score recorded yet. Keep practicing!")

# User preferences (dict)
preferences = {"theme": "dark"}
if preferences:
    print("Preferences loaded.")
else:
    print("Using default settings.")</code></pre>
            
            <p><strong>Output:</strong></p>
            <pre><code class="language-console">Your cart is empty. Add some items!
No score recorded yet. Keep practicing!
Preferences loaded.</code></pre>
            
            <div class="warning-box">
                Be careful with numbers: <code>0</code> is falsy, which can be surprising in contexts like scores or counters. Use explicit checks like <code>if score is not None</code> or <code>if score &gt;= 0</code> when zero is a valid value.
            </div>
        </div>

        <!-- Example 4: Explicit == True vs Implicit Truthy -->
        <h2
            style="font-size: 1.85em; margin: 50px 0 18px 0; color: #2c7a7b; border-left: 6px solid #2c7a7b; padding-left: 16px;">
            Explicit Comparison vs Implicit Truthy Evaluation
        </h2>
        <div style="margin-bottom: 45px; padding-left: 28px;">
            <p>Writing <code>if variable == True:</code> is usually unnecessary and can even be incorrect for truthy values that are not exactly the boolean <code>True</code>.</p>
            
            <pre><code class="language-python">is_active = 1          # truthy but not exactly True
is_logged_in = True    # exactly True

# Not recommended
if is_active == True:
    print("Account is active (using == True)")

# Better - implicit truthy check
if is_active:
    print("Account is active (truthy check)")

# This would fail or behave unexpectedly in some cases
if is_logged_in == True:
    print("User is logged in")
    
# The implicit way is cleaner and more Pythonic
if is_logged_in:
    print("User is logged in (recommended)")</code></pre>
            
            <p><strong>Output:</strong></p>
            <pre><code class="language-console">Account is active (using == True)
Account is active (truthy check)
User is logged in
User is logged in (recommended)</code></pre>
            
            <div class="tip">
                <strong>Tip:</strong> Reserve <code>== True</code> or <code>== False</code> only when you specifically need to distinguish the boolean <code>True</code> from other truthy values. In most cases, implicit evaluation is preferred.
            </div>
        </div>

        <!-- Example 5: Practical Combined Example -->
        <h2
            style="font-size: 1.85em; margin: 50px 0 18px 0; color: #2c7a7b; border-left: 6px solid #2c7a7b; padding-left: 16px;">
            Practical Example: User Registration Check
        </h2>
        <div style="margin-bottom: 45px; padding-left: 28px;">
            <p>Combine truthy checks for multiple fields in a registration flow.</p>
            
            <pre><code class="language-python">username = input("Choose a username: ").strip()
email = input("Enter your email: ").strip()
age_str = input("Enter your age: ").strip()

# Implicit checks for presence and validity
if username and email and age_str:
    try:
        age = int(age_str)
        if age >= 13:  # additional explicit check
            print(f"Welcome, {username}! Registration complete.")
            print("Account created successfully.")
        else:
            print("Sorry, you must be at least 13 years old.")
    except ValueError:
        print("Please enter a valid number for age.")
else:
    print("All fields (username, email, age) are required.")</code></pre>
            
            <p><strong>Sample Output (with valid input):</strong></p>
            <pre><code class="language-console">Welcome, student123! Registration complete.
Account created successfully.</code></pre>
            
            <p>This pattern keeps code clean while ensuring required data is present before proceeding.</p>
        </div>

        <!-- Biblical Reflection -->
        <h2
            style="font-size: 1.85em; margin: 50px 0 18px 0; color: #2c7a7b; border-left: 6px solid #2c7a7b; padding-left: 16px;">
            Biblical Reflection
        </h2>
        <div
            style="margin-bottom: 45px; padding-left: 28px; font-style: italic; color: #1a3c5e; background-color: #f0f7f7; padding: 25px; border-left: 6px solid #2c7a7b;">
            <p>
                In programming, we must learn to see values exactly as Python sees them — some are truthy, others falsy — without assuming or adding our own interpretations. God sees things perfectly as they truly are. Nothing is hidden from His sight.
            </p>
            <p style="margin-top: 15px;">
                From our human perspective, truth can sometimes seem relative or uncertain. We are prone to think that God Himself thinks and sees things this way as well. Yet, in Christ Jesus we have direct access to our Heavenly Father. He is teaching us, training us in godliness in Christ Jesus so that the falsehoods of the world will become clearer, and we will be prepared for every good work in Christ Jesus.
            </p>
            <p style="margin-top: 15px;">
                <strong>Scripture:</strong><br>
                “And do not be conformed to this world, but be transformed by the renewing of your mind, that you may prove what is that good and acceptable and perfect will of God.” (Romans 12:2 NKJV)<br>
                “For the grace of God that brings salvation has appeared to all men, teaching us that, denying ungodliness and worldly lusts, we should live soberly, righteously, and godly in the present age.” (Titus 2:11-12 NKJV)<br>
                “And the world is passing away, and the lust of it; but he who does the will of God abides forever.” (1 John 2:17 NKJV)
            </p>
        </div>

        <div
            style="background-color: #f8f9fa; padding: 22px; border-left: 6px solid #2c7a7b; margin: 35px 0; font-size: 1.05em;">
            <em>If you find any typos or errors, please let me know.</em><br><br>
            <a href="mailto:info@logosteach.com?subject=Feedback for Lesson Examples - Truthy and Falsy Values"
                style="color: #2c7a7b; font-weight: 600; text-decoration: none;">📧 Send me an email</a>
        </div>

        <div
            style="margin-top: 70px; padding-top: 25px; border-top: 2px solid #e0e0e0; font-size: 0.95em; color: #777777; text-align: center;">
            © 2026 LogosTeach - All Rights Reserved.
        </div>

        <p>Labs, Practice Files and Assessments are developed in collaboration with the Grok AI assistant under instructor supervision and review.</p>

    </div>

</body>

</html>