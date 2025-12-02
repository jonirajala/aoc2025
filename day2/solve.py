import os


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = f.read().strip()
    data = [tuple(map(int, x.split("-"))) for x in data.split(",")]

print(data)


# part 1

tot = 0

for low, high in data:
    for i in range(low, high + 1):
        i = str(i)
        if i[len(i)//2:] in i[:len(i)//2]:
            tot += int(i)


print(tot)

# part 2
    
tot = 0

for low, high in data:
    for i in range(low, high + 1):
        i = str(i)

        for j in range(1, len(i) // 2 + 1 ):
            if len(i) % j != 0:
                continue

            chunks = [int(i[k:k+j]) for k in range(0, len(i), j)]

            if len(set(chunks)) == 1:
                tot += int(i)
                break


print(tot)
