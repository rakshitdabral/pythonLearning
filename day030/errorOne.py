fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
	if index > len(fruits) :
		print("fruit pie")
	else:
		fruit = fruits[index]
		print(fruit + " pie")

make_pie(4)