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


def getSecretNumber():
    secret_number = ""

    numbers = list("0123456789")
    random.shuffle(numbers)

    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])

    return secret_number
    


if __name__ == "__main__":
    # main()
