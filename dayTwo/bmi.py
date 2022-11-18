# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
converted_height = float(height)
converted_weight = int(weight)
#Write your code below this line 👇
bmi = converted_weight/(converted_height**2)
print(int(bmi))