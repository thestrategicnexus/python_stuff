import numpy as np

#pseudo-random means
#random but consistent
#ensures reprodusability
#print(np.random.rand())

np.random.seed(1)
print(np.random.rand())
print(np.random.rand())

np.random.seed(4)
print(np.random.rand(1,5))
print(np.random.randint(1,5))

np.random.seed()
print(np.random.rand(1,5))
print(np.random.randint(1,5))