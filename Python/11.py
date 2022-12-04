class CatParent():
    def voice(self):
        print("Jestem Rodzicem!")

class CatKid(CatParent):
    def voice(self):
        print("Jestem Dzieckiem!")

#print(issubclass(CatKid, CatParent)) - sprawdzenie dziedziczenia klas

parent = CatParent()
kid = CatKid()

parent.voice()
kid.voice()