import numpy as np

num_data_points = 10

#definition of data types for each column
dtype = [('bullets', int), ('headshots', int), ('age', int), ('success_rate', int), ('gender', 'U1')]

bullets = np.full(num_data_points, 130, dtype=int)
headshots = np.random.randint(20, 130, num_data_points, dtype=int)
age = np.random.randint(20, 41, num_data_points, dtype=int)
success_rate = np.round((headshots * 100) / bullets, decimals=2).astype(int)
gender = np.random.choice(["f", "m"], size=num_data_points)

#creating the structured array with data types
np_shootingstar = np.empty(num_data_points, dtype=dtype)
np_shootingstar['bullets'] = bullets
np_shootingstar['headshots'] = headshots
np_shootingstar['age'] = age
np_shootingstar['success_rate'] = success_rate
np_shootingstar['gender'] = gender

#everyone with a success rate > 70% is a champ
champs = np_shootingstar[np_shootingstar['success_rate'] > 70]
average_success_rate = np.round(np.mean(champs['success_rate'],), decimals=2)
average_success_age = np.round(np.mean(champs["age"],), decimals=2)



#print array in column form with each row below the previous one
print("All participants")
for row in np_shootingstar:
    print(row)
print("\n")

#print array with all champs
print("Champs with Success Rate > 70")
for row in champs:
    print(row['bullets'], row['headshots'], row['age'], f"{row[3]}%")
    #print(row)
print("\n")

# Print the structured array in column form with each row below the previous one
#print("Champs: Best shooters with Success Rate > 70")
#for row in champs:
#    print(f"Bullets: {row['bullets']}, Headshots: {row['headshots']}, Age: {row['age']}, Success Rate: {row[3]}%")



print(f"Average Success Rate of all champs: {average_success_rate}")
print(f"Average Age of all champs: {average_success_age}")

print("\n")
# count female and male champs
female_champs_count = np.count_nonzero(champs['gender'] == 'f')
male_champs_count = np.count_nonzero(champs['gender'] == 'm')

# print the count of female and male champs
#print(f"Female champs count: {female_champs_count}")
#print(f"Male champs count: {male_champs_count}")

# print the outcome based on the count
if female_champs_count > male_champs_count:
    print("Ladies for the win!")
elif male_champs_count > female_champs_count:
    print("Gents shout out!")
else:
    print("It´s a tie!")
