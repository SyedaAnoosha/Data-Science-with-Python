import numpy as np

np_2d = np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(np_2d)
print(np_2d.shape) #(2, 5): 2 rows, 5 columns
print(np_2d[0][2])
print(np_2d[0,2])
print(np_2d[0][0:3])
print(np_2d[0])

baseball = [[180,78.4], [215,102.7], [210,98.5], [188,75.2]]
np_baseball = np.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)

# Print out the 4th row of np_baseball
print(np_baseball[3])

# Select the entire second column of np_baseball: np_weight_lb (weight second column)
np_weight_lb = np_baseball[:,1]

# Print out height of 3rd player height is first column
print(np_baseball[2][0])

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat * 2)
print(np_mat + np.array([10, 10]))
print(np_mat + np_mat )