<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# The IDLE Editor: Writing our first scripts

Welcome to the **IDLE Editor** 
This is where you can type Python code **multiple lines at a time**. You will only see the results after you save the script file and then 
choose the `Run` option in IDLE.

**Note:** Remember, all python script files must end with the `*.py` extension.

Open the IDLE Editor window and then proceed..

---

## Calculate a hypotenuse

In this labe we are going to calculate the length of the hypotenuse of a right triangle.

In mathematics, a right triangle has two legs and a hypotenuse. The hypotenuse is the side of the triangle that is *opposite* the right angle. The famous formula, also known as the Pythagorean theorem states that:

$a^2 + b^2 = c^2$

Where $a$ and $b$ are the legs, and $c$ is the length of the hypotenuse. Now if we take the square root of both sides we get:

$c = \sqrt{a^2 + b^2}$.

It is this formula that we will calculate in our python script.

## import

In order to us the $\sqrt{}$ function we need to import it from the standard math library. To do this we use the `from` and `import` keywords. Always put your imports at the very TOP of your script.

```python
from math import sqrt
# Extra stuff will come later
```

## Define the legs

Next we will add in two variables and values to represent the legs of the triangle.

```python
from math import sqrt

a = 3
b = 4
```

## Calculate the hypotenuse

Next, we calculate the value of the hypotenuse and then print the value.

```python
from math import sqrt

a = 3
b = 4
c = sqrt(a**2 + b**2)
print("The hypotenuse is: ", c)
```

And there you go! Now, here is an extra challenge for you.

**Is there a way to get the user to enter their own values for a and b into the program and calculate the value of the hypotenuse
based off of these values? This is left to you to research on your own.**
