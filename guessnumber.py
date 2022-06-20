# Guess a number
# import random module from python

import random

# function that runs to guess a number


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
#     guess can never be equal to random_number
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry guess again. Too High")

    print(
        f"Yay, Congrat you have guess the random number {random_number} correctly!")


guess(10)
