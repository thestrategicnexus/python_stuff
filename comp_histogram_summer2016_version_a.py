# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
# Read the data from file using read_csv
olympics = pd.read_csv('summer2016.csv', index_col=0)
fig,ax = plt.subplots()

# Filter for only Rowing and Gymnastics
filtered_olympics = olympics[(olympics['Sport'] == 'Rowing') | (olympics['Sport'] == 'Gymnastics')]

# Calculate mean height per sport
mean_heights = filtered_olympics.groupby('Sport')['Height'].mean()

# Plot the bar chart
#plt.figure(figsize=(8, 4))  # Adjust the size as needed
ax.bar(mean_heights.index, mean_heights.values)
ax.set_ylabel('Height (cm)')
#ax.title('Mean Height Comparison for Rowing and Gymnastics (2016 Summer Olympics)')
plt.show()


#Histogram from Datacamp
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observation")

plt.show()



