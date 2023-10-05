import tkinter as tk
from tkinter import messagebox
import string
import secrets

class PasswordGenerator:
    def __init__(self, length=400):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self):
        password = ''.join(secrets.choice(self.characters) for i in range(self.length))
        return password

def display_password():
    generator = PasswordGenerator()
    password = generator.generate()
    output.delete(1.0, tk.END)
    output.insert(tk.END, password)
    messagebox.showinfo("Reminder", "Remember to change your password in 4-5 days.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a Text widget to display the password
output = tk.Text(window, width=50, height=20, wrap=tk.WORD)
output.pack()

# Create a button to generate and display the password
generate_button = tk.Button(window, text="Generate Password", command=display_password)
generate_button.pack()

# Run the Tkinter event loop
window.mainloop()
