from tkinter import *
from tkinter import messagebox
import random
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [random.choice(letters) for _ in range(8)]
    password_symbols = [random.choice(symbols) for _ in range(2)]
    password_numbers = [random.choice(numbers) for _ in range(2)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave Website and Password empty!")
        return

    file_path = os.path.join(os.path.dirname(__file__), "data.txt")

    with open(file_path, "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
Label(text="Website:").grid(row=1, column=0, sticky="e")
Label(text="Email/Username:").grid(row=2, column=0, sticky="e")
Label(text="Password:").grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "umtrss@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
