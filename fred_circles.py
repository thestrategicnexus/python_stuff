import turtle
import math

# Create a Turtle screen and set its properties
screen = turtle.Screen()
screen.title("Circle Drawing with Turtle")
screen.bgcolor("white")

# Create a Turtle object and name it 'fred'
fred = turtle.Turtle()

# Set the speed of the turtle
fred.speed(1)  # You can adjust the speed as needed

# Set the color of the turtle to orange
fred.color("orange")

# Draw a circle
radius = 100
fred.circle(radius)

# Print the exact position where the arrow stops
position = fred.position()
print(f"The arrow stops at position: {position}")

# Draw petals around the circle
petal_count = 12  # Number of petals (adjust as needed)
angle = 360 / petal_count  # Angle between petals
petal_radius = radius * math.sin(math.radians(angle / 2))  # Radius of each petal
for _ in range(petal_count):
    fred.circle(petal_radius / 2, extent=angle)
    fred.left(180 - angle)  # Turn to draw the next petal


# Keep the window open until it's manually closed
turtle.done()
