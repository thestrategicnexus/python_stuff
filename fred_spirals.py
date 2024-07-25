import turtle

fred = turtle.Turtle()
#fred.speed(10)

fred.left(114)
#size=40
size=5
gap=5
angle=5
#fred.forward(40)

for _ in range(15):
    fred.forward(gap)
    #fred.forward(25)
    fred.left(114)
    #fred.forward(40)
    fred.forward(size)
    fred.right(90)
    #fred.forward(40)
    fred.forward(size)
    fred.right(90)
    #fred.forward(40)
    fred.forward(size)
    fred.right(90)
    #fred.forward(40)
    fred.forward(size)
    fred.right(180)
    fred.forward(size)
    fred.left(angle)
    #fred.forward(40)

    size += 7
    gap += 8
    angle += 1