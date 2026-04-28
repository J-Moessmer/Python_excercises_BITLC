#26-02-26_Klasse_Rechteck
class Square:
    def __init__(self, number, Lenght, Width):
            self.Lenght = Lenght
            self.Width = Width
            self.number = number
    def calc(self):
          print (f" The surface area of square No. {self.number} is", self.Lenght*self.Width)

S1=Square(1, 50, 10)
S2=Square(2, 3, 511)
S3=Square(3, 8,9)

S1.calc()
S2.calc()
S3.calc()
