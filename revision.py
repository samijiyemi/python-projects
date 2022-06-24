def say_hi(name):
    if name == "":
        print("please enter your name")
    else:
        print("Hi there....")
        for letter in name:
            print(letter)


name = input("what is your name? ")
say_hi(name)
