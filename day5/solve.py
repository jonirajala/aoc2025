import os


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = [line.strip() for line in f.readlines()]
    # find index of empty item
    empty_index = data.index("")
    
    ranges = [tuple(map(int, x.split("-"))) for x in data[:empty_index]]
    items = [int(x) for x in data[empty_index+1:]]



# part 1

tot = 0
for item in items:
    for r in ranges:
        if item >= r[0] and item <= r[1]:
            tot += 1
            break

print(tot)
# part 2

ranges.sort(key=lambda x: x[0], reverse=False)
updated_ranges = [ranges[0]]

for i in range(1, len(ranges)):
    if ranges[i][0] <= updated_ranges[-1][1]:
        updated_ranges[-1] = (updated_ranges[-1][0], max(updated_ranges[-1][1], ranges[i][1]))
    else:
        updated_ranges.append(ranges[i])

tot = 0
for r in updated_ranges:
    tot += r[1] - r[0] + 1
print(tot)
