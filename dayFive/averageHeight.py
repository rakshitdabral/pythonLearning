# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = int(0)
for index in range(0,len(student_heights)):
  sum = sum + student_heights[index]


average = round(sum/len(student_heights))
print(average)