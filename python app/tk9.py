import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database Setup
conn = sqlite3.connect('grace_platform.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT,
                    username TEXT,
                    password TEXT,
                    role TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS donations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    country TEXT,
                    organization TEXT,
                    item TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    account_number TEXT,
                    user_account TEXT,
                    amount REAL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_name TEXT,
                    description TEXT,
                    date TEXT,
                    organizer_id INTEGER,
                    FOREIGN KEY(organizer_id) REFERENCES users(id)
                 )''')

conn.commit()

# Global variable to track logged-in user
current_user_id = None
current_user_role = None

# Functions
def register():
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()
    if email and username and password and role:
        cursor.execute("INSERT INTO users (email, username, password, role) VALUES (?, ?, ?, ?)", (email, username, password, role))
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")
        notebook.select(login_frame)
    else:
        messagebox.showwarning("Error", "All fields are required!")

def login():
    global current_user_id, current_user_role
    username = login_username_entry.get()
    password = login_password_entry.get()
    cursor.execute("SELECT id, role FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    if result:
        current_user_id = result[0]
        current_user_role = result[1]
        messagebox.showinfo("Login Successful", f"Welcome, {username} ({current_user_role})!")
        if current_user_role == "Admin":
            notebook.select(admin_frame)
        elif current_user_role == "Donor":
            notebook.select(donation_frame)
        elif current_user_role == "Service Provider":
            notebook.select(event_frame)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def process_payment():
    account_number = account_entry.get()
    user_account = user_account_entry.get()
    amount = amount_entry.get()
    if account_number and user_account and amount:
        cursor.execute("INSERT INTO payments (user_id, account_number, user_account, amount) VALUES (?, ?, ?, ?)", (current_user_id, account_number, user_account, amount))
        conn.commit()
        messagebox.showinfo("Payment Successful", "Your payment has been processed successfully!")
    else:
        messagebox.showwarning("Error", "All fields are required!")

# Main Window
root = tk.Tk()
root.title("Grace Platform")
root.geometry("800x600")
root.configure(bg="#f0f8ff")  # Light blue background

# Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Dashboard", command=lambda: notebook.select(admin_frame))
file_menu.add_command(label="Payments", command=lambda: notebook.select(payment_frame))
file_menu.add_command(label="Donations", command=lambda: notebook.select(donation_frame))
file_menu.add_separator()
file_menu.add_command(label="Logout", command=lambda: notebook.select(login_frame))

# Header
header = tk.Label(root, text="Welcome to Grace Platform", font=("Arial", 24, "bold"), bg="#4a90e2", fg="white", pady=10)
header.pack(fill='x')

# Description
description = tk.Label(root, text="Grace (Giving Relief and Care Everywhere) connects donors, service providers, and beneficiaries to enhance transparency, efficiency, and community engagement.", wraplength=750, justify="center", font=("Arial", 12), bg="#f0f8ff")
description.pack(pady=10)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Registration Tab
reg_frame = tk.Frame(notebook)
notebook.add(reg_frame, text='Register')
tk.Label(reg_frame, text="Email").pack()
email_entry = tk.Entry(reg_frame)
email_entry.pack()
tk.Label(reg_frame, text="Username").pack()
username_entry = tk.Entry(reg_frame)
username_entry.pack()
tk.Label(reg_frame, text="Password").pack()
password_entry = tk.Entry(reg_frame, show="*")
password_entry.pack()
tk.Label(reg_frame, text="Role").pack()
role_var = tk.StringVar()
tk.OptionMenu(reg_frame, role_var, "Admin", "Donor", "Service Provider").pack()
tk.Button(reg_frame, text="Register", command=register).pack(pady=10)

# Login Tab
login_frame = tk.Frame(notebook)
notebook.add(login_frame, text='Login')
tk.Label(login_frame, text="Username").pack()
login_username_entry = tk.Entry(login_frame)
login_username_entry.pack()
tk.Label(login_frame, text="Password").pack()
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.pack()
tk.Button(login_frame, text="Login", command=login).pack(pady=10)

# Admin Frame
admin_frame = tk.Frame(notebook)
notebook.add(admin_frame, text='Admin Dashboard')
tk.Label(admin_frame, text="Admin Controls", font=("Arial", 16)).pack(pady=20)

# Donation Frame
donation_frame = tk.Frame(notebook)
notebook.add(donation_frame, text='Donations')
tk.Label(donation_frame, text="Donor Dashboard", font=("Arial", 16)).pack(pady=20)

# Event Frame
event_frame = tk.Frame(notebook)
notebook.add(event_frame, text='Service Provider Dashboard')
tk.Label(event_frame, text="Service Provider Controls", font=("Arial", 16)).pack(pady=20)

# Payment Frame
payment_frame = tk.Frame(notebook)
notebook.add(payment_frame, text='Payments')
tk.Label(payment_frame, text="Enter Payment Information", font=("Arial", 16)).pack(pady=10)
tk.Label(payment_frame, text="Account Number").pack()
account_entry = tk.Entry(payment_frame)
account_entry.pack()
tk.Label(payment_frame, text="Your Account Number").pack()
user_account_entry = tk.Entry(payment_frame)
user_account_entry.pack()
tk.Label(payment_frame, text="Amount to Pay").pack()
amount_entry = tk.Entry(payment_frame)
amount_entry.pack()
tk.Button(payment_frame, text="Submit Payment", command=process_payment).pack(pady=10)

# Footer
footer = tk.Label(root, text="© 2025 Grace Platform. All Rights Reserved.", font=("Arial", 10), bg="#4a90e2", fg="white", pady=5)
footer.pack(fill='x')

root.mainloop()
