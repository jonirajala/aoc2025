import os

data = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    for line in f:
        line = line.strip()
        data.append((line[:1], int(line[1:])))
    


# part 1
start = 50
n = 0

for direction, steps in data:
    if direction == "R":
        start += steps
    elif direction == "L":
        start -= steps
    
    if start % 100 == 0:
        n += 1

print(n)

# part 2
start = 50
n = 0

for direction, steps in data:
    for i in range(steps):
        if direction == "R":
            start += 1
        elif direction == "L":
            start -= 1
        
        if start % 100 == 0:
            n += 1

print(n)

