#26_02_23_02_Klasse_Auto
class Auto:
    def __init__(self, make, colour): #methode erstellen
        self.make = make
        self.colour = colour
    def Greeting(self):    
        print (f"the Car is made by {self.make} and is painted {self.colour}.")
        

#Klassen       
p1= Auto("BMW", "Rot")
p2= Auto("Audi", "Grün")
p3= Auto("Mercedes", "Tarnfarbe")




p1.Greeting()
p2.Greeting()
p3.Greeting()
