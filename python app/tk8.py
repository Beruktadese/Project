import tkinter as tk
from tkinter import messagebox

# Function to update the summary
def update_summary():
    summary_details.delete('1.0', tk.END)
    total_price = 0
    selected_ceremony = ceremony_var.get()

    if selected_ceremony in ceremonies:
        total_price += ceremonies[selected_ceremony]
        summary_details.insert(tk.END, f"Ceremony: {selected_ceremony} - {ceremonies[selected_ceremony]} birr\n")

    summary_details.insert(tk.END, "Additional Options:\n")
    for option, var in additional_vars.items():
        if var.get():
            total_price += additional_options[option]
            summary_details.insert(tk.END, f"- {option} - {additional_options[option]} birr\n")

    summary_details.insert(tk.END, f"Total Price: {total_price} birr")

# Function to proceed
def proceed():
    messagebox.showinfo("Proceed", "Thank you for your selection! Proceeding to the next step.")

# Data
ceremonies = {
    "Wedding Ceremony": 75000,
    "Birthday Celebration": 15000,
    "Corporate Event": 20000,
    "Anniversary Celebration": 30000,
    "Graduation": 15000
}

additional_options = {
    "Photography": 5000,
    "Decoration": 7000,
    "Catering": 10000
}

# Main window
root = tk.Tk()
root.title("Ceremony Planner")
root.geometry("400x500")

# Ceremony selection
tk.Label(root, text="Choose a Ceremony", font=('Arial', 14)).pack(pady=10)
ceremony_var = tk.StringVar()

for name in ceremonies:
    tk.Radiobutton(root, text=f"{name} - {ceremonies[name]} birr", variable=ceremony_var, value=name, command=update_summary).pack(anchor='w')

# Additional options
tk.Label(root, text="Additional Options", font=('Arial', 14)).pack(pady=10)
additional_vars = {}

for option in additional_options:
    var = tk.BooleanVar()
    tk.Checkbutton(root, text=f"{option} - {additional_options[option]} birr", variable=var, command=update_summary).pack(anchor='w')
    additional_vars[option] = var

# Summary section
summary_details = tk.Text(root, height=10, width=40)
summary_details.pack(pady=10)

# Proceed button
tk.Button(root, text="Proceed", command=proceed).pack(pady=10)

root.mainloop()
