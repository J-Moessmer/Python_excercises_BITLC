#26-02-23_07_Circle
class circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.circumference = radius*2*3.14
        self.area = 3.14*radius**2

    def info(self):
        print(f"Circumference: {self.circumference}\nArea: {self.area}")

C1 = circle(1, 32)


C1.info()
