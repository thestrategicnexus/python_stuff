import pandas as pd

brics = pd.read_csv('brics.csv')

'''
single square brackets to print out 
as a Pandas Series.
'''

'''
double square brackets to print out 
as a Pandas DataFrame.
'''

'''specify which column should be used as a row label'''
brics = pd.read_csv('brics.csv', index_col=0)

'''select which columns to print'''
'''column access through brackets'''
'''print as dataframe'''
print(brics[['country', 'capital']])

print()

'''print out all specifics of one key value'''
print('the loc function')
print(brics.loc["RU"])

print()

'''print as dataframe'''
print('the iloc function')
print(brics.iloc[[1]])

print()

'''print all rows with capital and country'''
'''row access through slicing'''
'''print as dataframe'''
print(brics.loc[:,['country', 'capital']])

print()
print('the loc function')
print(brics.loc[['RU','IN','CH'],['country', 'capital']])


print()
print('the iloc function')
print(brics.iloc[[1,2,3], [0,1]])


#print out first 3 observations
print(brics[0:3])