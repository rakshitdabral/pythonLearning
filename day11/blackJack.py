import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)

your_card = []
computer_card = []

def calculation( number1, number2):
    result = number1 + number2
    return result

def computer_behaviour(computer_score,player_score):
    if player_score > 21:
        return computer_score
    elif computer_score > player_score and computer_score < 21:
        random_number = random.randrange(2)

        if random_number == 0:
            random_number2 = random.randrange(0, 12)

            computer_card.append(cards[random_number2])

            temp_score = computer_score
            length = len(computer_card)
            computer_score = calculation(temp_score, computer_card[length - 1])
            return computer_score
        else:
            return computer_score
    else:
      while computer_score < 21:
       random_number = random.randrange(2)
       if random_number == 0:
         random_number2 = random.randrange(0,12)
         computer_card.append(cards[random_number2])

         temp_score = computer_score
         length = len(computer_card)
         computer_score = calculation(temp_score,computer_card[length-1])

         return computer_score
       else:
           return computer_score

def winner_checking(cpu_score,player_score):
    if int(cpu_score) > 21 and player_score <= 21:
        print("You won")
    elif player_score > 21 and cpu_score <= 21:
        print("Cpu win")
    elif player_score < 21 and cpu_score < 21:
        if player_score > cpu_score:
            print("You Won")
        else:
            print("Cpu Win")
    elif cpu_score == player_score:
        print("Draw")


for i in range(2):
    random_number = random.randrange(0, 12)
    your_card.append(cards[random_number])

current_score = calculation(your_card[0],your_card[1])
print(f"Your Cards: {your_card}, current score: {current_score} ")



for i in range(2):
    random_number = random.randrange(0, 12)
    computer_card.append(cards[random_number])

computer_score = calculation(computer_card[0],computer_card[1])
print(f"Computer first card: {computer_card[0]}")

is_playing = True

while is_playing:
    choice = input("Type 'y' for another card, type 'n' to pass: ")
    if choice == 'y':
        for i in range(1):
            random_number = random.randrange(0, 12)
            your_card.append(cards[random_number])
        items=len(your_card)
        temporary_result = current_score
        new_result= calculation(current_score,your_card[items-1])
        current_score=new_result
        print(f"Your Cards: {your_card}, current score: {new_result} ")
    elif choice == 'n':

        final_score_cpu = computer_behaviour(computer_score,current_score)
        print(f"computer final hand: {computer_card}, final score: {final_score_cpu}")
        winner_checking(final_score_cpu,current_score)
        is_playing =False


