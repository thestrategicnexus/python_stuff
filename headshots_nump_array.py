import numpy as np

shootingstar =[[50, 130],
               [20, 130],
               [35, 130],
               [95, 130],
               [101, 130],
               [99, 130]]

np_shootingstar = np.array(shootingstar)

#print(np_shootingstar)


successrate = np.round(np_shootingstar[:, 0] / np_shootingstar[:, 1] * 100, decimals=2)
np_shootingstar_new = np.column_stack((np_shootingstar, successrate))

print(np_shootingstar_new)

for row in np_shootingstar_new:
    print(f"{row[0]} {row[1]} {row[2]:.2f}%")

#print(type(np_shootingstar))
#print(np_shootingstar.shape)

#print(np_shootingstar[3,:]) #print out the third row
#print(np_shootingstar[:,1]) #print out the second column
#print(np_shootingstar[1,0]) #print out the headshots of the second player

#np_bullets = np_shootingstar[:,1] #select the entire second column
#np_headshots = np_shootingstar[:,0] #select the entire first column
#np_headshots = [np_shootingstar[:,0] > 50, 0] #select the entire first column and all entries above 50
#np_headshots = np_shootingstar[np_shootingstar[:, 0] > 50]#select the entire first column and all entries above 50


#print(np_bullets)
#print(np_headshots)
