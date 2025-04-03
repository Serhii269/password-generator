import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_click():
    try:
        length = int(password_length_entry.get())
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6 characters.")
            return
        generated_password = generate_password(length)
        password_label.config(text=f"Generated Password: {generated_password}")
        global password_to_copy
        password_to_copy = generated_password
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for password length.")

def copy_to_clipboard():
    try:
        w.clipboard_clear()
        w.clipboard_append(password_to_copy)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while copying: {str(e)}")

w = tk.Tk()
w.title("Password Generator")
w.geometry("400x250")
w.config(bg="red")

prompt_label = tk.Label(w, text="Enter the desired password length:", bg="red", fg="black", font=("Arial", 15))
prompt_label.pack(pady=10)

password_length_entry = tk.Entry(w, font=("Arial", 12), width=10)
password_length_entry.pack(pady=5)

generate_button = tk.Button(w, text="Generate Password", command=on_generate_click, bg="white", fg="black", font=("Arial", 12))
generate_button.pack(pady=10)

password_label = tk.Label(w, text="Generated Password: ", bg="white", fg="black", font=("Arial", 12))
password_label.pack(pady=10)

copy_button = tk.Button(w, text="Copy to Clipboard", command=copy_to_clipboard, bg="white", fg="black", font=("Arial", 12))
copy_button.pack(pady=10)

password_to_copy = ""

w.mainloop()

