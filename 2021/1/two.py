numbers = []
number_str = input()
while number_str != "":
    numbers.append(int(number_str))
    try:
        number_str = input()
    except EOFError: # when redirected stdin, may get an eof. at this point, break the loop
        break

window_sums = []

for i in range(len(numbers) - 2):
    window_sums.append(numbers[i] + numbers[i + 1] + numbers[i + 2])


count = 0
for i in range(1, len(window_sums)):
    if(window_sums[i] > window_sums[i-1]):
        count += 1


print(count)
