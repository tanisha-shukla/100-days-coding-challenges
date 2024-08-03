print(" USE OF TURTLE ")
print("DAY - 80 COMPLETED ")
import turtle as t
a = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")
''''a.begin_fill()
screen = t.Screen()
screen.bgcolor("black")
a.color("red" , "green")
for i in range(4) :
    a.forward(200)
    a.left(90)
a.end_fill() '''
c = ["blue" ,"purple" , "red" ,"orange" , "yellow" ,"pink" , "white"]
k = 0
for i in range(150,0,-20):
    a.color(c[k])
    k += 1
    a.begin_fill()
    a.circle(i)
    a.end_fill()
t.done()


