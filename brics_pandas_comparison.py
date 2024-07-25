import pandas as pd
import numpy as np

brics = pd.read_csv('brics.csv', index_col=0)
#print(brics.loc[:, 'area'])
#is_huge = brics['area'] >8
#is_huge = brics[brics['area'] >8]
#print(brics[is_huge])

#print(np.logical_and(brics['area'] > 8, brics['area'] < 10))

#print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)])

#extract the area column as series
print(brics['area'])
#use small to subset brics
small = brics['area'] < 5
#create subset sm
sm = brics[small]
#convert the code of small and sm to a one liner
sme = brics[brics['area'] < 5]

#create medium area between 2 and 5
areas = brics['area']
between = np.logical_and(areas > 2, areas < 5)
medium = brics[between]

#print subset
print(medium)

