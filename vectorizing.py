import numpy as np

#python
parray = np.array([[1,2,3],[4,5,6]])
for row in range(parray.shape[0]):
    for column in range(parray.shape[1]):
        parray[row][column] += 3
print(parray) #the code iterates throught each element and adds 3 to each directly
print()

#numpy
narray = np.array([[1,2,3],[4,5,6]])
narray + 3 #numpy does not store the result back into narray, therefore the print stays the same
narray = narray + 3 #each element is saved to each one , result is printed
print(narray)
print()

#vectorize python code
varray = np.array(["NumPy", "is", "awesome"])
print(len(varray) > 2) #len is python function not numpy fuction -> cant vectorize
print(varray) #gives out the words
print()

vectorized_len = np.vectorize(len)
print(vectorized_len(varray) > 2)


