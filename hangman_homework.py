from hangman_words import word_list

# Imported the random library to generate random number
import random

# Defining the function


def hangman_game():
    name = input("what is your name?")
    print(f"Hello {name} are you ready to play hangman!")
    # Words are generated randomly from the word_list
    words = word_list
    word = random.choice(words)
    print("Guess the characters")
    guesses = " "
    attempt = 5
    while attempt > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("Congratulations!! You win")
            print("The word is:", word)
            break
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            attempt -= 1
            print("Wrong")
            print(f"You have {attempt} chance left")
            if attempt == 0:
                print("Better luck next time")
                play_again = input("Would you like to play again?(y/n) ")
                if play_again == "y" or play_again == "yes" or play_again == "yeah":
                    hangman_game()
                else:
                    break


hangman_game()
