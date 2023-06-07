import math
r = 0.435623546256
C = 2 * math.pi * r 
A =  math.pi * r * r


print("Circumference: " + str(C))
print("Area: " + str(A))

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * math.radians(12)
print(dist)