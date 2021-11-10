
import time as t
print(t.localtime())
time_now = t.localtime()
print("Transaction completed at ", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "min")

print(t.time())
time_now = t.time()
delivery_time = time_now + 86400 * 7
t.sleep(5)
print(t.localtime(delivery_time))

from matplotlib import pyplot as plt
x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]
plt.plot(x, y)
plt.show()
legend = ["January", "February", "March", "April"]
plt.xticks(x, legend)
plt.plot(x, y)
plt.show()
plt.bar(x, y)
plt.ylabel("Sales in US$")
plt.title("Monthly Sales")
plt.show()




import time
import turtle

turtle.bgcolor("white")
turtle.pensize(2)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.speed(0)
turtle.color("black", "black")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
time.sleep(5)
turtle.hideturtle



""""

import time
from turtle import *

bgcolor("red")
penup()
goto(0, -90)
pendown()
color("white")
begin_fill()
circle(90)
end_fill()


penup()
goto(0, -60)
pendown()
color("red")
begin_fill()
circle(60)
end_fill()


penup()
goto(18, -54)
pendown()
color("white")
begin_fill()
circle(54)
end_fill()

penup()
goto(0, -90)
pendown(0, -10)

AF = 25
a = 180 - 180/5
color("red")
begin_fill()
for i in range(5):
    forward(AF)
    right(a - 360/5)
    forward(AF)
    left(a)
end_fill()



"""


