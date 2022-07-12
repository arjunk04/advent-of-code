grid_dict = {}
while True:
    try:
        line = input()
        coords = line.split(" -> ")
        c1 = coords[0].split(",")
        x1 = int(c1[0])
        y1 = int(c1[1])
        c2 = coords[1].split(",")
        x2 = int(c2[0])
        y2 = int(c2[1])

        if (x1 == x2):
            if (y1 > y2):
                swap = y1
                y1 = y2
                y2 = swap
            for i in range(y1, y2 + 1):
                if ((x1, i) in grid_dict):
                    grid_dict[(x1,i)] += 1
                else:
                    grid_dict[(x1,i)] = 1
        elif (y1 == y2): # no diagonals
            if (x1 > x2):
                swap = x1
                x1 = x2
                x2 = swap
            for i in range(x1, x2 + 1):
                if ((i, y1) in grid_dict):
                    grid_dict[(i,y1)] += 1
                else:
                    grid_dict[(i,y1)] = 1
    except EOFError:
        break

count = 0
for v in grid_dict.values():
    if (v > 1):
        count += 1

print(count)