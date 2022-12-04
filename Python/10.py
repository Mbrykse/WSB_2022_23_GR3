class Cat():
    def _init_(self, name): #konstruktor - inicjalizuje obiekt z definicji klasy
        self.name = name #atrybut

a_cat = Cat("Kociak")

print(a_cat.name)