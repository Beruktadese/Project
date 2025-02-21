import tkinter as tk
from tkinter import ttk, messagebox

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
        tk.Button(self.content_frame, text="Ceremony").pack(pady=5)
        tk.Button(self.content_frame, text="Donate Now", command=self.open_donation_form).pack(pady=5)
        tk.Button(self.content_frame, text="Donate Food", command=self.open_donation_form).pack(pady=5)

    def open_donation_form(self):
        DonationApp(self.root, self.open_food_donation)

    def open_food_donation(self):
        FoodMenuApp(tk.Toplevel(self.root))

    def show_membership(self):
        membership_form = tk.Toplevel(self.root)
        membership_form.title("Membership Registration")
        membership_form.geometry("400x500")

        tk.Label(membership_form, text="Register", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(membership_form, text="Please fill in this form to become a member.").pack()

    def show_login(self):
        tk.Label(self.content_frame, text="Login", font=("Arial", 16)).pack()

        tk.Label(self.content_frame, text="Username:").pack()
        username_entry = tk.Entry(self.content_frame)
        username_entry.pack()

        tk.Label(self.content_frame, text="Password:").pack()
        password_entry = tk.Entry(self.content_frame, show="*")
        password_entry.pack()

        tk.Button(self.content_frame, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get())).pack(pady=5)

    def login(self, username, password):
        if username and password:
            messagebox.showinfo("Login", "Login Successful!")
        else:
            messagebox.showerror("Error", "Please enter valid credentials")


class DonationApp:
    def __init__(self, root, callback):
        self.root = tk.Toplevel(root)
        self.root.title("Donation Form")
        self.root.geometry("400x500")
        self.callback = callback

        tk.Label(self.root, text="THIS HOME PAGE FOR DONATION FOR NOW", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self.root, text="Where would you like to donate?", font=("Arial", 10, "bold")).pack()
        self.country_var = tk.StringVar()
        self.country_dropdown = ttk.Combobox(self.root, textvariable=self.country_var, state="readonly", values=["Addis Ababa", "Dire Dawa", "Debre Berhan", "Adama", "Hawasa"])
        self.country_dropdown.pack(pady=5)
        
        tk.Label(self.root, text="From which organization?", font=("Arial", 10, "bold")).pack()
        self.org_var = tk.StringVar()
        self.org_dropdown = ttk.Combobox(self.root, textvariable=self.org_var, state="readonly", values=["Habesha Agerawian", "Meqodonia", "Tefenakay", "Other"])
        self.org_dropdown.pack(pady=5)
        
        tk.Label(self.root, text="What would you like to order?", font=("Arial", 10, "bold")).pack()
        self.item_var = tk.StringVar()
        self.item_dropdown = ttk.Combobox(self.root, textvariable=self.item_var, state="readonly", values=["Meals", "Materials"])
        self.item_dropdown.pack(pady=5)
        
        tk.Label(self.root, text="Choose a hotel?", font=("Arial", 10, "bold")).pack()
        self.hotel_var = tk.StringVar()
        self.hotel_dropdown = ttk.Combobox(self.root, textvariable=self.hotel_var, state="readonly", values=["Bernos", "Janhoy", "Sunshine"])
        self.hotel_dropdown.pack(pady=5)
        
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_form)
        submit_button.pack(pady=10)

    def submit_form(self):
        if not all([self.country_var.get(), self.org_var.get(), self.item_var.get(), self.hotel_var.get()]):
            messagebox.showerror("Error", "Please fill in all fields")
        else:
            messagebox.showinfo("Submission Successful", "Thank you for your donation!")
            self.root.destroy()
            self.callback()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraceApp(root)
    root.mainloop()
