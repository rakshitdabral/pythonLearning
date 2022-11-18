import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice==0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice ==2:
    print(scissors)
else:
    print("not a valid choice")

print("Computer chose:\n")
cpu_choice = random.randint(0,2)

if cpu_choice==0:
    print(rock)
elif cpu_choice == 1:
    print(paper)
else:
    print(scissors)

if choice ==0:
    if cpu_choice==0:
        print("Draw")
    elif cpu_choice==1:
        print("You lose")
    else:
        print("You won")

if choice ==1:
    if cpu_choice==0:
        print("You Win")
    elif cpu_choice==1:
        print("Draw")
    else:
        print("You lose")

if choice ==2:
    if cpu_choice==0:
        print("You lose")
    elif cpu_choice==1:
        print("You won")
    else:
        print("You lose")
