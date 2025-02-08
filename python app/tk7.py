import tkinter as tk
from tkinter import messagebox

# Function to simulate payment processing
def process_payment():
    hotel_account = hotel_account_var.get()
    user_account = user_account_entry.get()
    amount = amount_entry.get()

    if hotel_account and user_account and amount:
        payment_frame.pack_forget()
        success_frame.pack(pady=20)
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Main window
root = tk.Tk()
root.title("Payment Form")
root.geometry("400x400")

# Payment Form Frame
payment_frame = tk.Frame(root)
payment_frame.pack(pady=20)

# Event Organization Account Number Selection
tk.Label(payment_frame, text="Select Event Organization Account Number:").pack()
hotel_account_var = tk.StringVar()
hotel_account_dropdown = tk.OptionMenu(payment_frame, hotel_account_var, "", "Account CBE 100134875", "Account Abisinya 01247843", "Account Awash 100378686")
hotel_account_dropdown.pack(pady=5)

# User's Account Number
tk.Label(payment_frame, text="Your Account Number:").pack()
user_account_entry = tk.Entry(payment_frame)
user_account_entry.pack(pady=5)

# Payment Amount
tk.Label(payment_frame, text="Amount to Pay:").pack()
amount_entry = tk.Entry(payment_frame)
amount_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(payment_frame, text="Submit Payment", command=process_payment)
submit_button.pack(pady=10)

# Success Message Frame
success_frame = tk.Frame(root)
tk.Label(success_frame, text="Payment Successful!", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(success_frame, text="Thank you for your payment. Your transaction is complete!\nWe will send you the receipt.", wraplength=300, justify="center").pack()

root.mainloop()
