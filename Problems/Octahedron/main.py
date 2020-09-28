import math

n = int(input())
area = (2 * math.sqrt(3) * math.pow(n, 2))
volume = (1 / 3 * math.sqrt(2) * math.pow(n, 3))

print(round(area, 2), round(volume, 2))

