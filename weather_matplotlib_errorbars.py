# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')
seattle_weather['DATE'] = pd.to_numeric(seattle_weather['DATE'], errors='coerce')
austin_weather['DATE'] = pd.to_numeric(austin_weather['DATE'], errors='coerce')

seattle_agg_1 = seattle_weather.groupby('DATE')['MLY-TAVG-STDDEV'].mean().reset_index()
seattle_agg_2 = seattle_weather.groupby('DATE')['MLY-TAVG-NORMAL'].mean().reset_index()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_agg_1["DATE"], seattle_agg_2["MLY-TAVG-NORMAL"], yerr=seattle_agg_1["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()