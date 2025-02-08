import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import bcrypt

# Database Setup (No changes needed here)
def create_tables():
    # ... (same as before)

create_tables()

# Global variables (No changes needed here)
current_user_id = None
current_user_role = None

# Password Hashing (No changes needed here)
def hash_password(password):
    # ... (same as before)

def verify_password(hashed_password, input_password):
    # ... (same as before)

# Functions (Modified for relationship handling)
def register():
    # ... (same as before)

def login():
    # ... (same as before)

def logout():
    # ... (same as before)

def process_payment():
    # ... (same as before)

def make_donation():
    if current_user_id is None:
        messagebox.showwarning("Error", "You must be logged in to make a donation.")
        return

    country = donation_country_entry.get()
    organization = donation_org_entry.get()
    item = donation_item_entry.get()

    if country and organization and item:
        try:
            with sqlite3.connect('grace_platform.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO donations (user_id, country, organization, item) VALUES (?, ?, ?, ?)",
                               (current_user_id, country, organization, item))
                conn.commit()
                messagebox.showinfo("Donation Successful", "Thank you for your donation!")
                # Clear donation entries after successful donation
                donation_country_entry.delete(0, tk.END)
                donation_org_entry.delete(0, tk.END)
                donation_item_entry.delete(0, tk.END)
        except Exception as e:  # Catch potential errors (e.g., database issues)
            messagebox.showerror("Error", f"Donation failed: {e}")
    else:
        messagebox.showwarning("Error", "All donation fields are required!")


def create_event():  # For Service Providers
    if current_user_id is None or current_user_role != "Service Provider":
        messagebox.showwarning("Error", "You must be a logged-in Service Provider to create an event.")
        return

    event_name = event_name_entry.get()
    description = event_description_entry.get()
    date = event_date_entry.get()

    if event_name and description and date:
        try:
            with sqlite3.connect('grace_platform.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO events (event_name, description, date, organizer_id) VALUES (?, ?, ?, ?)",
                               (event_name, description, date, current_user_id))  # Link to current user
                conn.commit()
                messagebox.showinfo("Event Created", "Your event has been created successfully!")
                # Clear event entries
                event_name_entry.delete(0, tk.END)
                event_description_entry.delete(0, tk.END)
                event_date_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Event creation failed: {e}")
    else:
        messagebox.showwarning("Error", "All event fields are required!")


# Main Window (Modified for Donation and Event inputs)
root = tk.Tk()
# ... (rest of the window setup - title, geometry, background, etc. - same as before)

# Menu Bar (No changes needed here)
# ...

# Header and Description (No changes needed here)
# ...


# Notebook (Modified for Donation and Event frames)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# ... (Registration and Login frames - same as before)


# Admin Frame (No changes needed here for this example)
admin_frame = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(admin_frame, text='Admin Dashboard')
# ... (Add admin controls as needed)


# Donation Frame (Modified)
donation_frame = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(donation_frame, text='Donations')
tk.Label(donation_frame, text="Make a Donation", font=("Arial", 16), bg="#f0f8ff").pack(pady=10)

tk.Label(donation_frame, text="Country", bg="#f0f8ff").pack()
donation_country_entry = tk.Entry(donation_frame)
donation_country_entry.pack(pady=5)

tk.Label(donation_frame, text="Organization", bg="#f0f8ff").pack()
donation_org_entry = tk.Entry(donation_frame)
donation_org_entry.pack(pady=5)

tk.Label(donation_frame, text="Item", bg="#f0f8ff").pack()
donation_item_entry = tk.Entry(donation_frame)
donation_item_entry.pack(pady=5)


tk.Button(donation_frame, text="Donate", command=make_donation, bg="#4a90e2", fg="white").pack(pady=10)


# Event Frame (Modified)
event_frame = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(event_frame, text='Service Provider Dashboard')
tk.Label(event_frame, text="Create Event", font=("Arial", 16), bg="#f0f8ff").pack(pady=10)

tk.Label(event_frame, text="Event Name", bg="#f0f8ff").pack()
event_name_entry = tk.Entry(event_frame)
event_name_entry.pack(pady=5)

tk.Label(event_frame, text="Description", bg="#f0f8ff").pack()
event_description_entry = tk.Entry(event_frame)
event_description_entry.pack(pady=5)

tk.Label(event_frame, text="Date (YYYY-MM-DD)", bg="#f0f8ff").pack()  # Added date format hint
event_date_entry = tk.Entry(event_frame)
event_date_entry.pack(pady=5)

tk.Button(event_frame, text="Create Event", command=create_event, bg="#4a90e2", fg="white").pack(pady=10)

# Payment Frame (No changes needed here)
# ...

# Footer (No changes needed here)
# ...

root.mainloop()