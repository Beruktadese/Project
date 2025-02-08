import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("400x300")

# Header
header = tk.Label(root, text="Welcome to the GRACE", font=("Arial", 16), pady=10)
header.pack()


# Main content frame
content_frame = tk.Frame(root, padx=20, pady=20)
content_frame.pack(fill='both', expand=True)

# Label
label = tk.Label(content_frame, text="Enter your name:", font=("Arial", 12))
label.grid(row=0, column=0, sticky='w')

# Entry field
name_entry = tk.Entry(content_frame, width=30)
name_entry.grid(row=0, column=1, padx=10)

# Button functionality
def greet():
    name = name_entry.get()
    greeting_label.config(text=f"Hello, {name}!")

# Button
greet_button = tk.Button(content_frame, text="Greet", command=greet)
greet_button.grid(row=1, column=0, columnspan=2, pady=10)

# Greeting label
greeting_label = tk.Label(content_frame, text="", font=("Arial", 12), fg="blue")
greeting_label.grid(row=2, column=0, columnspan=2)

# Footer
footer = tk.Label(root, text="Thank you for using the app", font=("Arial", 10), pady=10)
footer.pack(side="bottom")

# Run the application
root.mainloop()
