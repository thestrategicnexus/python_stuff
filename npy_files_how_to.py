from matplotlib import pyplot as plt
import numpy as np

with open("rgb_array.npy", "rb") as f:
    rgb_array_test = np.load(f)
#plt.imshow(rgb_array_test)
#plt.show()

#examining the rbg data
red_array = rgb_array_test[:, :, 0]
blue_array = rgb_array_test[:, :, 1]
green_array = rgb_array_test[:, :, 2]
print(red_array, blue_array, green_array)
print()


#change rgb data
change_array = np.where(rgb_array_test == 153, 50, rgb_array_test)
#plt.imshow(change_array)
#plt.show()


#reduce every value in rgb data
all_change_array = rgb_array_test * 0.5

#convert into an array of int
all_change_array_int = all_change_array.astype(np.int8)

#saving arrays as npy, if file exists it will be overwritten
with open("change_array.npy", "wb") as f:
    np.save(f, all_change_array_int)



#get help
help(np.unique)
help(np.array)
help(np.ndarray.astype) #np.ndarray prefix method name