#HANGMAN GAME
#program to implement Hangman game using python. 


import random

# Visual stages of the hangman based on incorrect guesses
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |

     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """,
]

# Word bank for the game
WORD_BANK = [
    "python",
    "developer",
    "algorithm",
    "computer",
    "software",
    "variable",
    "database",
    "interface",
]


def get_random_word(words):
    """Selects and returns a random word from the provided list."""
    return random.choice(words).lower()


def display_game_state(hangman_pics, missed_letters, correct_letters, secret_word):
    """Prints the current hangman art, missed letters, and the hidden word phrase."""
    # Print current hangman stage based on total errors
    print(hangman_pics[len(missed_letters)])
    print()

    # Show missed letters
    print("Missed letters:", " ".join(missed_letters))
    print()

    # Build the hidden word display (e.g., d e v e _ _ _ e r)
    blanks = [
        letter if letter in correct_letters else "_" for letter in secret_word
    ]
    print("Word:", " ".join(blanks))
    print()


def get_guess(already_guessed):
    """Prompts the player for a letter and ensures it is a single valid alphabet."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a valid alphabet character.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        else:
            return guess


def play_hangman():
    """Main function to run the game loop."""
    print("Welcome to HANGMAN!")

    secret_word = get_random_word(WORD_BANK)
    missed_letters = []
    correct_letters = []
    game_over = False

    while not game_over:
        # 1. Refresh and show the board
        display_game_state(
            HANGMAN_PICS, missed_letters, correct_letters, secret_word
        )

        # 2. Get user input
        guess = get_guess(missed_letters + correct_letters)

        # 3. Check if the guess is in the word
        if guess in secret_word:
            correct_letters.append(guess)

            # Check if player won
            found_all_letters = all(
                letter in correct_letters for letter in secret_word
            )
            if found_all_letters:
                display_game_state(
                    HANGMAN_PICS, missed_letters, correct_letters, secret_word
                )
                print(
                    f"🎉 Congratulations! The secret word was '{secret_word}'."
                )
                print("You won!")
                game_over = True
        else:
            missed_letters.append(guess)

            # Check if player ran out of turns
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_game_state(
                    HANGMAN_PICS, missed_letters, correct_letters, secret_word
                )
                print("☠️ Out of guesses! Game Over.")
                print(f"The correct word was: '{secret_word}'")
                game_over = True


# Run the game
if __name__ == "__main__":
    play_hangman()