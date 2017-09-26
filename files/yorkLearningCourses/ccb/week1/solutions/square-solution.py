from turtle import *

"""Make a blue square """

length = 100
angle = 90 

penup()
setpos(0,0)
pendown()


color('blue')

begin_fill()
forward(length)
left(angle)
forward(length)
left(angle)
forward(length)
left(angle)
forward(length)
end_fill()
