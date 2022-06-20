class Person:
    default_name = "ogbenisamu"
    default_email = "me@saijiyemi.co.uk"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def zero(cls, username, email_address):
        return cls(username, email_address)

    def get_profile(self):
        return f"my name is {self.name} my email is {self.email}"


sam = Person.zero("ogbenisam", "samijiyemi@gmail.com")
print(sam.get_profile())
