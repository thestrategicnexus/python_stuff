import numpy as np

height = np.round(np.random.normal(1.75, 0.30, 1100), 2)
weight = np.round(np.random.normal(60.32, 15, 1100), 2)

np_people = np.column_stack((height, weight)) #create the array

print (np_people) #show the dataset

print("Average weight")
print(np.mean(weight)) # the mean height of all 5000 data entries

#avg_weight = np.mean(np_people[:, 0]) #calc the average weight two options either by selecting column or like below
avg_weight = np.mean(weight)
#avg_height = np.mean(np_people[:, 1])
avg_height = np.mean(height) #calc the average height either by select column or like this

print("Average weight:", avg_weight)
print("Average height:", avg_height)

#print("Average weight: " + str(weight))

corr=np.corrcoef(np_people[:,0], np_people[:,1])
print("Correlation: " + str(corr))
#correlation coefficient if between 0 and 1 its positive indicate a moderate linear relationsship
# if below 0 then weak negative linear relationsship which means, that one var increases but the other tends to decrease or vice versa = the relationship is weak
