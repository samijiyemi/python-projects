class Person:
    default_name = "ogbenisamu"
    default_email = "me@saijiyemi.co.uk"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_profile(self):
        return f"my name is {self.name} my email is {self.email}"


Person.default_name = "sainthemiddle"

sam = Person(Person.default_name, Person.default_email)
print(Person.default_name)
print(sam.get_profile())
