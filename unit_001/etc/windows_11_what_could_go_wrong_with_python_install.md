# Windows 11 - What Could Go Wrong

If you don’t completely remove the old Python (especially the one from the Microsoft Store) before installing the official version from python.org, Windows 11 gets confused. It still “remembers” the Store version and will secretly use that one sometimes—even though you think you’re using the new one. So when you type `pip install pygame`, the game library gets saved in the *new* Python, but your computer might run your code with the *old* (empty) Python that has no pygame at all.

You’ll see errors like “No module named 'pygame'” even though you just installed it, or your virtual environment (the little sandbox for each project) will point to the wrong Python. Double-clicking a `.py` file might do nothing, and VS Code could keep picking the Store version. All of this happens quietly in the background, making programming feel broken until you do a full clean-up and fresh install.
