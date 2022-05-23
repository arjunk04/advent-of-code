values = [0, 0, 0, 0] # horizontal, depth (p1), depth (p2), aim

def move(values, direction, units):
    if (direction == "forward"):
        values[0] += units
        values[2] += values[3] * units
    elif (direction == "down"):
        values[1] += units
        values[3] += units
    elif (direction == "up"):
        values[1] -= units
        values[3] -= units

    return values
        
direction = input()

while direction != "":
    parts = direction.split(" ")
    values = move(values, parts[0], int(parts[1]))

    try:
        direction = input()
    except EOFError:
        break
