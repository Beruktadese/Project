import tkinter as tk
from tkinter import messagebox

# Function to handle registration
def register():
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    repeat_password = repeat_password_entry.get()

    if not email or not username or not password or not repeat_password:
        messagebox.showerror("Error", "All fields are required!")
    elif password != repeat_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

# Main window
root = tk.Tk()
root.title("Register")
root.geometry("400x400")
root.configure(bg="#f4f4f9")

# Form Container
form_frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=1, relief="solid")
form_frame.pack(pady=20, padx=20)

# Title
title_label = tk.Label(form_frame, text="Register", font=("Arial", 20), bg="white")
title_label.pack(pady=10)

# Email
email_label = tk.Label(form_frame, text="Email", bg="white")
email_label.pack()
email_entry = tk.Entry(form_frame, width=30)
email_entry.pack(pady=5)

# Username
username_label = tk.Label(form_frame, text="Username", bg="white")
username_label.pack()
username_entry = tk.Entry(form_frame, width=30)
username_entry.pack(pady=5)

# Password
password_label = tk.Label(form_frame, text="Password", bg="white")
password_label.pack()
password_entry = tk.Entry(form_frame, show="*", width=30)
password_entry.pack(pady=5)

# Repeat Password
repeat_password_label = tk.Label(form_frame, text="Repeat Password", bg="white")
repeat_password_label.pack()
repeat_password_entry = tk.Entry(form_frame, show="*", width=30)
repeat_password_entry.pack(pady=5)

# Register Button
register_button = tk.Button(form_frame, text="Register", command=register, bg="#007bff", fg="white", width=20)
register_button.pack(pady=10)

root.mainloop()
