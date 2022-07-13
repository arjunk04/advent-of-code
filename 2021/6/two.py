# Part 1: Define Constants
DAYS = 256
CYCLE = 6
FIRST_CYCLE = 8

# Part 2: Take Input String
init_state = input()

# Part 3: Parse Input into Initial State
fishies = [0] * (FIRST_CYCLE + 1)
count_fish = 0
print(fishies)
for s in init_state.split(","):
    try:
        n = int(s)
        fishies[n] += 1
        count_fish += 1
    except:
        print("SOMETHING HAS GONE HORRIBLY WRONG OH GOD HELP ME")

# Part 4: Simulation
print(count_fish)
for i in range(DAYS):
    next = fishies.pop(0)
    fishies[CYCLE] += next
    fishies.append(next)
    count_fish += next
    print("Day", i + 1, ": ", count_fish)

print(count_fish)