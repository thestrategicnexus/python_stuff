import pandas as pd

dict = {
    'bullets given':[130,130,130,130,130,130,130,130,130],
    'headshots':[109,65,23,39,81,34,28,15,45],
    'age':[25,36,18,29,45,62,33,26,41],
    'gender':['f','m','m','f','m','f','f','m','f'],
    'success rate':[109/130, 65/130, 23/130, 39/130, 81/130, 34/130, 28/130, 15/130, 45/130 ]
}

shots = pd.DataFrame(dict)
print(shots)



'''
dict = {'country':names,
        'drives_right':dr}
        define the key and value name but not giving values yet'''


'''
specify the row labels '''
row_labels = [1,2,3,4,5,6,7,8,9]
shots.index = row_labels

print(shots)



