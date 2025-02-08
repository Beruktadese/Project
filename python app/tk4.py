import tkinter as tk
from tkinter import messagebox

# Function to simulate payment processing
def process_payment():
    hotel_account = hotel_account_var.get()
    user_account = user_account_entry.get()
    amount = amount_entry.get()

    if hotel_account and user_account and amount:
        payment_section.pack_forget()  # Hide payment form
        success_message.pack()         # Show success message
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Main window
root = tk.Tk()
root.title("Payment Details")
root.geometry("400x350")
root.configure(bg='#f4f4f9')

# Payment Section
payment_section = tk.Frame(root, bg='white', padx=20, pady=20, relief=tk.RIDGE, borderwidth=2)
payment_section.pack(pady=20)

# Header
header = tk.Label(payment_section, text="Enter Payment Information", font=("Arial", 16), bg='white')
header.pack(pady=10)

# Hotel Account Number Selection
hotel_account_var = tk.StringVar()
hotel_label = tk.Label(payment_section, text="Select Hotel Account Number:", bg='white')
hotel_label.pack(anchor='w')
hotel_account_menu = tk.OptionMenu(payment_section, hotel_account_var, "", "Hotel Account 1001", "Hotel Account 1002", "Hotel Account 1003")
hotel_account_menu.pack(fill='x', pady=5)

# User's Account Number
user_account_label = tk.Label(payment_section, text="Your Account Number:", bg='white')
user_account_label.pack(anchor='w')
user_account_entry = tk.Entry(payment_section)
user_account_entry.pack(fill='x', pady=5)

# Payment Amount
amount_label = tk.Label(payment_section, text="Amount to Pay:", bg='white')
amount_label.pack(anchor='w')
amount_entry = tk.Entry(payment_section)
amount_entry.pack(fill='x', pady=5)

# Submit Button
submit_button = tk.Button(payment_section, text="Submit Payment", command=process_payment, bg='#007bff', fg='white', padx=10, pady=5)
submit_button.pack(pady=10)

# Success Message (hidden initially)
success_message = tk.Frame(root, bg='#e6ffe6', padx=20, pady=20)
success_label = tk.Label(success_message, text="Payment Successful!", font=("Arial", 16), bg='#e6ffe6', fg='green')
success_label.pack(pady=10)
success_info = tk.Label(success_message, text="Thank you for your payment. Your transaction is complete!", bg='#e6ffe6')
success_info.pack()

# Run the Tkinter loop
root.mainloop()