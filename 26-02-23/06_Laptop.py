#26-02-23_06_Laptop!
class computer:
    def __init__(self, name, ram):
        self.name = name
        self.ram = ram
    def info(self):
        print(f"Laptop Brand: {self.name}\nRAM: {self.ram}GB")

C1 = computer("Lenovo", 32)
C2 = computer("Mac", 8)

C1.info()
C2.info()
