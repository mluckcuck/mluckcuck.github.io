from turtle import *

"""Make a purple rectangle """

length = 100
width = 60
angle = 90
sides = 4
drawLength = True

penup()
setpos(0,0)
pendown()


color('purple')

begin_fill()

for i in range(sides):
    if drawLength:
        forward(length)
        
    else:
        forward(width)

    left(angle)
    drawLength = not drawLength


end_fill()
