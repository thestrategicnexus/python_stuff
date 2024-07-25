import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
df = pd.read_csv('gapminder.csv')

# Print the maximum population value (optional)


print(df)

print(df['population'].max())
print(df['year'].max())
#print(df['lifeexp'].max())
#print(df['gdpcap'].max())
# Extract year and population data
#year = df['year']
#pop = df['pop']

year = df['year']
population = df['population']

# Set y-axis limits to encompass full population range (with slight buffer)
#plt.ylim(bottom=0, top=population.max() * 1.2)  # Adjust '1.1' as needed

# Plot population vs year
plt.plot(year, population)

# Add informative labels
plt.xlabel("Year")
plt.ylabel("Population")

# Add a title (optional)
plt.title("Global Population Over Time (Gapminder)")  # Adjust title as needed

# Show the plot
plt.show()
# Show the plot
#plt.show()


#help(plt.plot)

"""
print("Scatterplot")
plt.scatter(df.year, df.population)
plt.xscale('log')
xlab = 'Year'
ylab = 'Population'
title = "Year and Population"
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
#plt.show()

print("Plot")
plt.plot(df.gdp_cap, df.life_exp)
plt.xlabel('GDP')
plt.ylabel('LIFE EXP')
#plt.show()

print("Histogram")
plt.hist(df.life_exp)
#plt.show()

print("Histogram with bins")
plt.hist(df.life_exp, bins = 5)
#plt.show()
plt.clf() #clean up the plot


plt.hist(df.life_exp, bins = 15)
#plt.show()
plt.clf()

#print(df.life_exp)


#help
#help(plt.hist)
"""