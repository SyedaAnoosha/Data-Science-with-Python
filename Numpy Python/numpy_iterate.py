import numpy as np
height = [68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122]
np_height = np.array(height)
for x in np.nditer(np_height) :
    print(str(x)+" inches")