"""Darw a green triangle """

from turtle import * # Imports from the turtle library everything it defines


length = 100 #This is a normal python variable
angle = 120 # Another python variable

penup() # Stops the turtle from drawing as it moves
setpos(-200,200) # Moves the turtle to the given position
pendown() # Starts the turtle drawing as it moves 

color('green') #Sets the colour for the fill commands..

begin_fill() #Begins a section that we want to fill with colour 
forward(length) #Moves the turtle forwards by 100 steps
left(angle) # Turns the turtle left by 120 degrees
forward(length)
left(angle)
forward(length)
end_fill() # Ends a section that we want to fill with colour
