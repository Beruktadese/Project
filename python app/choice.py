import tkinter as tk
from tkinter import ttk, messagebox

def submit_donation():
    country = country_var.get()
    organization = organization_var.get()
    item = item_var.get()
    hotel = hotel_var.get()
    
    if country and organization and item and hotel:
        messagebox.showinfo("Donation Submitted", f"You have chosen to donate {item} via {hotel} to {organization} in {country}.")
    else:
        messagebox.showerror("Error", "Please select all fields before submitting.")

root = tk.Tk()
root.title("Donation Page")
root.geometry("400x400")

# Title
title_label = tk.Label(root, text="THIS HOME PAGE IS FOR DONATION", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Country Selection
tk.Label(root, text="Where would you like to donate?").pack()
country_var = tk.StringVar()
country_menu = ttk.Combobox(root, textvariable=country_var, values=["Addis Ababa", "Dire Dawa", "Debre Berhan", "Adama", "Hawasa"], state="readonly")
country_menu.pack()

# Organization Selection
tk.Label(root, text="From which organization?").pack()
organization_var = tk.StringVar()
organization_menu = ttk.Combobox(root, textvariable=organization_var, values=["Habesha Agerawian", "Meqodenia", "Tefenakay", "Other"], state="readonly")
organization_menu.pack()

# Item Selection
tk.Label(root, text="What would you like to order?").pack()
item_var = tk.StringVar()
item_menu = ttk.Combobox(root, textvariable=item_var, values=["Meals", "Materials"], state="readonly")
item_menu.pack()

# Hotel Selection
tk.Label(root, text="Choose hotels?").pack()
hotel_var = tk.StringVar()
hotel_menu = ttk.Combobox(root, textvariable=hotel_var, values=["Bernos", "Janhoy", "Sunshine"], state="readonly")
hotel_menu.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_donation)
submit_button.pack(pady=10)

root.mainloop()
