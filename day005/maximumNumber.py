# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maximumValue = 0
for index in range(0,len(student_scores)):
    if maximumValue <= student_scores[index]:
        maximumValue= student_scores[index]
    else:
        continue

print(f"The highest score in the class is: {maximumValue}")