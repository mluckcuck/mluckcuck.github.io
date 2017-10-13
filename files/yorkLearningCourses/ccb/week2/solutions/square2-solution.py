from turtle import *

"""Make a blue square """

length = 100
angle = 90
sides = 4

penup()
setpos(0,0)
pendown()


color('blue')

begin_fill()
for i in range(sides):
    forward(length)
    left(angle)

end_fill()
