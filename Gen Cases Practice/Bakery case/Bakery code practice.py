import numpy as np
import pandas as pd
cupcakes = np.array([2, 0.75, 2 ,1 , 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter = ',')

print(recipes)
print('\n')
eggs = recipes[:,2]
print(eggs)

one_eggs = recipes[(eggs == 1)]
print('\n')
print(one_eggs)
print('\n')
print('\n')
cookies = recipes[2,:]
print(cookies)
print('\n')
double_batch = cupcakes*2
print(double_batch)
print('\n')
grocery_list = cookies + double_batch
print(grocery_list)