import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

print(user_visits.head())
#This function is to see the first 5 rows of the DataFrame

click_source = user_visits.groupby('utm_source').id.count().reset_index()

print(click_source)

print('\n')
#This is how I separate the information of columns (GROUP BY ...)
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

print(click_source_by_month)
print('\n')

click_source_by_month_pivot = click_source_by_month.pivot(columns = 'month', index = 'utm_source', values ='id').reset_index()

print(click_source_by_month_pivot)