import numpy as np
#the list headshots
headshots = [50, 20, 35, 95, 101, 99]
#the list with the amount of bullets everyone had
bullets = [130, 130, 130, 130, 130, 130]

#creating the numpy array
np_headshots = np.array(headshots)
#print(np_headshots)

#calculating a factor
np_headshots_factor = np_headshots * 0.025
#print(np_headshots_factor)

#creating the numpy array
np_bullets = np.array(bullets)
#print(np_bullets)

#the success rate based on the factor of 0.025
successratewithfactor = np_bullets * np_headshots_factor
#print(successratewithfactor)

#the normal success rate
successrateclear = np.round(np_headshots / np_bullets * 100, decimals =2)
#print(successrateclear)
#print([f"{rate:.2f}%" for rate in successrateclear]) #printing the success rate in percentage

#everyone who has more than 70% percent ranks as champ
champ = np.array(successrateclear > 70)

#print(champ)
#printing the success rate in percentage
print([f"{rate:.2f}%" for rate in successrateclear[champ]])


print(np_headshots[2])
print(np_bullets[1:5])