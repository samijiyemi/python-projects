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

    def __init(self, breed):
        self.breed = breed

    def setColor(self, color):
        self.color = color

    def getColor(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.color


class GeekforGeeks:

    def __init__(self):
        self.geek = "GeekforGeeks"

    def _print_geeks(self):
        print(self.geek)


class Employee:
    def __init__(self):
        """_summary_
        """
        print("Employee Created!")

    def __del__(self):
        print("Destructor Called, Employee Deleted!")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Person:
    """_summary_
    """

    # Constructor
    def __init__(self, name):
        self.name = name

    # get name
    def _get_name(self):
        return self.name

    # check if the user is employee
    def is_employee(self):
        return False


class Employee(Person):

    def is_employee(self):
        return True


emp = Person("Sam")
print(emp._get_name(), emp.is_employee())
emp = Employee("Ogbenisamu")
print(emp._get_name(), emp.is_employee())
