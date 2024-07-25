import turtle

fred = turtle.Turtle()
#fred.speed(10)

#fred.left(114)
#fred.forward(40)

"""for _ in range(1):
    fred.right(90)
    fred.forward(40)
fred.right(180)
fred.forward(80)
"""

for i in range(5):
  side_length=25
  #angle = 95
  #increment = 2

  for side in range(1):
   fred.forward(side_length)
 # fred.forward(25)
   fred.left(114)
   fred.forward(40)
   fred.right(90)
   fred.forward(40)
   fred.right(90)
   fred.forward(40)
   fred.right(90)
   fred.forward(40)
   fred.right(180)
   fred.forward(40)
  # fred.forward(increment / 2)
  # var = side_length - increment
   fred.left(10)

#fred.left(180)
