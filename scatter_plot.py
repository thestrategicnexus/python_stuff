import numpy as np
from matplotlib import pyplot as plt

zero_array = np.zeros((2,4))
print(zero_array)

random_array = np.random.rand(3,6)
print(random_array)

doubling_array = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512])
# Create an array of integers from one to ten
one_to_ten = np.arange(1, 11)


plt.scatter(one_to_ten, doubling_array)
plt.show()
