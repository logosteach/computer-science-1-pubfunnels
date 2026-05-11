import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Social Scene Login")
root.geometry("400x300")  # width x height
root.resizable(False, False)

# Main container with some padding
main_frame = ttk.Frame(root, padding="30 20")
main_frame.pack(expand=True, fill="both")

# Welcome title - centered at the top
title_label = ttk.Label(
    main_frame,
    text="Welcome to the Social Scene!",
    font=("Helvetica", 16, "bold")
)
title_label.pack(pady=(0, 30))  # padding below the title

# Username section
username_frame = ttk.Frame(main_frame)
username_frame.pack(fill="x", pady=10)

ttk.Label(username_frame, text="Username:", width=12, anchor="e").pack(side="left", padx=(0, 10))
username_entry = ttk.Entry(username_frame, width=30)
username_entry.pack(side="left")
username_entry.focus()  # cursor starts here

# Password section
password_frame = ttk.Frame(main_frame)
password_frame.pack(fill="x", pady=10)

ttk.Label(password_frame, text="Password:", width=12, anchor="e").pack(side="left", padx=(0, 10))
password_entry = ttk.Entry(password_frame, width=30, show="*")
password_entry.pack(side="left")

# Submit button
def submit():
    # Just a placeholder - you can add real login logic here
    print(f"Username: {username_entry.get()}")
    print(f"Password: {password_entry.get()}")
    # For demo: show a simple message
    tk.messagebox.showinfo("Submitted", "Login attempt recorded!")

submit_button = ttk.Button(
    main_frame,
    text="Login",
    command=submit,
    width=15
)
submit_button.pack(pady=30)

# Center the window on screen (optional but nice)
root.eval('tk::PlaceWindow . center')

# Start the application
root.mainloop()
