# Lesson 3 – Challenge Problems Solutions  
**The Magnificent Print Function**

Here are clean, minimal solutions that work perfectly when typed directly into the Python Shell.

### Challenge 1 – Exact Verse
```python
>>> print("Psalm 23:1 – The LORD is my shepherd, I shall not want.")
```

### Challenge 2 – No Extra Spaces
```python
>>> print("Bless" + " the" + " LORD," + " O" + " my" + " soul!")
```
or the shorter version:
```python
>>> print("Bless the LORD, O my soul!")
```

### Challenge 3 – Same-Line Verse
```python
>>> print("The LORD is my light", end="")
>>> print(" and my salvation")
```
or
```python
>>> print("The LORD is my light", end=" ")
>>> print("and my salvation")
```

### Challenge 4 – Perfect Cross
```python
>>> print("   |   ")
>>> print("   |   ")
>>> print("-------")
>>> print("   |   ")
>>> print("   |   ")
```
or a one-print version using `\n` is not allowed yet, so the multi-line way above is perfect.

### Challenge 5 – Hallelujah Chorus
```python
>>> print("Christ is risen! " * 7)
```
Result: Christ is risen! Christ is risen! Christ is risen! … (7 times with one space between)

### Challenge 6 – Framed Verse
```python
>>> print("+" * 21)
>>> print("+  The LORD is good  +")
>>> print("+" * 21)
```

### Challenge 7 – Countdown with Drama
```python
>>> print(5, end=" >>> ")
>>> print(4, end=" >>> ")
>>> print(3, end=" >>> ")
>>> print(2, end=" >>> ")
>>> print(1, end=" >>> ")
>>> print("PRAISE HIM!")
```

### Challenge 8 – Growing Praise
```python
>>> print("H")
>>> print("Ha")
>>> print("Hal")
>>> print("Hall")
>>> print("Halle")
>>> print("Hallel")
>>> print("Hallelu")
>>> print("Halleluj")
>>> print("Halleluja")
>>> print("Hallelujah!")
```
Clever one-line version (still allowed in shell): This does use a for loop which you have not learned yet, so if this does not make sense yet, don't worry. :smiley:

```python
>>> for word in ["H","Ha","Hal","Hall","Halle","Hallel","Hallelu","Halleluj","Halleluja","Hallelujah!"]: print(word)
```
But the separate prints above are perfectly fine for this lesson.

### Challenge 9 – Secret Message
```python
>>> print("Jesus", end="")
>>> print("loves", end="")
>>> print("me")
```
Then with spaces:
```python
>>> print("Jesus", end=" ")
>>> print("loves", end=" ")
>>> print("me")
```

### Challenge 10 – Example of a Beautiful Psalm Art Creation
```python
>>> print("✝" * 25)
>>> print("  The LORD is my shepherd  ", end="")
>>> print("Psalm 23")
>>> print("  I shall not want  " * 2)
>>> print("✝" * 25)
>>> print("Created by: [Your Name]")
```

You now have clean, working solutions for every challenge!  
Use these only after students have tried on their own.  
Great job teaching the magnificent `print()`!
