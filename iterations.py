import pandas as pd
brics = pd.read_csv('brics.csv', index_col = 0)
#print(brics)
for lab,row in brics.iterrows() :
  #  print('print lab ' + str(lab))
    #print('print row ' + str(row))
    #print('print lab')
    #print(lab)
    #print('print row')
    #print(row)
    #print(lab + ': ' + row["capital"])

    #LAB and ROW are ITERATORS

    #adding new column 'name_length' and adding the name length of each country from the row 'country'
    #here we create a series of objects on every iteration
    #brics.loc[lab, 'name_length'] = len(row['country'])

    #better option for larger datasets as the above will lead to loss in efficiency
    #applying on the 'country' column the len function and produces new array 'name_length' after
    #brics['name_length'] = brics['country'].apply(len)
#print(brics)

   brics.loc[lab, 'COUNTRY'] = row ['country'].upper()
print(brics)