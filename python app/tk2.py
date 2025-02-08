import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    repeat_password = repeat_password_entry.get()

    if not username or not password or not repeat_password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    if password != repeat_password:
        messagebox.showerror("Password Error", "Passwords do not match.")
        return

    messagebox.showinfo("Login Successful", f"Welcome, {username}!")

def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    repeat_password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x300")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Login", font=("Arial", 18), fg="#333", bg="#f0f0f0")
title_label.pack(pady=10)

# Username Label and Entry
username_label = tk.Label(root, text="Username", bg="#f0f0f0")
username_label.pack(pady=(10, 0))
username_entry = tk.Entry(root, width=30, bd=2, relief="solid")
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password", bg="#f0f0f0")
password_label.pack(pady=(10, 0))
password_entry = tk.Entry(root, show="*", width=30, bd=2, relief="solid")
password_entry.pack(pady=5)

# Repeat Password Label and Entry
repeat_password_label = tk.Label(root, text="Repeat Password", bg="#f0f0f0")
repeat_password_label.pack(pady=(10, 0))
repeat_password_entry = tk.Entry(root, show="*", width=30, bd=2, relief="solid")
repeat_password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", bg="#4CAF50", fg="white", width=30, command=login)
login_button.pack(pady=(20, 5))

# Reset Button
reset_button = tk.Button(root, text="Reset", bg="#f44336", fg="white", width=30, command=reset)
reset_button.pack(pady=5)

# Run the application
root.mainloop()
