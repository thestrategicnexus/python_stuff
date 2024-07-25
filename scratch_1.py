import matplotlib.pyplot as plt
import pandas as pd

# Read CSV using pandas
df = pd.read_csv('seattle_weather.csv')

# Converting the "MONTH" column to numeric
df['DATE'] = pd.to_numeric(df['DATE'], errors='coerce')

# Filtering out rows where "MONTH" conversion failed
df.dropna(subset=['DATE'], inplace=True)

# Plotting with pandas
plt.figure(figsize=(10, 6))
plt.plot(df['DATE'], df['MLY-PRCP-NORMAL'], marker='o', linestyle='-', color='skyblue', label='Seattle')

# Adding plot details
plt.title('Monthly Precipitation - Seattle')
plt.xlabel('Month')
plt.ylabel('Precipitation (MLY-PRCP-NORMAL)')
plt.grid(axis='y', linestyle='--')
plt.xticks(df['DATE'])  # Set x-ticks to match month values
plt.legend()

plt.tight_layout() # Adjust layout to prevent overlapping elements
plt.show()
