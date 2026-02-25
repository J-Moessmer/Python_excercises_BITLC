#26-02-25_01_ROTQUAD
import turtle
import random
 
t = turtle.Turtle()
t.speed(100)
turtle.colormode(255)
t.setheading(90)
sqrlen = int(input("Enter the length of the side of square: "))
change = int(input("enter the change coefficient: "))
sqrcount = int(input("Enter the number of squares: "))
laps = int(input("How many laps?: "))

def square(): #square subroutine
    for _ in range(4):
        t.forward(sqrlen) 
        t.right(90) 

for _ in range(1,sqrcount+1):
    # red = random.randint(0,255)
    # blue = random.randint(0,255)
    # green = random.randint(0,255)
    sqrlen = sqrlen+(sqrlen*change/100)
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.begin_fill()
    square()
    t.end_fill()
    t.right((360*laps)/sqrcount)
    

turtle.exitonclick()
