import tkinter as tk
from tkinter import ttk
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
    reminder_label.config(text="Remember to change your password in 4-5 days.")

def copy_to_clipboard():
    password = output.get("1.0", 'end-1c')
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()  # Now it stays on the clipboard after the window is closed

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.configure(bg='black')

# Style configuration
style = ttk.Style()
style.configure("TButton", foreground="black", background="white")

# Create a Text widget to display the password
output = tk.Text(window, width=50, height=20, wrap=tk.WORD, bg='black', fg='white')
output.pack()

# Create a button to generate and display the password
generate_button = ttk.Button(window, text="Generate Password", command=display_password)
generate_button.pack()

# Create a button to copy the password to clipboard
copy_button = ttk.Button(window, text="Copy", command=copy_to_clipboard)
copy_button.pack()

# Create a label for the reminder
reminder_label = tk.Label(window, text="", bg='black', fg='white')
reminder_label.pack()

# Run the Tkinter event loop
window.mainloop()
