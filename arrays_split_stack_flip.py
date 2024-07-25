import numpy as np
from matplotlib import pyplot as plt

array = np.array([[1.1, 1.2, 1.3],
                  [2.1, 2.2, 2.3],
                  [3.1, 3.2, 3.3],
                  [4.1, 4.2, 4.3]])

print(array)
print()

#flips arrays along both axes
print("Flipped array")
print(np.flip(array))
print()

#flips array axis order and keeping element order within each axis the same
print("Transposed array")
print(np.transpose(array))
print()


#splitting arrays
#first row red, yellow, white
#second row magenta, green, cyan
#third row black, light blue, blue
rgb = np.array([[[255, 0, 0], [255, 255, 0], [255, 255, 255]],
             [[255, 0, 255], [0, 255, 0], [ 0, 255, 255]],
             [[ 0, 0, 0], [ 0, 255, 255], [ 0, 0, 255]]])

red_array = rgb[:, :, 0]
#new array selecting only red component
#all rows, all columns, only firs element from each pixel (red component)
green_array = rgb[:, :, 1]
blue_array = rgb[:, :, 2]

print("red array")
print(red_array)
print("red array shape")
print(red_array.shape) #still 3 dimensional
print()



# Stack the color arrays along the last axis to create the RGB image
rgb_image = np.stack((red_array, green_array, blue_array), axis=-1)
# Display the RGB image using Matplotlib
plt.imshow(rgb_image)
plt.axis('off')  # Turn off axis labels and ticks
plt.show()

#split array in 3 equal parts along third axis (axis=2) and assigns resulting three arrays
#to red, green, blue
red_array, green_array, blue_array = np.split (rgb, 3, axis = 2)
print("display the red channel")
print(red_array)
print()


#split array in 3 equal parts along third axis (axis=2) and assigns resulting three arrays
#to red, green, blue
red_array, green_array, blue_array = np.split (rgb, 3, axis = 2)
plt.imshow(red_array)
plt.imshow(blue_array)
plt.imshow(green_array)
plt.show()