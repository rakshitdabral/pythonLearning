from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	# ---------------------------- GLOBAL VARIABLES ---------------------------- #
	LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
	           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


	password_letters = [random.choice(LETTERS) for _ in range(random.randint(8,10))]
	password_symbols = [random.choice(LETTERS) for _ in range(random.randint(2,4))]
	password_numbers = [random.choice(LETTERS) for _ in range(random.randint(2,4))]

	password_list  = password_letters + password_symbols + password_numbers
	random.shuffle(password_list)

	password = "".join(password_list)

	password_entry.delete(0, END)
	password_entry.insert(0,password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_save():

		if website_entry.get() == '' or password_entry.get() == '':
			messagebox.showinfo(title="Error", message="Please enter Valid Information")
		else:
			is_ok = messagebox.askokcancel(title=website_entry.get(),
			                               message=f"These are the details Entered: \n Email: {email_entry.get()}"
			                                       f"\n Password: {password_entry.get()}\n Is it ok to save?")
			if is_ok:
				with open("password.txt", "a") as data_file:
					data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ---------------------------- LABELS ------------------------------- #
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ---------------------------- ENTRIES ------------------------------- #
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abcd@gmail.com")
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

# ---------------------------- BUTTONS ------------------------------- #
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30 , command=password_save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()