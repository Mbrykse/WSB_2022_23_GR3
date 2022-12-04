class CatParent():
    def voice(self):
        print("Jestem Rodzicem!")

class CatKid(CatParent):
    def voice(self):
        print("Jestem Dzieckiem!")

    def walk(self):
        print("Moge Chodzic!")


parent = CatParent()
kid = CatKid()

kid.walk()
parent.walk()