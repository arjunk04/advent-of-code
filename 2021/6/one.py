# Part 1: Define Constants
DAYS = 80
CYCLE = 6
FIRST_CYCLE = 8

# Part 2: Take Input String
init_state = input()

# Part 3: Parse Input into Initial State
fishies = []
for s in init_state.split(","):
    try:
        n = int(s)
    except:
        print("SOMETHING HAS GONE HORRIBLY WRONG OH GOD HELP ME")

    fishies.append(n)

# Part 4: Simulation
for i in range(DAYS):
    for x in range(len(fishies)):
        fishies[x] -= 1
        if (fishies[x] < 0):
            fishies[x] = CYCLE
            fishies.append(FIRST_CYCLE)

print(len(fishies))