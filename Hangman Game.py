# A code to play the classic Hangman game.
# It selects a random word from a predefined list.
# The user guesses one letter at a time.
# The game ends when the user either guesses the word correctly or makes 6 incorrect guesses.
# It includes input validation and shows guessed letters and remaining attempts.
# The code is written in a clean, structured, and intermediate-friendly way using functions.

import random


WORDS = ["python", "blender", "hangman", "developer", "animation", "wizard", "dragon"]

MAX_ATTEMPTS = 6


def choose_word():
    return random.choice(WORDS)


def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)


def get_valid_input(prompt, guessed_letters):
    while True:
        guess = input(prompt).lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Enter a single alphabet only.")
        elif guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
        else:
            return guess


def hangman():
    print("🎮 Welcome to Hangman!\n")
    word_to_guess = choose_word()
    guessed_letters = set()
    wrong_attempts = 0
    while wrong_attempts < MAX_ATTEMPTS:
        current_display = display_current_state(word_to_guess, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"❗ Attempts left: {MAX_ATTEMPTS - wrong_attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")

        guess = get_valid_input("🔤 Guess a letter: ", guessed_letters)
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("✅ Good guess!")
            if is_word_guessed(word_to_guess, guessed_letters):
                print(f"\n🎉 You won! The word was: {word_to_guess}")
                return
        else:
            print("❌ Not in the word.")
            wrong_attempts += 1


    print(f"\n💀 You lost! The word was: {word_to_guess}")


if __name__ == "__main__":
    hangman()
