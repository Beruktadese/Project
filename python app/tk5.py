import tkinter as tk
from tkinter import ttk, messagebox

def submit_donation():
    country = country_var.get()
    organization = organization_var.get()
    item = item_var.get()

    if country == "Choose" or organization == "Choose" or item == "Choose":
        messagebox.showwarning("Incomplete Form", "Please select all options before submitting.")
    else:
        messagebox.showinfo("Submission Successful", "Thank you for your donation!")

# Main window
root = tk.Tk()
root.title("Donation Home Page")
root.geometry("400x350")
root.configure(bg="#f4f4f9")

# Title
title_label = tk.Label(root, text="THIS HOME PAGE IS FOR DONATION FOR NOW", font=("Arial", 14, "bold"), bg="#f4f4f9", fg="#333")
title_label.pack(pady=10)

# Country Selection
country_var = tk.StringVar(value="Choose")
tk.Label(root, text="Where would you like to donate?", font=("Arial", 10, "bold"), bg="#f4f4f9").pack(anchor='w', padx=20)
tk.Label(root, text="Choose Country", bg="#f4f4f9").pack(anchor='w', padx=20)

country_dropdown = ttk.Combobox(root, textvariable=country_var, values=["Choose", "Addis Ababa", "Dire Dawa", "Debre Berhan", "Adama", "Hawasa"], state="readonly")
country_dropdown.pack(padx=20, pady=5)

# Organization Selection
organization_var = tk.StringVar(value="Choose")
tk.Label(root, text="For which organization?", font=("Arial", 10, "bold"), bg="#f4f4f9").pack(anchor='w', padx=20)
tk.Label(root, text="Choose Organization", bg="#f4f4f9").pack(anchor='w', padx=20)

organization_dropdown = ttk.Combobox(root, textvariable=organization_var, values=["Choose", "Habesha Agerawian", "Meqodonia", "Tefenakay", "Other"], state="readonly")
organization_dropdown.pack(padx=20, pady=5)

# Items Selection
item_var = tk.StringVar(value="Choose")
tk.Label(root, text="What would you like to donate?", font=("Arial", 10, "bold"), bg="#f4f4f9").pack(anchor='w', padx=20)
tk.Label(root, text="Choose Items", bg="#f4f4f9").pack(anchor='w', padx=20)

items_dropdown = ttk.Combobox(root, textvariable=item_var, values=["Choose", "Meals", "Materials"], state="readonly")
items_dropdown.pack(padx=20, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_donation, bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised")
submit_button.pack(pady=15)

root.mainloop()
