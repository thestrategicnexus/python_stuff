import matplotlib.pyplot as plt

#LINE PLOT
year=[1958,1970,1990,2010,2015,2020,2030]
pop=[2.519,3.692,5.263,6.972,8.993,9.572,11.268]

#add data
year=[1800, 1850, 1900] + year
pop=[1.000, 1.964, 1.790] + pop

plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population 1958-2030')
plt.yticks([0,2,4,6,8,10,12],
            ['0', '2B', '4B', '6B', '8B', '10B', '12B'])


#plt.scatter(year,pop)
plt.show()

#HISTOGRAM
values =[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins = 3)
plt.show()