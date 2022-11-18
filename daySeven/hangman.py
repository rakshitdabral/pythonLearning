import random
import hangman_words
import hangman_art


word_list=hangman_words.word_list
end_of_game = False
random_index = random.randrange(0,len(word_list))
chosen_word = word_list[random_index]

print(hangman_art.logo)


lives = 6

display = []


for x in range(0,len(chosen_word)):
    display.append("_")
print(display)



while not end_of_game:
    guess = input("Guess a letter? ").lower()



    print(guess)

    if guess in display:
        print(f"You've already guessed {guess}")


    for y in range(len(chosen_word)):
        if chosen_word[y] == guess:
            display[y] = guess

    if guess not in chosen_word:
        print(f"{guess}, is not in the word")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])
