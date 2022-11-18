# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lowered = name1.lower()
name2_lowered = name2.lower()

t_count =  name1_lowered.count('t')
r_count = name1_lowered.count('r')
u_count = name1_lowered.count('u')
e_count = name1_lowered.count('e')
l_count = name1_lowered.count('l')
o_count = name1_lowered.count('o')
v_count = name1_lowered.count('v')
e_count = name1_lowered.count('e')



t_count2 =  name2_lowered.count('t')
r_count2 = name2_lowered.count('r')
u_count2 = name2_lowered.count('u')
e_count2 = name2_lowered.count('e')
l_count2 = name2_lowered.count('l')
o_count2 = name2_lowered.count('o')
v_count2 = name2_lowered.count('v')
e_count2 = name2_lowered.count('e')

count = t_count + r_count + u_count +e_count +t_count2 +r_count2 +u_count2+e_count2

count2 = l_count +o_count +v_count +e_count +  l_count2 + o_count2 +v_count2 +e_count2

count1_converted = str(count)
count2_converted = str(count2)

final_score = count1_converted + count2_converted;
final_score_converted = int(final_score)

if final_score_converted < 10 or final_score_converted > 90 :
    print(f"Your score is {final_score_converted}, you go together like coke and mentos.")
elif final_score_converted > 40 and final_score_converted < 50 :
    print(f"Your score is {final_score_converted}, you are alright together.")
else:
    print(f"Your score is {final_score_converted}.")