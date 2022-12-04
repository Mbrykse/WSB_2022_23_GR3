class Person():
    def __init__(self, name):
        self.name = name

class Emailaddress(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

E = Emailaddress("Name", "name.surname@mail.com")
print(E.name)
print(E.email)
