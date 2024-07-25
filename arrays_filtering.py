import numpy as np
list_simp = np.arange(1,6)
mask = list_simp % 2 == 0

#output values that fit the calculation in mask
print(list_simp[mask])

#print whole list
print(list_simp)

#print boolean which calculation fits to which value
print(mask)


searchlist = ([[1, 22],
         [2, 21],
         [3, 27],
         [4, 26]])

np_searchlist = np.array(searchlist)

print(np.where(np_searchlist[:, 1] % 2 == 0))