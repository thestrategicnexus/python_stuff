# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("seaborn")
# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')


seattle_agg = seattle_weather.groupby('DATE')['MLY-TAVG-NORMAL'].mean().reset_index()
austin_agg = austin_weather.groupby('DATE')['MLY-TAVG-NORMAL'].mean().reset_index()

ax.plot(seattle_agg["DATE"], seattle_agg["MLY-TAVG-NORMAL"])
ax.plot(austin_agg["DATE"], austin_agg["MLY-TAVG-NORMAL"])

ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")

plt.show()