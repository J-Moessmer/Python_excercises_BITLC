#26_02_23_01_OOP
class Person:
    def __init__(self, name, age): #ethode erstellen
        self.name = name
        self.age = age
    def Greeting(self):    
        if self.age>=18:
            print (f"Hey Everyone, Im learning OOP in Python My name is {self.name} and I am {self.age} years old")
        else:
            pass

#Klassenbeispiel        
p1= Person("tom", 35)
p2= Person("bob", 40)
p3= Person("Kool", 16)

# P1.name = "tom"
# P1.age = 35

# P2.name = "Bob"
# P2.age = 40


p1.Greeting()
p2.Greeting()


# class Klasse_1:
#     pass

# class Klasse_2:
#     pass

# class Klasse_3:
#     pass


