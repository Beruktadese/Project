import tkinter as tk
from tkinter import ttk, messagebox

class FoodMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Menu")
        self.root.geometry("600x500")
        
        self.menu_items = [
            ("Tebs", 300),
            ("Shiro", 70),
            ("Pasta", 80),
            ("Aynet", 70),
            ("Juice", 80),
            ("Water", 30),
            ("Kurt", 550),
            ("Kitfo", 700)
        ]
        
        self.cart = {}
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Welcome to Our Food Menu", font=("Arial", 16)).pack(pady=10)
        
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()
        
        for item, price in self.menu_items:
            frame = tk.Frame(self.menu_frame)
            frame.pack(fill=tk.X, pady=5)
            
            tk.Label(frame, text=f"{item} - {price} birr", width=20, anchor="w").pack(side=tk.LEFT)
            qty_var = tk.IntVar(value=1)
            qty_entry = tk.Entry(frame, textvariable=qty_var, width=5)
            qty_entry.pack(side=tk.LEFT)
            order_btn = tk.Button(frame, text="Order", command=lambda i=item, p=price, q=qty_var: self.add_to_cart(i, p, q))
            order_btn.pack(side=tk.LEFT)
        
        self.checkout_btn = tk.Button(self.root, text="Proceed to Payment", command=self.open_payment_form, state=tk.DISABLED)
        self.checkout_btn.pack(pady=10)
    
    def add_to_cart(self, item, price, qty_var):
        qty = qty_var.get()
        if qty > 0:
            self.cart[item] = (price, qty)
            messagebox.showinfo("Added", f"{qty} x {item} added to cart")
            self.checkout_btn.config(state=tk.NORMAL)
    
    def open_payment_form(self):
        self.payment_window = tk.Toplevel(self.root)
        self.payment_window.title("Payment Form")
        self.payment_window.geometry("400x300")
        
        tk.Label(self.payment_window, text="Enter Payment Information", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.payment_window, text="Select Hotel Account:").pack()
        self.hotel_var = tk.StringVar()
        self.hotel_dropdown = ttk.Combobox(self.payment_window, textvariable=self.hotel_var, state="readonly", values=[
            "Hotel Account CBE 100143567",
            "Hotel Account Abisiniya 0148285",
            "Hotel Account Awash 108527542"
        ])
        self.hotel_dropdown.pack()
        
        tk.Label(self.payment_window, text="Your Account Number:").pack()
        self.user_account = tk.Entry(self.payment_window)
        self.user_account.pack()
        
        self.total_amount = sum(price * qty for price, qty in self.cart.values())
        tk.Label(self.payment_window, text=f"Amount to Pay: {self.total_amount} birr").pack()
        
        self.agree_var = tk.IntVar()
        tk.Checkbutton(self.payment_window, text="I agree to the Terms & Conditions", variable=self.agree_var).pack()
        
        tk.Button(self.payment_window, text="Submit Payment", command=self.process_payment).pack(pady=10)
    
    def process_payment(self):
        if not self.hotel_var.get() or not self.user_account.get() or self.agree_var.get() == 0:
            messagebox.showerror("Error", "Please fill out all fields and agree to terms.")
            return
        
        messagebox.showinfo("Payment Successful", "Thank you for your payment. Your transaction is complete!")
        self.payment_window.destroy()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodMenuApp(root)
    root.mainloop()