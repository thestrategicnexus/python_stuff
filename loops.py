# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)




# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for element in areas:
    print(element)

for index, a in enumerate(areas) :
    print('room ' + str (index) + ': ' + str(a))
    print(a)

for index, area in enumerate(areas) :
    print('room ' + str(index + 1) + ': ' + str(area))




# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
          ["bedroom", 10.75],
           ["bathroom", 9.50]]

# Build a for loop from scratch
for x in house:
     print('the ' + x[0] + " is " + str(x[1]) + 'sqm')



world = {'afghanistan':30.55,
        'albania':2.77,
        'algeria':39.21}
for key, value in world.items() :
    print(key + " -- " + str(value))

    # Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
         'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

    # Iterate over europe
for key, value in europe.items():
    print('the capital of ' + (key) + ' is ' + (value))
    print('the capital of ' + str(key[0:3]) + ' is ' + value[0])