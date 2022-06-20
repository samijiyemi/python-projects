# string concatenation

programming_language = "python"

# 3 ways on how to output strings
print("Am currently learning " + programming_language)
print("Am currently learning {}".format(programming_language))
print(f"Am currently learning {programming_language}")

# madlibs game
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

# using the third string concatenation method f string

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

# output madlib
print(madlib)
