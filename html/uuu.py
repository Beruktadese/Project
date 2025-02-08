import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Database connection
def connect_db():
    conn = sqlite3.connect('donor_management.db')
    return conn

# Create tables if they don't exist
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS donor (
        donor_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        password TEXT,
        username TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Business (
        business_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT,
        address TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Charity (
        charity_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bank_System (
        bank_id INTEGER PRIMARY KEY,
        bank_name TEXT NOT NULL,
        account_number TEXT,
        balance INTEGER
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transaction (
        trans_id INTEGER PRIMARY KEY,
        donor_id INTEGER NOT NULL,
        business_id INTEGER NOT NULL,
        charity_id INTEGER NOT NULL,
        bank_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        amount INTEGER NOT NULL,
        FOREIGN KEY (donor_id) REFERENCES donor(donor_id),
        FOREIGN KEY (business_id) REFERENCES Business(business_id),
        FOREIGN KEY (charity_id) REFERENCES Charity(charity_id),
        FOREIGN KEY (bank_id) REFERENCES Bank_System(bank_id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Beneficiary (
        beneficiary_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        charity_id INTEGER NOT NULL,
        FOREIGN KEY (charity_id) REFERENCES Charity(charity_id)
    )''')

    conn.commit()
    conn.close()

# Function to add a donor
def add_donor():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO donor (name, email, phone, address, password, username)
    VALUES (?, ?, ?, ?, ?, ?)''', (entry_donor_name.get(), entry_donor_email.get(), entry_donor_phone.get(), entry_donor_address.get(), entry_donor_password.get(), entry_donor_username.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Donor added successfully!")
    clear_donor_entries()

# Function to clear donor entries
def clear_donor_entries():
    entry_donor_name.delete(0, tk.END)
    entry_donor_email.delete(0, tk.END)
    entry_donor_phone.delete(0, tk.END)
    entry_donor_address.delete(0, tk.END)
    entry_donor_password.delete(0, tk.END)
    entry_donor_username.delete(0, tk.END)

# Function to add a business
def add_business():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Business (name, email, phone, address)
    VALUES (?, ?, ?, ?)''', (entry_business_name.get(), entry_business_email.get(), entry_business_phone.get(), entry_business_address.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Business added successfully!")
    clear_business_entries()

# Function to clear business entries
def clear_business_entries():
    entry_business_name.delete(0, tk.END)
    entry_business_email.delete(0, tk.END)
    entry_business_phone.delete(0, tk.END)
    entry_business_address.delete(0, tk.END)

# Function to add a charity
def add_charity():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Charity (name, email, phone, address)
    VALUES (?, ?, ?, ?)''', (entry_charity_name.get(), entry_charity_email.get(), entry_charity_phone.get(), entry_charity_address.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Charity added successfully!")
    clear_charity_entries()

# Function to clear charity entries
def clear_charity_entries():
    entry_charity_name.delete(0, tk.END)
    entry_charity_email.delete(0, tk.END)
    entry_charity_phone.delete(0, tk.END)
    entry_charity_address.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Donor Management System")

# Donor Management
tk.Label(root, text="Donor Management").grid(row=0, columnspan=2)

tk.Label(root, text="Name").grid(row=1, column=0)
entry_donor_name = tk.Entry(root)
entry_donor_name.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
entry_donor_email = tk.Entry(root)
entry_donor_email.grid(row=2, column=1)

tk.Label(root, text="Phone").grid(row=3, column=0)
entry_donor_phone = tk.Entry(root)
entry_donor_phone.grid(row=3, column=1)

tk.Label(root, text="Address").grid(row=4, column=0)
entry_donor_address = tk.Entry(root)
entry_donor_address.grid(row=4, column=1)

tk.Label(root, text="Password").grid(row=5, column=0)
entry_donor_password = tk.Entry(root, show='*')
entry_donor_password.grid(row=5, column=1)

tk.Label(root, text="Username").grid(row=6, column=0)
entry_donor_username = tk.Entry(root)
entry_donor_username.grid(row=6, column=1)

# Add donor button
button_add_donor = tk.Button(root, text="Add Donor", command=add_donor)
button_add_donor.grid(row=7, columnspan=2)

# Business Management
tk.Label(root, text="Business Management").grid(row=8, columnspan=2)

tk.Label(root, text="Business Name").grid(row=9, column=0)
entry_business_name = tk.Entry(root)
entry_business_name.grid(row=9, column=1)

tk.Label(root, text="Business Email").grid(row=10, column=0)
entry_business_email = tk.Entry(root)
entry_business_email.grid(row=10, column=1)

tk.Label(root, text="Business Phone").grid(row=11, column=0)
entry_business_phone = tk.Entry(root)
entry_business_phone.grid(row=11, column=1)

tk.Label(root, text="Business Address").grid(row=12, column=0)
entry_business_address = tk.Entry(root)
entry_business_address.grid(row=12, column=1)

# Add business button
button_add_business = tk.Button(root, text="Add Business", command=add_business)
button_add_business.grid(row=13, columnspan=2)

# Charity Management
tk.Label(root, text="Charity Management").grid(row=14, columnspan=2)

tk.Label(root, text="Charity Name").grid(row=15, column=0)
entry_charity_name = tk.Entry(root)
entry_charity_name.grid(row=15, column=1)

tk.Label(root, text="Charity Email").grid(row=16, column=0)
entry_charity_email = tk.Entry(root)
entry_charity_email.grid(row=16, column=1)

tk.Label(root, text="Charity Phone").grid(row=17, column=0)
entry_charity_phone = tk.Entry(root)
entry_charity_phone.grid(row=17, column=1)

tk.Label(root, text="Charity Address").grid(row=18, column=0)
entry_charity_address = tk.Entry(root)
entry_charity_address.grid(row=18, column=1)

# Add charity button
button_add_charity = tk.Button(root, text="Add Charity", command=add_charity)
button_add_charity.grid(row=19, columnspan=2)

# Initialize the database
create_tables()

# Start the main event loop
root.mainloop()
