from math import inf
from statistics import median

crabstr = input()
crabs = []
weighted = []
avg = 0

min = inf
max = -inf

for c in crabstr.split(","):
    n = int(c)
    crabs.append(n)

    if (n < min):
        min = n
    
    if (n > max):
        max = n

lowest_fuel = inf
for i in range(min, max):
    fuel_sum = 0
    for c in crabs:
        dist = abs(c - i)
        dist = (dist * (dist + 1))/2

        fuel_sum += dist
    
    if (fuel_sum < lowest_fuel):
        lowest_fuel = fuel_sum
        print(i)

print(lowest_fuel)
