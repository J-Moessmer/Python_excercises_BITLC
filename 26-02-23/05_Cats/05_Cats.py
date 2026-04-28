#26-02-23_05_CATS!
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Meoww(self):
        print(f"MEOW! Im {self.name} !")

C1 = Cat("Snape", 18)
C2 = Cat("Mr.Bo", 18)

C1.Meoww()
C2.Meoww()
