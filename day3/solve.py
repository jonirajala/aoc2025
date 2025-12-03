import os


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = [line.strip() for line in f.readlines()]



# part 1

tot = 0
for line in data:

    largest_digit = max(line[:-1])
    index = line[:-1].index(largest_digit)

    largest_second_digit = max(line[index+1:])
    
    tot += int(largest_digit + largest_second_digit)

print(tot)

# part 2

tot = 0
for line in data:
    dig = ""
    index = 0
    for i in range(11, -1, -1):
        end = None if i == 0 else -i
        part = line[index:end]
        largest_digit = max(part)
        index = part.index(largest_digit) + index
        dig += largest_digit
        index += 1

    print(dig, line)    
    tot += int(dig)

print(tot)
assert tot == 172516781546707, tot-172516781546707
