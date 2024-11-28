import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        f"""
    Bagels, a deductive logic game, By Al Sweigart al@inventwithpython.com

    I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.

    Here are some clues:

    When I say: Pico    That means:  One digit is correct but in thewrong position.
                Fermi                One digit is correct and in theright position.
                Bagels               No digit is correct.

    I have thought up a number.
    """
    )

    while True:
        print(f"You have {MAX_GUESSES} guesses to get it.")
        secret_number = getSecretNumber()
        num_guesses = 1
        print(secret_number)

        while num_guesses <= MAX_GUESSES:
            guess = ""

            while len(guess) != NUM_DIGITS:
                print(f"Guess #{num_guesses}")
                guess = input("> ")

            clues = getClues(guess, secret_number)
            print(clues)
            num_guesses += 1
            
            if guess == secret_number:
                break

        if num_guesses > MAX_GUESSES:
            print("You ran out of guesses.")
            print(f"The answer was {secret_number}")

        print("Do you want to play again? (y or n)")
        if not input("> ").lower().startswith("y"):
            break
        print("Thanks for playing!")



def getSecretNumber():
    secret_number = ""

    numbers = list("0123456789")
    random.shuffle(numbers)

    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])

    return secret_number


def getClues(guess, secret_num):
    if guess == secret_num:
        return "You got it."
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()

    return " ".join(clues)
    


if __name__ == "__main__":
    main()
