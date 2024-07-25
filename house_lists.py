#intialization of the values of the variables
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

#array
house = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

#changing size of kitchen
house[-3] = 10.50
#renaming living room to chill house
house[4] ="chill zone"
#adding the pool
house_1 = house + ["pool", 24.5]
#removing the pool again
del(house_1[-2:])

#creating a copy of the intitial list into new one
new_house = list(house)
#changing value of hallway in new list
new_house[1] = 5.0

#convert strings to uppercase
place ="poolhouse"
place_up = place.upper()
print(place_up)
print(place)
#zählen wieviele Buchstaben in einem Wort vorkommen
print(place.count("p"))


#convert strings in an array to uppercase
#room is a variable for each item in the house list
#isinstance is a function that checks an objects of a specific type
house_up = [room.upper() if isinstance(room, str)
            else room
            for room
            in house]
print(house_up)

#print the index of an element in a list
print(house)
print(house_1)
print(new_house)
print(house.index("hallway"))

#shows how many times the letter a is in a word
#housecounting = [room.count("a") for room in house if
#isinstance (room, str) and "a" in room]

#shows all rooms which include the letter a
housecounting = [room for room in house if isinstance(room, str) and 'a' in room]



house.reverse()
print(house)