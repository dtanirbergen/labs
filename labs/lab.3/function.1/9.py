import math
def volume(r):
    v = (4/3) * math.pi * (r ** 3)
    return v

radius = float(input())
print(volume(radius))