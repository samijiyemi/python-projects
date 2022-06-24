# import random

# user = input("Enter a choice (rock, paper, scissors): ")
# possible = ["rock", "paper", "scissors"]
# computer = random.choice(possible)

# if user == computer:
#     print(f"Both players selected {user}. It is a tie!")
# elif user == "rock":
#     if computer == "scissors":
#         print(f"Rock smashed scissors you win!")
#     else:
#         print("Paper covers rock! You Loose")
# elif user == "paper":
#     if computer == "rock":
#         print("Paper cover rock, you win!")
#     else:
#         print("Scissors cut prayer, you loose!")
# elif user == "scissors":
#     if computer == "paper":
#         print("Scissors cuts paper! You win!")
#     else:
#         print("Rock smashes scissors, You Loose!")

# # print(f"you choose {user} and computer choose {computer}")


class Dog:
    """_summary_
    """

    animal = "Dog"

    # The Init Method or constructor
    def __init__(self, breed, color):

        #  Instance Variable
        self.breed = breed
        self.color = color


# Object of a Dog Class
Rudger = Dog("German Sheperd", "Black")
Buzo = Dog("Local Dog", "Brown")


print("Rudger Details")
print("Rudger is a", Rudger.animal)
print("Breed:", Rudger.breed)
print("Color:", Rudger.color)

print("-" * 100)

print("Buzo Details")
print("Buzo is a", Buzo.animal)
print("Breed:", Buzo.breed)
print("Color:", Buzo.color)
