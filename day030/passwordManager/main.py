from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
		website = website_entry.get()
		email = email_entry.get()
		password = password_entry.get()
		new_data = {
			website : {
				"email": email,
				"password" : password,
			}
		}

		if website_entry.get() == '' or password_entry.get() == '':
			messagebox.showinfo(title="Error", message="Please enter Valid Information")
		else:
				try:
					with open("data.json","r") as data_file:
						data = json.load(data_file)
				except FileNotFoundError:
					with open("data.json", "w") as data_file:
						json.dump(new_data, data_file,indent=4)
				else:
					data.update(new_data)
					with open("data.json", "w") as data_file:
						json.dump(data, data_file,indent=4)
				finally:
					website_entry.delete(0,END)
					password_entry.delete(0,END)

def find_password():

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
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=47)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "abcd@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

# ---------------------------- BUTTONS ------------------------------- #
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30 , command=password_save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search",width=20,command=find_password)
search_button.grid(row=1, column=2, columnspan=2)
window.mainloop()