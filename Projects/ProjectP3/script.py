from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

orders = pd.read_csv('orders.csv')
# print(orders.head(5))
#My solution using chatgpt & codeacademy
month = orders['date'].str.split('-', expand = True).reset_index()
print('\n')
orders['month'] = month[0]
# print month[0].head(5)
print(orders.head(5).reset_index())
# solution from chatgpt
# date_parts = data['date_column'].str.split('/', expand=True)
# solution of codeacademy
# orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print('\n')
#I used this to create an avg of the price per month
#I grouped by the months, and then I called the column 'price' from orders and called the function mean 
avg_order = orders.groupby('month')['price'].mean().reset_index()
print(avg_order.head(5).reset_index())
print('\n')
std_order = orders.groupby('month')['price'].std().reset_index()
print(std_order.head(5).reset_index())

#THIS IS FOR BAR CHART
ax = plt.subplot()
bar_heights = avg_order.price
bar_errors = std_order.price
plt.bar(range(len(bar_heights)), bar_heights, yerr = bar_errors, capsize = 5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.title('Orders Pricing')
plt.xlabel("Month")
plt.ylabel("Prices")
plt.show()


#THIS IS FOR HISTOGRAM
customer_amount = orders.groupby('customer_id').price.sum().reset_index()

print(customer_amount.head(5))

plt.hist(customer_amount.price, range = (0, 200), bins = 40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Customer Types')
plt.show()