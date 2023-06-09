import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print(np.logical_or(my_house > 18.5, my_house < 10))
print(np.logical_and(my_house < 10, your_house < 10))