#26-02-23_08_chargeing
class handy:
    def __init__(self, brand, charge):
        self.brand = brand
        self.charge = charge
        charge = 0
               

    def info(self):
        for i in range(0,100,1):
            self.charge = self.charge +1
            if self.charge <= 101 and self.charge%10==0:
                print(f"{self.brand} charge level: {self.charge}%")
            else:
                pass #print("else",self.charge) (this was a test)

C1 = handy("Nokia", 55)


C1.info()
