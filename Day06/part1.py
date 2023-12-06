import math


def find_roots(time, distance):
    x1 = (-time + math.sqrt(time**2-4*distance)) / -2
    x2 = (-time - math.sqrt(time**2-4*distance)) / -2
    return x1, x2



with open('input.txt') as f:
    for line in f:
        values = list(map(int, line.strip().split()[1:]))
        if line.startswith('Time'):
            times = values
        elif line.startswith('Distance'):
            distances = values

total = 1
for i in range(len(times)):
    r1, r2 = find_roots(times[i], distances[i]+1)
    r1 = math.ceil(r1)
    r2 = math.floor(r2)
    print(str(r1) + " " + str(r2))
    total *= r2 - r1 + 1


print(total)
