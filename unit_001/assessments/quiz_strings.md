# Python Strings Quiz  
**Topics:** Immutability, `.strip()`, `.upper()`, and Slicing  
**Level distribution:** 14 Beginner • 6 Intermediate  
**Instructions:** Choose the single best answer unless otherwise stated.

### Beginner Level (Questions 1–14)

1. What does it mean that strings in Python are **immutable**?  
   A) Strings can be changed after creation using index assignment  
   B) Once created, the content of a string cannot be modified  
   C) Strings are automatically deleted when not used  
   D) Strings can only contain letters, not numbers  

2. Which line of code will raise an error?  
   A) `s = "hello"; s = "hi"`  
   B) `s = "hello"; s += " world"`  
   C) `s = "hello"; s[0] = "H"`  
   D) `s = "hello"; print(s.upper())`  

3. What is printed by this code?  
   ```python
   a = "python"
   b = a
   a = a.upper()
   print(b)
   ```  
   A) PYTHON  
   B) python  
   C) error  
   D) nothing  

4. What does the `.strip()` method do by default?  
   A) Removes all spaces inside the string  
   B) Converts the string to uppercase  
   C) Removes whitespace from the beginning and end of the string  
   D) Splits the string into a list  

5. What is the result of `"   hello world   ".strip()`?  
   A) `"hello world"`  
   B) `"helloworld"`  
   C) `"   hello world"`  
   D) error  

6. Which characters are removed by `.strip()` by default?  
   A) Only space characters `" "`  
   B) Only newline characters `\n`  
   C) Whitespace characters (spaces, tabs, newlines, etc.)  
   D) All vowels  

7. What does `"Hello".upper()` return?  
   A) `"hello"`  
   B) `"HELLO"`  
   C) `"Hello"`  
   D) error  

8. Does `.upper()` change the original string?  
   A) Yes, it modifies the string in place  
   B) No, it returns a new string  
   C) It depends on the length of the string  
   D) It only works on lowercase strings  

9. What is the result of `"python"[0]`?  
   A) `"p"`  
   B) `"python"`  
   C) `0`  
   D) error  

10. What does `"programming"[2:6]` return?  
    A) `"ogr"`  
    B) `"ogra"`  
    C) `"ogramm"`  
    D) `"pro"`  

11. What is `"hello"[-1]`?  
    A) `"h"`  
    B) `"o"`  
    C) error  
    D) `""` (empty string)  

12. What does `"abcdefgh"[1:7:2]` return?  
    A) `"bdf"`  
    B) `"bdef"`  
    C) `"aceg"`  
    D) `"bcdefg"`  

13. Which expression returns `"PYTHON"`?  
    A) `"python".strip().upper()`  
    B) `" PYTHON ".upper()`  
    C) `" PYTHON ".strip().upper()`  
    D) Both A and C  

14. What is the result of this code?  
    ```python
    s = "   data   "
    print(s.strip() == "data")
    ```  
    A) `False`  
    B) `True`  
    C) error  
    D) `"   data   "`  

### Intermediate Level (Questions 15–20)

15. What is printed by the following code?  
    ```python
    s = "test"
    t = s
    s = s.strip() + "ing"
    print(t)
    ```  
    A) `testing`  
    B) `test`  
    C) ` testing `  
    D) error  

16. Which of these lines **will raise an error**? (select one)  
    A) `"hello"[::2] = "Hi"`  
    B) `s = "hi"; s += "!"`  
    C) `"hello".upper()`  
    D) `print("data".strip("ad"))`  

17. What does `"   x   y   z   ".strip(" xyz")` return?  
    A) `""` (empty string)  
    B) `"x y z"`  
    C) `"   "`  
    D) error  

18. What is the result of this slicing?  
    ```python
    word = "supercalifragilistic"
    print(word[-7:-1])
    ```  
    A) `stic`  
    B) `istic`  
    C) `listi`  
    D) `gilist`  

19. After running this code, what is the value of `a`?  
    ```python
    a = "  PYTHON  "
    a = a.strip().lower().upper()
    ```  
    A) `"  PYTHON  "`  
    B) `"python"`  
    C) `"PYTHON"`  
    D) error  

20. Which statement is **false** about string immutability and methods?  
    A) `s.replace("a", "b")` creates a new string  
    B) `s.upper()` modifies the original string in place  
    C) Attempting `s[3] = "x"` raises a TypeError  
    D) Concatenation with `+` or `+=` creates new string object(s)  

---

**End of Quiz**
