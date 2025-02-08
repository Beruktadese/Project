import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database Setup
conn = sqlite3.connect('charity_management.db')
cursor = conn.cursor()

# Creating Tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Donor (
    DonorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Address TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Business (
    BusinessID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Address TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Charity (
    CharityID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Address TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS BankSystem (
    BankID INTEGER PRIMARY KEY AUTOINCREMENT,
    BankName TEXT NOT NULL,
    AccountNumber TEXT NOT NULL,
    Balance DECIMAL(15,2) NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Transaction (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    DonorID INTEGER,
    BusinessID INTEGER,
    CharityID INTEGER NOT NULL,
    BankID INTEGER NOT NULL,
    Date TEXT NOT NULL,
    Amount DECIMAL(15,2) NOT NULL,
    TransactionType TEXT NOT NULL,
    FOREIGN KEY(DonorID) REFERENCES Donor(DonorID),
    FOREIGN KEY(BusinessID) REFERENCES Business(BusinessID),
    FOREIGN KEY(CharityID) REFERENCES Charity(CharityID),
    FOREIGN KEY(BankID) REFERENCES BankSystem(BankID)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Beneficiary (
    BeneficiaryID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    DisabilityType TEXT NOT NULL,
    CharityID INTEGER NOT NULL,
    FOREIGN KEY(CharityID) REFERENCES Charity(CharityID)
)''')

conn.commit()

# GUI Setup
root = tk.Tk()
root.title("Charity Management System")
root.geometry("900x600")

# Tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Donor Registration
frame_donor = tk.Frame(notebook)
notebook.add(frame_donor, text="Donor Registration")

fields = ['Name', 'Email', 'Phone', 'Address']
donor_entries = {}

for field in fields:
    tk.Label(frame_donor, text=field).pack()
    entry = tk.Entry(frame_donor)
    entry.pack()
    donor_entries[field] = entry

def register_donor():
    data = [donor_entries[field].get() for field in fields]
    if all(data):
        cursor.execute("INSERT INTO Donor (Name, Email, Phone, Address) VALUES (?, ?, ?, ?)", data)
        conn.commit()
        messagebox.showinfo("Success", "Donor Registered Successfully")
    else:
        messagebox.showerror("Error", "All fields are required")

btn_register = tk.Button(frame_donor, text="Register Donor", command=register_donor)
btn_register.pack(pady=10)

root.mainloop()
