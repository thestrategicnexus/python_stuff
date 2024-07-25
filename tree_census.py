import numpy as np

num_data_points = 1000
start_number_tree = 3
start_number_block = 104000
end_number_block = 516296
min_count_block = int(num_data_points * 0.1)  # Minimum count for 30% of data points

tree_id = np.arange(start_number_tree, start_number_tree + num_data_points)

# Generate block IDs if the file doesn't exist
block_id = np.repeat(np.random.randint(start_number_block, end_number_block + 1), min_count_block)
remaining_points = num_data_points - len(block_id)
if remaining_points > 0:
    additional_block_id = np.random.randint(start_number_block, end_number_block + 1, remaining_points)
    block_id = np.concatenate((block_id, additional_block_id))

# Save the block_id array to a file
np.save('block_id_neww.npy', block_id)
trunk_dia = np.random.randint(0, 51, num_data_points)
stump_dia = np.random.randint(0, 31, num_data_points)

# Shuffle the block IDs to randomize their order
np.random.shuffle(block_id)

# Create the array
np_trees = np.column_stack((tree_id, block_id, trunk_dia, stump_dia))

#print the array
print("The tree census dataset")
print(np_trees)
print()


#select five block ids starting from the 10th
block_id_slice = block_id[9:14]
print("The selected five block ID´s beginning from the 10th")
print(block_id_slice)
print()



#print(np_trees[:100])

#create array of trunk diameters with even row indices from 50 to 100
every_other_dia = np_trees[50:101:2, 2]
print("Array with trunk diameters with even row indices from 50 to 100")
print(every_other_dia)
print()



#create array of first 100 trunk diameters
hundred_diameters = np_trees[:100, 2]
print("The first 100 trunk diameters")
print(hundred_diameters)
print()

#sorted trunk diameters from smallest to largest
sorted_trunk_diameters = np.sort(np_trees[:, 2])
print("Trunk diameters sorted from smallest to largest")
print(sorted_trunk_diameters)

#array contains row data on largest tree in array
print("Largest tree in array")
largest_tree_data = np_trees[np_trees[:, 2] == 50]
print(largest_tree_data)
print()

#slice array to get only block id
print("slice array to get block id")
largest_tree_block_id = largest_tree_data[:, 1]
print(largest_tree_block_id)
print()

#create a block array with trees containing block id 313879
#block_207843 = np_trees[np_trees[:, 2] == 387694]
#print(block_207843)
#not working to double check

trunk_stump_dia = np.where(np_trees[:,2] == 0, np_trees[:, 3], np_trees[:, 2])
true_indices = np_trees [:, 2] == 0
true_rows = np_trees[true_indices]

print("true rows")
for row in true_rows:
    print(row)


print(trunk_stump_dia)


print()

#create a new trees array
new_trees = np.array([[1211, 227386, 20, 0], [1212, 227386, 8, 0]])
#print shape of tree census and the new tree array
print("The tree shape and the new array shape")
print(np_trees.shape, new_trees.shape)
print()

#add rows to np_trees to contain the data for the new trees
updated_tree_census = np.concatenate((np_trees, new_trees))
#print the new tree census
print("The new tree census")
print(updated_tree_census)


#reshape trunk stump diameters
reshaped_dia = trunk_stump_dia.reshape((1000,1))

#conc the reshaped dia to the tree census as last column
concatenated_tree_census = np.concatenate((np_trees, reshaped_dia), axis=1)
print("The new conc tree census")
print(concatenated_tree_census)


#delete stump dia column from tree census
trees_no_stumps = np.delete(np_trees, 3, axis=1)

#saving the indices of trees on block
private_block_ind = np.where(np_trees[:,1]== 313879)

#delete all rows for 313879
np_trees_clean = np.delete(trees_no_stumps, private_block_ind, axis=0)

#print new tree
print(np_trees_clean)