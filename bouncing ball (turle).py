print("BOUNCING BALL USING TURTLE  ")
print("DAY - 81  COMPLETED")
import turtle as t
import time

def moveleft():
    xb = ball.xcor()
    ball.setx(xb - 10)

def moveright():
    xb = ball.xcor()
    ball.setx(xb + 10)


a = t.Screen()
a.title("BOUNCING BALL ")
a.bgcolor("black")

a.setup(width=600 , height=600)

ball = t.Turtle()

ball.color("purple")
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=8, stretch_len=8)
ball.penup()

w = 0
while True :
    if w == 0 :
         moveright()

    if w == 1:
         moveleft()


    if ball.xcor()  >=300:
          w = 1

    if ball.xcor() <=-300:
           w = 0

    time.sleep(0.1)
    a.update()


'''
 ## ON ARROW KEYS ONLY 
import random

def moveleft():
    xb = ball.xcor()
    ball.setx(xb - 10)

def moveright():
    xb = ball.xcor()
    ball.setx(xb + 10)

def moveup():
    y = ball.ycor()
    ball.sety(y + 10)

def movedown():
    y = ball.ycor()
    ball.sety(y - 10)

a = t.Screen()
a.title("BOUNCING BALL ")
a.bgcolor("black")

a.setup(width=600 , height=600)

ball = t.Turtle()

ball.color("purple")
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=8, stretch_len=8)
ball.penup()

a.listen()
a.onkeypress(moveleft , "l")
a.onkeypress(moveright , "r")
a.onkeypress(moveup , "u")
a.onkeypress(movedown , "d")

while True :
    a.update()
'''


    
