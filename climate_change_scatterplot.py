# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")

eighties = climate_change["1980-01-01":"1989-12-31"]
nineties = climate_change["1990-01-01":"1999-12-31"]
fig, ax = plt.subplots()

ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)
#ax.scatter(eighties["co2"], eighties["relative_temp"], color="red", label="eighties")
#ax.scatter(nineties["co2"], nineties["relative_temp"], color="blue", label="nineties")


ax.set_xlabel ("CO2 (ppm")
ax.set_ylabel ("Relative temperature")

plt.show()
plt.clf()