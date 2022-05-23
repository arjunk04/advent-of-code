numbers = []
number_str = input()
while number_str != "":
    numbers.append(int(number_str))
    try:
        number_str = input()
    except EOFError: # when redirected stdin, may get an eof. at this point, break the loop
        break

count = 0
for i in range(1, len(numbers)):
    if(numbers[i] > numbers[i-1]):
        count += 1

print(count)
