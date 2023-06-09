import turtle

# Create a turtle instance
my_turtle = turtle.Turtle()

# Move the turtle forward and turn right
my_turtle.forward(100)
my_turtle.right(90)

# Draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Close the turtle graphics window
turtle.done()
