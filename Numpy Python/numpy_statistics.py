import numpy as np

#--- 1st example ----
baseball = [[180,78.4],
            [215,102.7],
            [210,98.5],
            [188,75.2]]

np_baseball = np.array(baseball)

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

med = np.median(np_baseball[:,0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))


#-----2nd example----

positions = ['GK', 'DF', 'MF', 'FW', 'FW', 'MF', 'DF', 'DF', 'MF', 'FW']
heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 176]

np_positions = np.array(positions)
np_heights = np.array(heights)

gk_heights = np_heights[np_positions == 'GK'] # goalkeeper heoght
other_heights = np_heights[np_positions != 'GK'] # other player heights

print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))