# put your code here
import math

angle_b = 35
angle_c = 105
angle_a = 40
side_b = 7

side_c = side_b * math.sin(math.radians(angle_c)) / math.sin(math.radians(angle_b))

print(round(side_c, 1))