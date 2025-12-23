# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")


import matplotlib.pyplot as plt
fig, ax = plt.subplots()


def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors = color)


plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time', 'CO2(ppm)')


plt.show()