import random

words = ["python", "coding", "programming", "computer", "science", "engineering"]
word = random.choice(words)
guesses = ''
turns = 6

def display_hangman(word):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

while turns > 0:
    current_word = display_hangman(word)
    print("Word:", current_word)
    print("Guesses:", guesses)

    guess = input("Guess a letter: ")

    if guess in guesses:
        print("You already guessed that letter. Try again.")
    elif guess in word:
        guesses += guess
        print("Good job!")
    else:
        turns -= 1
        print("Incorrect. You have", turns, "turns left.")

    if current_word == word:
        print("Congratulations, you won!")
        break

if turns == 0:
    print("You ran out of turns. The word was:", word)