import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        messagebox.showinfo("Login", f"Welcome, {username}!")
    else:
        messagebox.showwarning("Login Failed", "Please enter both username and password.")

# Function to reset fields
def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("400x300")
root.configure(bg='lightgrey')

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

# Create a frame to mimic the form section
form_frame = tk.Frame(root, bg='white', padx=30, pady=30, bd=1, relief=tk.SOLID)
form_frame.place(relx=0.5, rely=0.5, anchor='center')

# Title Label
title_label = tk.Label(form_frame, text="Login", font=("Arial", 18), fg="#333", bg="white")
title_label.pack(pady=(0, 10))

# Username Label and Entry
username_label = tk.Label(form_frame, text="Username", bg="white")
username_label.pack(anchor='w')
username_entry = tk.Entry(form_frame, width=30, bd=1, relief=tk.SOLID)
username_entry.pack(pady=(0, 10))

# Password Label and Entry
password_label = tk.Label(form_frame, text="Password", bg="white")
password_label.pack(anchor='w')
password_entry = tk.Entry(form_frame, show="*", width=30, bd=1, relief=tk.SOLID)
password_entry.pack(pady=(0, 10))

# Login Button
login_button = tk.Button(form_frame, text="Login", bg="#0de014", fg="white", width=25, command=login)
login_button.pack(pady=(5, 5))

# Reset Button
reset_button = tk.Button(form_frame, text="Reset", bg="#0c09ce", fg="white", width=25, command=reset)
reset_button.pack(pady=(5, 5))

# Run the application
root.mainloop()

