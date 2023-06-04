import numpy as np
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
print(type(np_baseball))


# Calculate the BMI: bmi
height_in = [23.4,56.7,18]
weight_lb = [23.4,56.7,18]
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = np.array(bmi < 21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

new_np_array = np.array([True, 1, 2]) + np.array([3, 4, False])
print(new_np_array)