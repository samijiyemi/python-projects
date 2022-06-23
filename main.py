import random

user = input("Enter a choice (rock, paper, scissors): ")
possible = ["rock", "paper", "scissors"]
computer = random.choice(possible)

if user == computer:
    print(f"Both players selected {user}. It is a tie!")
elif user == "rock":
    if computer == "scissors":
        print(f"Rock smashed scissors you win!")
    else:
        print("Paper covers rock! You Loose")
elif user == "paper":
    if computer == "rock":
        print("Paper cover rock, you win!")
    else:
        print("Scissors cut prayer, you loose!")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors, You Loose!")

# print(f"you choose {user} and computer choose {computer}")
