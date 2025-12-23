
# njust a comment Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots(2,2)

seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')

seattle_weather['DATE'] = pd.to_numeric(seattle_weather['DATE'], errors='coerce')
austin_weather['DATE'] = pd.to_numeric(austin_weather['DATE'], errors='coerce')

seattle_agg_1 = seattle_weather.groupby('DATE')['MLY-PRCP-NORMAL'].mean().reset_index()
seattle_agg_2 = seattle_weather.groupby('DATE')['MLY-TAVG-NORMAL'].mean().reset_index()


# Plot MLY-PRCP-NORMAL from seattle_weather against MONTH
#ax.plot(seattle_agg["DATE"], seattle_agg["MLY-PRCP-NORMAL"], marker='o')
ax[0,0].plot(seattle_agg_1["DATE"],
             seattle_agg_1["MLY-PRCP-NORMAL"],
             color='r')

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
#ax.plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"], marker='o')
ax[0,1].plot(austin_weather["DATE"],
             austin_weather["MLY-PRCP-NORMAL"],
             color='b')


ax[1,0].plot(seattle_agg_2["DATE"],
             seattle_agg_2["MLY-TAVG-NORMAL"],
             color='r')



ax[1,1].plot(austin_weather["DATE"],
             austin_weather["MLY-TAVG-NORMAL"],
             color='b')


#ax.set_xlabel("Time(months)")
# Call the show function
plt.show()

