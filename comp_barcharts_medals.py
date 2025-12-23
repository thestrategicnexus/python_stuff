# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
# Read the data from file using read_csv
medals = pd.read_csv('medals_by_country_2016.csv', index_col=0)

fig,ax = plt.subplots()
ax.bar(medals.index, medals["Gold"], label="Gold")
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")

ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")
ax.legend()
plt.show()