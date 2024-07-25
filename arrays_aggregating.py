import numpy as np

array_1d = np.array([1,2,3])
column_array_2d = array_1d.reshape((3,1))
print(column_array_2d)


row_array_2d = array_1d.reshape((1,3))
print(row_array_2d)
print()

#test array for aggregations
np_security = np.array([[0, 5, 1],
             [0, 2, 0],
             [1, 1, 2],
             [2, 2, 1],
             [0, 0, 0]])

print(np_security)
print()

print(np_security.sum()) #the sum per row
print(np_security.sum(axis=0)) #sum columns
print(np_security.sum(axis=1)) #sum rows
print(np_security.mean()) #the average
print(np_security.sum(axis=1, keepdims=True)) #keeping the dimensions as it is


