import tkinter as tk
from tkinter import messagebox

class GraceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grace Platform")
        self.root.geometry("800x600")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="lightblue", pady=10)
        header.pack(fill=tk.X)
        
        title = tk.Label(header, text="Welcome to Grace", font=("Arial", 20), bg="lightblue")
        title.pack()
        
        nav_frame = tk.Frame(header, bg="lightblue")
        nav_frame.pack()
        
        for text in ["Home", "About Us", "How It Works", "Donate", "Login"]:
            btn = tk.Button(nav_frame, text=text, command=lambda t=text: self.navigate(t))
            btn.pack(side=tk.LEFT, padx=5)
        
        # Main Content
        self.content_frame = tk.Frame(self.root, padx=10, pady=10)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        self.show_home()
    
    def navigate(self, section):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        if section == "Home":
            self.show_home()
        elif section == "About Us":
            self.show_about()
        elif section == "How It Works":
            self.show_how_it_works()
        elif section == "Donate":
            self.show_donate()
        elif section == "Login":
            self.show_login()
    
    def show_home(self):
        tk.Label(self.content_frame, text="GRACE (Giving Relief and Care Everywhere)", font=("Arial", 16)).pack()
        tk.Label(self.content_frame, text="The online system for charity management...", wraplength=600, justify="left").pack()
    
    def show_about(self):
        tk.Label(self.content_frame, text="About Us", font=("Arial", 16)).pack()
        tk.Label(self.content_frame, text="Grace is a platform bridging donors and beneficiaries...", wraplength=600, justify="left").pack()
    
    def show_how_it_works(self):
        tk.Label(self.content_frame, text="How It Works", font=("Arial", 16)).pack()
        tk.Label(self.content_frame, text="The platform connects donors, businesses, and beneficiaries...", wraplength=600, justify="left").pack()
    
    def show_donate(self):
        tk.Label(self.content_frame, text="Donate", font=("Arial", 16)).pack()
        tk.Label(self.content_frame, text="Choose an option below to donate:", wraplength=600).pack()
        
        tk.Button(self.content_frame, text="Membership", command=self.show_membership).pack(pady=5)
        tk.Button(self.content_frame, text="Ceremony", command=self.show_ceremony).pack(pady=5)
        tk.Button(self.content_frame, text="Donate Now", command=self.show_donate_now).pack(pady=5)
    
        donate_form = tk.Toplevel(self.root)
        donate_form.title("Donation Form")
        donate_form.geometry("400x400")
        
        tk.Label(donate_form, text="Where would you like to donate?", font=("Arial", 12)).pack()
        country_var = tk.StringVar(donate_form)
        country_menu = tk.OptionMenu(donate_form, country_var, "Addis Ababa", "Dire Dawa", "Debre Berhan", "Adama", "Hawasa")
        country_menu.pack()
        
        tk.Label(donate_form, text="From which organization?", font=("Arial", 12)).pack()
        org_var = tk.StringVar(donate_form)
        org_menu = tk.OptionMenu(donate_form, org_var, "Habesha Agerawian", "Meqodenia", "Tefenakay", "Other")
        org_menu.pack()
        
        tk.Label(donate_form, text="What would you like to order?", font=("Arial", 12)).pack()
        item_var = tk.StringVar(donate_form)
        item_menu = tk.OptionMenu(donate_form, item_var, "Meals", "Materials")
        item_menu.pack()
        
        tk.Label(donate_form, text="Choose hotels", font=("Arial", 12)).pack()
        hotel_var = tk.StringVar(donate_form)
        hotel_menu = tk.OptionMenu(donate_form, hotel_var, "Bernos", "Janhoy", "Sunshine")
        hotel_menu.pack()
        
        tk.Button(donate_form, text="Submit", command=lambda: self.submit_donation(country_var.get(), org_var.get(), item_var.get(), hotel_var.get())).pack(pady=10)
    
    def submit_donation(self, country, organization, item, hotel):
        messagebox.showinfo("Donation Submitted", f"Donation to {organization} in {country} for {item} via {hotel} submitted successfully!")
    
    def show_login(self):
        tk.Label(self.content_frame, text="Login", font=("Arial", 16)).pack()
        
        tk.Label(self.content_frame, text="Username:").pack()
        username_entry = tk.Entry(self.content_frame)
        username_entry.pack()
        
        tk.Label(self.content_frame, text="Password:").pack()
        password_entry = tk.Entry(self.content_frame, show="*")
        password_entry.pack()
        
        tk.Button(self.content_frame, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get())).pack(pady=5)
        tk.Button(self.content_frame, text="Reset", command=lambda: self.reset_entries(username_entry, password_entry)).pack(pady=5)
    
    def login(self, username, password):
        if username and password:
            messagebox.showinfo("Login", "Login Successful!")
        else:
            messagebox.showerror("Error", "Please enter valid credentials")
    
    def reset_entries(self, *entries):
        for entry in entries:
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GraceApp(root)
    root.mainloop()
