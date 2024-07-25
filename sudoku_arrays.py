import numpy as np

sudoku_list=[[0, 0, 4, 3, 0, 0, 2, 0, 9],
 [0, 0, 5, 0, 0, 9, 0, 0, 1],
 [0, 7, 0, 0, 6, 0, 0, 4, 3],
 [0, 0, 6, 0, 0, 2, 0, 8, 7],
 [1, 9, 0, 0, 0, 7, 4, 0, 0],
 [0, 5, 0, 0, 8, 3, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 1, 0, 5],
 [0, 0, 3, 5, 0, 8, 6, 9, 0],
 [0, 4, 2, 9, 1, 0, 3, 0, 0]]

#create an nump array
np_sudoku = np.array(sudoku_list)

#print the type
#print(type(np_sudoku))

print("The Sudoku")
print(np_sudoku)

#slice the sudoku
print("Slicing the Sudoku")
print(np_sudoku[3:8, 3:8])
print()

print("Slice the Sudoku in two-step size")
#slice the sudoku in 2 steps
print(np_sudoku[3:8:2, 3:8:2])
print()


#transform it into 1D array
print ("Transform the Sudoku into a 1D array")
print(np_sudoku.flatten())
print()

#print the type
#print(np_sudoku.dtype)

#making it smaller
#small_sudoku = np_sudoku.astype(np.int8)

#print the new type
#print(small_sudoku.dtype)

#sort the sudoku along columns
print("Sorting the Sudoku along columns")
print(np.sort(np_sudoku, axis = 0))
print()

#replace the 0 with ""
new_sud= np.where(np_sudoku == 0, "", np_sudoku)
print("Replace the zero´s with ''")
print(new_sud)


