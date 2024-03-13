import matplotlib as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

print(restaurants.head(5))

cuisine_options_count = restaurants.cuisine.nunique()
print('\n')
print(cuisine_options_count)
#This is useful to do the following things:
# 1. groupby is used for group columns 
# 2. Uses column names
# 3. count() is used to count
# 4. reset_index() is used to reset any array before
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(cuisine_counts)