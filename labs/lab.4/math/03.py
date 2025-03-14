import math
n_sides = int(input("input number of sides: "))
l_sides = float(input("input legth of a side: "))
A = int((n_sides * l_sides **2)/(4*math.tan(math.pi/n_sides)))

print(f"The area of the polygon is: {A}")

#area of regular polygon