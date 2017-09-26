from turtle import *

"""Make a purple rectangle """

length = 100
width = 60
angle = 90 
penup()
setpos(0,0)
pendown()


color('purple')

begin_fill()
forward(length)
left(angle)
forward(width)
left(angle)
forward(length)
left(angle)
forward(width)
end_fill()
