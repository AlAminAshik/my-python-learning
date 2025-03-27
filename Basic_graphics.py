#python follows the cartesian coordinate system
#turtle graphics is a module in python that allows us to draw shapes and patterns

#finding turtle commands
import turtle
print(dir(turtle))

#common turlte commands
'''degrees, radians, reset, clear, tracer, forward, backward, right, left, 
circle, up, down, width, color, begin_fill, end_fill, fillcolor, pencolor,'
speed, goto, setpos, setposition, position, pos, xcor, ycor, heading, towards'
#few examples
# t.forward(100)	Move forward by 100 pixels
# t.backward(50)	Move backward by 50 pixels
# t.right(90)	    Turn 90 degrees right
# t.left(45)	    Turn 45 degrees left
# t.circle(100)	    Draw a circle with radius 100
# t.penup()	        Lift the pen (move without drawing)
# t.pendown()	    Put the pen down (start drawing)
# t.color("blue")	Change the pen color to blue
# t.speed(5)	    Set speed (1-10, 0 is fastest)
'''


#creating a circle
import turtle
t = turtle.Turtle() # Create a turtle object (not very important)
t.speed(3)      # Set the speed (1-10, 0 is fastest)
t.circle(100)   # Draw a circle with a radius of 100
turtle.done()   # Keep the window open


#drawing rectangle using for loop
import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done() # keep the window open
turtle.bye()    # close the window