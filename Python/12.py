class Person():
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name):
        self.name = "Doctor: " ,name

class Lawyer(Person):
    def __init__(self, name):
        self.name = "Lawyer: " ,name

P = Person("Michal")
D = Doctor("Anna")
L = Lawyer("Magdalena")

print(P.name)
print(L.name)
print(D.name)