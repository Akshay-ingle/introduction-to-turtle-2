import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set the background color

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")  # Set the turtle shape
t.color("blue")  # Set the turtle color

# Draw a square
for _ in range(4):
    t.forward(100)  # Move the turtle forward by 100 units
    t.left(90)  # Turn the turtle left by 90 degrees

# Close the window when clicked
screen.exitonclick()
