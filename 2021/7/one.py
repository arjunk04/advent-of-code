from statistics import median

crabstr = input()
crabs = []
avg = 0

for c in crabstr.split(","):
    n = int(c)
    crabs.append(n)

median_crab = int(median(crabs))
alignment_cost = 0
for n in crabs:
    cost = median_crab - n
    if (cost < 0):
        cost *= -1
    
    alignment_cost += cost

print(alignment_cost)