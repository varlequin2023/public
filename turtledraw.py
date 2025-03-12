#Turtle Draw by Vincent Arlequin - FA/24 CSC-175-02 - 09/20/24
#To Do: Draw a red pentagon, octagon, and green circle separately, and then on top of one another 

#Imports Turtle Module
import turtle

#Purpose: Draws a Red Pentagon
#Assumptions: A turtle is separately defined 
#Inputs: Turtle Name, Size, X-Coordinate, Y-Coordinate
#Post-Conditions: A Red Pentagon is drawn at the size and at the location specified by the named turtle
def pentagon(turtle, size, x, y):

    #Moves Turtle on Screen
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    #Set line and fill colors to red
    turtle.pencolor("red")
    turtle.fillcolor("red")

    #Begins Fill (so that shape can be filled with red)
    turtle.begin_fill()

    #Loop that repeats drawing the necessary lines for a drawing the pentagon
    for i in range(5):
        #Draws a line
        turtle.forward(size)
        #Turns the turtle in preparation for drawing the next line
        turtle.left(72)

    #Completes and fills shape
    turtle.end_fill()

#Purpose: Draws an Octagon with dots at the vertices
#Assumptions: A turtle is separately defined 
#Inputs: Turtle Name, Size, X-Coordinate, Y-Coordinate
#Post-Conditions: An Octagon with dots at the vertices is drawn at the size and at the location specified by the named turtle
def octagon(turtle, size, x, y):
    #Moves Turtle on Screen
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    #Set line color to black
    turtle.pencolor("black")

    #Loop that repeats drawing the necessary lines for drawing the octagon
    for i in range(8):
        #Draws a line
        turtle.forward(size)
        #Adds a dot at the end of each line
        turtle.dot()
        #Turns the turtle in preparation for drawing the next line
        turtle.left(45)

#Purpose: Draws a Green Circle
#Assumptions: A turtle is separately defined 
#Inputs: Turtle Name, Size, X-Coordinate, Y-Coordinate
#Post-Conditions: A Green Circle is drawn at the size and at the location specified by the named turtle
def circle(turtle, size, x, y):
    #Moves Turtle on Screen
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    #Set line and fill color to green
    turtle.pencolor("green")
    turtle.fillcolor("green")

    #Begins Fill (so that shape can be filled with green)
    turtle.begin_fill()

    #Loop that draws a circle one degree at a time
    for i in range(365):
        #Draws a part of the circle
        turtle.forward(size)
        #Turns the turtle in preparation for drawing the next part of the circle
        turtle.left(1)

    #Completes and fills shape
    turtle.end_fill()

#Purpose: A circle, octagon, and pentagon are drawn on top of eachother
#Assumptions: A turtle is separately defined, the circle, octagon, and pentagon functions being defined
#Inputs: Turtle Name, X-Coordinate, Y-Coordinate
#Post-Conditions: A circle, octagon, and pentagon are drawn on top of eachother in the specified location by the named turtle
def combined(turtle, x, y):
    circle(turtle, 2, x, y)
    octagon(turtle, 50, x, y+30)
    pentagon(turtle, 25, x, y+50)

#Draws individual shapes, then draws combined shapes
def main():
    steve = turtle.Turtle()

    #Draws Individual Shapes
    pentagon(steve, 50, -125, 50)

    octagon(steve, 50, 0, 50)

    circle(steve, 1, 175, 50)

    #Draws Combined Shapes
    combined(steve, 0, -200)

#Runs main() Function
main()
