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
        return guess


number_guess = guess(10)
print(number_guess)
