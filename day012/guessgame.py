import random
import art

print(art.logo)


# number guessed going to store the number computer guessed
number_guessed = int(random.uniform(1,101))

# checking whether player playing game or not
is_playing = True

# main logic inside the function
def calculation(user_guess,attempt_left):
    if user_guess == number_guessed:
        print(f"you got it! The Number was {user_guess}")
        return False
    elif user_guess > number_guessed and (user_guess-number_guessed) >= 10:
        if attempt == 1:
            print("Out of Guesses, You Lose")
            return False
        else:
            print("Your guess is Too high")
            print("Guess Again")
        return attempt_left - 1
    elif user_guess > number_guessed and (user_guess-number_guessed) <= 10:
        if attempt == 1:
            print("Out of Guesses, You Lose")
            return False
        else:
            print("Your guess is high")
            print("Guess Again")
        return attempt_left - 1
    elif user_guess < number_guessed and (number_guessed-user_guess) >= 10:
        if attempt == 1:
            print("Out of Guesses, You Lose")
            return False
        else:
            print("your guess is Too Low")
            print("Guess Again")
        return attempt_left - 1
    elif user_guess < number_guessed and (number_guessed-user_guess) <=10:
        if attempt == 1:
            print("Out of Guesses, You Lose")
            return False
        else:
            print("your guess is Low")
            print("Guess Again")
        return attempt_left - 1
    else:
        return "Enter Valid Number"

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if user_choice == 'easy':
    attempt = 10
    while is_playing:
     print(f"You have {attempt} remaining to guess the number.")
     user_guess=int(input("Make a guess: "))
     attempt=calculation(user_guess,attempt)
     is_playing = attempt
elif user_choice == 'hard':
    attempt = 5
    while is_playing:
        print(f"You have {attempt} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempt = calculation(user_guess, attempt)
        is_playing = attempt
else:
    print("invalid choice")
    is_playing = False
