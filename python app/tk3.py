import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def go_back():
    messagebox.showinfo("Redirect", "Redirecting to the first page for sign-in!")
    # You can add code to actually open another window here

# Create the main window
root = tk.Tk()
root.title("Registration Successful")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Create a frame for better layout
frame = tk.Frame(root, bg="#ffffff", bd=2, relief="solid")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Success message
label1 = tk.Label(frame, text="Successfully Registered!", font=("Arial", 16), fg="black", bg="white")
label1.pack(pady=(20, 10))

# Instruction message
label2 = tk.Label(frame, text="Go to the first page and sign in!", font=("Arial", 12), fg="gray", bg="white")
label2.pack(pady=(0, 20))

# Back button
back_button = tk.Button(frame, text="Back", command=go_back, bg="#23a027", fg="white", font=("Arial", 12), padx=20, pady=10, bd=0, relief="ridge")
back_button.pack()

# Run the application
root.mainloop()
