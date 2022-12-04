class Animal():
    def sound(self):
        return " I'm talking !"

class Monkey(Animal):
    def sound(self):
        return "Give me a banana O.o"

class Horse(Animal):
    def sound(self):
        return "Ihhhaaaa"

class Dog(Monkey,Horse):
    pass

class Cat(Monkey,Horse):
    pass

#print(Dog.mro()) #pokazuje poziomy dziedziczenia

D = Dog()
C = Cat()
print(D.sound())