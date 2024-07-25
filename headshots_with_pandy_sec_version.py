import pandas as pd

bulletsstart = [130,130,130,130,130,130,130,130,130]
headshots = [109,65,23,39,81,34,28,15,45]
age = [25,36,18,29,45,62,33,26,41]
gender = ['f','m','m','f','m','f','f','m','f']




'''create the dictionary with three four key:value pairs: my_dict'''

headshotmaster = {
    'startwith':bulletsstart,
    'realshots': headshots,
    'age': age,
    'gender': gender
}

'''build the dataframe from headshotmaster'''

champ = pd.DataFrame(headshotmaster)

print(champ)