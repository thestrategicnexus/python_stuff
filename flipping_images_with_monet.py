from matplotlib import pyplot as plt
import numpy as np

with open("rgb_array.npy", "rb") as f:
    rgb_array_monet = np.load(f)
plt.imshow(rgb_array_monet)
plt.show()

#flipping is done sequentially. First one axis then the other axis (like separate flipping operations)
flipping_monet = np.flip(rgb_array_monet)
#plt.imshow(flipping_monet)
#plt.show()

#flipping along axis 0 horizontal
flip_one_axis = np.flip(rgb_array_monet, axis=0)
plt.imshow(flip_one_axis)
plt.show()

#flipping along axis 1 vertikal
flip_one_axis = np.flip(rgb_array_monet, axis=1)
#plt.imshow(flip_one_axis)
#plt.show()

#flipping multiple axes simoultaneously, vertikal und horizontal, combined flip
flip_some = np.flip(rgb_array_monet, axis=(0,1))
#plt.imshow(flip_some)
#plt.show()


#transposing axis order, performs rotation
#axis 0 becomes axis 1, axis 1 becomes axis 2 and axis 2 remains
transposed_monet = np.transpose(rgb_array_monet, axes=(1, 0, 2))
#plt.imshow(transposed_monet)
#plt.show()

#splitting monet
red_array, green_array, blue_array = np.split(rgb_array_monet, 3, axis=2)


#emphasize blue, applies condition to array
#if value > than mean replace with 255
#alters the content (modifies image)
emphasized_blue_monet = np.where(blue_array > blue_array.mean(), 255, blue_array)
emphasized_red_monet = np.where(red_array > red_array.mean(), 255, red_array)
emphasized_green_monet = np.where(green_array > green_array.mean(), 255, green_array)
print(emphasized_blue_monet.shape)
print(emphasized_red_monet.shape)
print(emphasized_green_monet.shape)
print()


#remove trailing dimension / reshaping the array into 2D
#changes structure without altering content
emphasized_blue_monet_2D= emphasized_blue_monet.reshape((675,843))
emphasized_red_monet_2D = emphasized_red_monet.reshape((675,843))
emphasized_green_monet_2D = emphasized_green_monet.reshape((675,843))

print(blue_array.shape, emphasized_blue_monet_2D.shape)
print(red_array.shape, emphasized_red_monet_2D.shape)
print(green_array.shape, emphasized_green_monet_2D.shape)


emphasized_monet = np.stack([emphasized_blue_monet_2D, emphasized_red_monet_2D, emphasized_green_monet_2D], axis=2)
print("emphasized monet")
print(emphasized_monet.shape)
print()
plt.imshow(emphasized_monet)
plt.show()
#note: in datacamp it shows 675, 844 ,1 instead of 843


