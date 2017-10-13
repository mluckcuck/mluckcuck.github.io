"""Draw a green triangle """

from turtle import * 


length = 100 
angle = 120
sides = 3

penup() 
setpos(0,0) 
pendown() 

color('green') 

begin_fill()

for i in range(sides):
    forward(length)
    left(angle) 

end_fill() 
