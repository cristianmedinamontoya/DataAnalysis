from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')
print(restaurants.head(5))
cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()

# print(cuisine_counts.head(5))
cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values
print(counts)

plt.pie(counts, labels = cuisines, autopct='%d%%')
plt.title("FoodWheel Offer")
plt.axis('equal')
plt.show()