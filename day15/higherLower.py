import random
import art
import gameData

user_choice=''
score=0
data = gameData.data
follower_a=0
follower_b=0

def printing_logo():
    print(art.logo)

def printing_vs():
    print(art.vs)

def main_logic(random_one,random_two):
    printing_logo()
    print(f"Compare A: {data[random_one]['name']}, a {data[random_one]['description']}, from {data[random_one]['country']}")
    printing_vs()
    print(f"Compare B: {data[random_two]['name']}, a {data[random_two]['description']}, from {data[random_two]['country']}")
    user_choice=input("Who has more follower? Type 'A' or 'B': ")
    return user_choice



def score_checking(follower_one,follower_two):
    if follower_one > follower_two and user_choice == 'A':
        return True
    elif follower_two > follower_one and user_choice == 'B':
        return True
    else:
        return False

def playing():
    is_playing = True
    global score
    global user_choice
    global follower_b
    global follower_a

    while is_playing:
        random_number_one = random.randrange(0, len(gameData.data))
        random_number_two = random.randrange(0, len(gameData.data))
        user_choice=main_logic(random_number_one,random_number_two)
        follower_a = data[random_number_one]['follower_count']
        follower_b = data[random_number_two]['follower_count']
        if score_checking(follower_a,follower_b):
            score+=1
            print(f"You're right! current score: {score}")
            is_playing = True
        else:
            printing_logo()
            print(f"Sorry, that's wrong. Final Score: {score}")
            is_playing = False

playing()