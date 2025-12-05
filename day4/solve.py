import os


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    # data = [line.strip() for line in f.readlines()]
    # data = [line.split(", ") for line in data]
    data = f.read()
    h = len(data.split("\n"))
    w = len(data.split("\n")[0])
    data = data.replace("\n", "")


print(data)
print(h, w)

# part 1 
tot = 0
for i in range(h):
    for j in range(w):
        if data[i*w+j] == "@":
            count = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == l == 0:
                        continue
                    if i+k < 0 or i+k >= h or j+l < 0 or j+l >= w:
                        continue
                    if data[(i+k)*w+j+l] == "@":
                        count += 1

            if count < 4:
                
                tot += 1


print(tot)

# 1351


# part 2
tot = 0
data = list(data)
while True:
    start = tot
    for i in range(h):
        for j in range(w):
            if data[i*w+j] == "@":
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if i+k < 0 or i+k >= h or j+l < 0 or j+l >= w or k == l == 0: continue
                        if data[(i+k)*w+j+l] == "@":
                            count += 1

                if count < 4:
                    tot += 1
                    data[i*w + j] = "."

    if start == tot:
        break
    
print(tot)

# 8345
