#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters = ""
random_symbol = ""
random_numbers= ""
for x in range(0,nr_letters):
    rand_indx = random.randrange(len(letters))
    random_letters = letters[rand_indx] + random_letters
for y in range(0,nr_symbols):
    rand_indx = random.randrange(len(symbols))
    random_symbol = symbols[rand_indx] + random_symbol
for z in range(0,nr_numbers):
    rand_indx = random.randrange(len(numbers))
    random_numbers = numbers[rand_indx] + random_numbers

print(random_letters+random_symbol+random_numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password=""
password_list = []

for x in range(0,nr_letters):
   password_list += random.choice(letters)
for y in range(0,nr_symbols):
    password_list += random.choice(symbols)
for z in range(0,nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

for char in password_list:
    password+=char
print(password)