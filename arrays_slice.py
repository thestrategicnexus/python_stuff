import numpy as np

# 3d arrays
array_1_2D = np.array([[1,2], [5,7]])
array_2_2D = np.array([[8,9], [5,7]])
array_3_2D = np.array([[1,2], [5,7]])
array_3d = np.array([array_1_2D, array_2_2D, array_3_2D])
print(array_3d)
print()

array = np.array([[1,2], [5,7], [6,6]],dtype=np.float64)
#put the array into one dimension
array.flatten()
print(array.flatten())
print()
# reshape the array
print(array.reshape(2,3))
print()
print(array.dtype)

back_to_int = array.dtype=np.int32
print(array.dtype)
print()

# LIST ORDERS
list_order = ([[3,1,4,8],
        [7,9,2,5],
        [0,6,0,0]])

np_list_order = np.array(list_order)
print(np.sort(np_list_order, axis = 1))
print()

#LIST SLICING
list_slice = [[1,2,3,4,5,6],
[7,8,9,10,11,12],
[13,14,15,16,17,18],
[19,20,21,22,23,24],
[25,26,27,28,29,30],
[31,32,33,34,35,36],
[37,38,39,40,41,42]]

np_list_slice = np.array(list_slice)
print(np_list_slice[1:4, 1:4])


