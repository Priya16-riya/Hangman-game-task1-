import random

def choose_word():
    # List of possible words
    words = ["python", "programming", "hangman", "openai", "computer", "robotics", "intelligence", "game", "language"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Show the word with guessed letters and underscores for missing letters
    display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Enter a letter: ").lower()
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            # Check if the player has uncovered all letters
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word '{word}' correctly!")
                break
        else:
            attempts -= 1
            print("Incorrect guess.")

        if attempts == 0:
            print(f"\nSorry, you've run out of attempts. The word was '{word}'. Better luck next time!")

if __name__ == "__main__":
    hangman()
