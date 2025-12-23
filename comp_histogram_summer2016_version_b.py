import matplotlib.pyplot as plt
import pandas as pd

# Read the data from file using read_csv
olympics = pd.read_csv('summer2016.csv', index_col=0)

# Filter for only Rowing and Gymnastics
filtered_olympics = olympics[(olympics['Sport'] == 'Rowing') | (olympics['Sport'] == 'Gymnastics')]

# Create a single plot
plt.figure(figsize=(8, 4))

# Plot histogram for Rowing
plt.hist(filtered_olympics[filtered_olympics['Sport'] == 'Rowing']['Height'],
         bins=10, alpha=0.5, label='Rowing')

# Plot histogram for Gymnastics
plt.hist(filtered_olympics[filtered_olympics['Sport'] == 'Gymnastics']['Height'],
         bins=10, alpha=0.5, label='Gymnastics')

plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.title('Height Distribution for Rowing and Gymnastics (2016 Summer Olympics)')
plt.legend()
plt.show()
