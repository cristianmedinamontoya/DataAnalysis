#While the mean and median can tell us about the center of our data, they do not reflect the range of the data. That’s where standard deviation comes in.

#Similar to the interquartile range, the standard deviation tells us the spread of the data. The larger the standard deviation, 
# the more spread out our data is from the center. The smaller the standard deviation, the more the data is clustered around the mean.

import numpy as np

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)

acorn_squash_avg = np.mean(acorn_squash)

pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)

print(pumpkin_std)
print(acorn_squash_std)

winner = pumpkin

#The biggest standard deviation between the two datasets is
#pumpkin