import numpy as np

num_data_points = 10

bullets = np.full(num_data_points, 130, dtype=int) #everyone has 130 bullets
headshots = np.random.randint(20, 130, num_data_points, dtype=int) #generating random dataset how many headshots everyone got
age = np.random.randint(20, 41, num_data_points, dtype=int) #assigning the age randomly
gender = np.random.choice(["f", "m"], size=num_data_points)  # Random gender (character)
success_rate = np.round(headshots.astype(float) / bullets.astype(float) * 100, decimals = 2)


print(bullets.dtype)
print(headshots.dtype)
print(age.dtype)
print(gender.dtype)
print(success_rate.dtype)

shootingstar = np.column_stack((bullets, headshots, age, gender, success_rate))
#np_shootingstar = np.array(shootingstar).dtype


print(shootingstar.dtype)
print(shootingstar)


#calculating the success rate of the shooters by diving headshots by bullets
#success_rate = (headshots / bullets * 100)

#success_rate = np.round(headshots / bullets * 100, decimals=2)  # Convert to float


#champs = np_shootingstar[:, 4] > 70


#everyone with a success rate of 70% is a champ
#champs = np_shootingstar[:, 4]
#champs = np_shootingstar[np_shootingstar[:, 4] > "70"]
#print("\n")
#print(champs)
#print("\n")
#print("\nChampions (Success Rate > 70%):")
#for champ in champs:
    #print(champ)

#print all champs
#print("Entries with Success Rate > 70:")
#for entry in champs:
#    print(entry)
#print("\n")

#avg_champ = np.round(np.mean(champs[:, 4]), decimals=2)  # Calculate average success rate for champs
#avg_age = int(np.mean(champs[:, 2]))  # Calculate average age for champs
#avg_champ = np.round(np.mean(champs[:, 4].astype(float)), decimals=2)  # Calculate average success rate for champs

avg_champ = np.round(np.mean(success_rate), decimals=2) #the average success_rate of all champs
avg_age = float(np.mean(age)) #the average age of all champs

female_champs = np.count_nonzero(champs[:, 3] == 'f')
male_champs = np.count_nonzero(champs[:, 3] == 'm')
if female_champs > male_champs:
    print("Females won!")
elif male_champs > female_champs:
    print("Males won!")
else:
    print("It's a tie!")


print("\n") #leaving some space in between
print("Average success rate of the champs")
print(str(avg_champ) + " %")
print("Average age of the champs")
print(avg_age)



