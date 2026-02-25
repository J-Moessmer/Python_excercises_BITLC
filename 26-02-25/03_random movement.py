#26-02-23_03_random movement
import turtle as t
import random

t.colormode(255)
t.shape("turtle")
runlen = int(input("How long should turtle run?: "))


# Draw border
t.speed (1000)   
t.penup()
t.setposition(-400,-400)
t.pendown()
t.pensize(5)
for side in range(4):
    t.forward(800)
    t.left(90)
t.hideturtle()
t.penup()

#set to middle
t.setposition(-0,-0)
t.pensize(2)
t.pendown()

#start
t.speed(0)
t.showturtle()
for i in range (1,runlen*100):
    t.setheading(random.randint(0,360))
    t.forward(random.randint(0,50))
        # Boundary Player Checking x coordinate
    if t.xcor() > 350 or t.xcor() < -350:
            t.setposition(0,0)
            t.setheading(random.randint(0,360))
            t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

        # Boundary Player Checking y coordinate
    if t.ycor() > 350 or t.ycor() < -350:
            t.setposition(0,0)
            t.setheading(random.randint(0,360))
            t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))




t.setposition (0,0)
t.exitonclick()
