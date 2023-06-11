import numpy as np
np.random.seed(123) # saves the output of your choice

# Use randint() to simulate a dice
print(np.random.randint(1,7))
print(np.random.randint(1,7))

step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)