import numpy as np
from matplotlib import pyplot as plt

#sales dataset, each column is one industry, each row one month
np_sales = np.array([[4134, 23925,  8657],
       [ 4116, 23875,  9142],
       [ 4673, 27197, 10645],
       [ 4580, 25637, 10456],
       [ 5109, 27995, 11299],
       [ 5011, 27419, 10625],
       [ 5245, 27305, 10630],
       [ 5270, 27760, 11550],
       [ 4680, 24988,  9762],
       [ 4913, 25802, 10456],
       [ 5312, 25405, 13401],
       [ 6630, 27797, 18403]])



#multipliers dataset
np_multipliers = np.array([[0.98, 1.02, 1.  ],
       [1.00, 1.01, 0.97],
       [1.06, 1.03, 0.98],
       [1.08, 1.01, 0.98],
       [1.08, 0.98, 0.98],
       [1.1 , 0.99, 0.99],
       [1.12, 1.01, 1.  ],
       [1.1 , 1.02, 1.  ],
       [1.11, 1.01, 1.01],
       [1.08, 0.99, 0.97],
       [1.09, 1.  , 1.02],
       [1.13, 1.03, 1.02]])

print("the initial array")
print(np_sales)
print()


monthly_industry_sales = np_sales.sum(axis=1, keepdims=True)
print("the sum along rows and keeping dimension")
print(monthly_industry_sales)
print()


# Add column as last column in monthly_sales
monthly_sales_with_total = np.concatenate((np_sales, monthly_industry_sales), axis=1)
print("adding this column to the initial array")
print(monthly_sales_with_total)
print()

#create 1d array
avg_monthly_sales = np_sales.mean(axis = 1)
print("Average monthly sales")
print(avg_monthly_sales)
print()

#plot the avg monthly sales across all departments
#plt.plot(np.arange(1,13),
        # avg_monthly_sales, label ="Average sales across industries")
#plt.show()

#plot department sales by month
#plt.plot(np.arange(1, 13), np_sales[:, 2], label="Department store sales")
#plt.legend()
#plt.show()


#cumulative monthly industry sales
#cum_monthly_industry_sales1 = np.cumsum(np_sales, axis=0) another variation
cum_monthly_industry_sales = np_sales.cumsum(axis=0)
print(cum_monthly_industry_sales)
print()


#plot each depts cum sales by month in separate lines
#plt.plot(np.arange(1,13), cum_monthly_industry_sales[:, 0], label ="Liquor Stores")
#plt.plot(np.arange(1,13), cum_monthly_industry_sales[:, 1],label="Restaurants")
#plt.plot(np.arange(1,13), cum_monthly_industry_sales[:, 2], label="Department Stores")
#plt.legend()
#plt.show()

#calculate taxes by industry each month
taxes = np_sales
taxes = taxes * 0.05
#in short
#taxes = np_sales * 0.05
#print (taxes)


#array revenue plus tax by industry and month
total_tax_revenue = np_sales + taxes
#print(total_tax_revenue)

print(np_multipliers)

#monthly projected sales for all industries
projected_monthly_sales = np_sales * np_multipliers
print(projected_monthly_sales)

plt.plot(np.arange(1,13), np_sales[:, 0], label ="Liquor Stores")
plt.plot(np.arange(1,13), projected_monthly_sales[:, 0], label ="Liquor Stores")
plt.show()


#splitting into quarterly data
q1_sales, q2_sales, q3_sales, q4_sales = np.split(np_sales, 4)
plt.imshow(q1_sales)
plt.show()
print(q1_sales)


#stack the four arrays
quarterly_sales = np.stack([q1_sales, q2_sales, q3_sales, q4_sales])
print(quarterly_sales)


