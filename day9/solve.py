import os
import operator
import numpy as np
from functools import reduce
import re
import math

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = [list(map(int, line.strip().split(','))) for line in f.readlines()]

print(data)
sizes = dict()

for i in range(len(data)):
    w1, h1 = data[i]
    for j in range(i + 1, len(data)):
        w2, h2 = data[j]
        if w1 == w2 or h1 == h2:
            sizes[(i, j)] = 0
        else:
            sizes[(i, j)] = (abs(w2 - w1)+1) * (abs(h2 - h1)+1)
        
        
print(max(sizes.values()))

# 4750038360 too low



# part 2

# do rle
# for evey point caclulate rle right and left
# get max


# # Step 1: boundary
# lims = []

# for i in range(len(data)):
#     w0, h0 = data[i]
#     w1, h1 = data[(i + 1) % len(data)]

#     if w0 == w1:
#         step = 1 if h1 >= h0 else -1
#         for j in range(h0, h1 + step, step):
#             lims.append((w0, j))

#     elif h0 == h1:
#         step = 1 if w1 >= w0 else -1
#         for j in range(w0, w1 + step, step):
#             lims.append((j, h0))

# # Step 2: fill using scanlines
# filled = set(lims)

# from collections import defaultdict

# # boundary → rows dictionary
# rows = defaultdict(list)
# for x, y in lims:
#     rows[y].append(x)

# # store spans per row instead of every pixel
# filled_rows = defaultdict(list)

# for y, xs in rows.items():
#     xmin, xmax = min(xs), max(xs)
#     filled_rows[y].append((xmin, xmax))

# lims = list(set(filled))
# print(lims)





# lims = list(set(lims))
# sizes = dict()
# for i in range(len(data)):
#     print(i, len(data))
#     w1, h1 = data[i]
#     for j in range(i + 1, len(data)):
#         w2, h2 = data[j]
#         if w1 == w2 or h1 == h2: 
#             sizes[(i, j)] = 0
#             continue
#         size = (abs(w2 - w1)+1) * (abs(h2 - h1)+1)
#         if size < max(sizes.values(), default=0):
#             continue


#         w3, h3 = w1, h2
#         w4, h4 = w2, h1
#         if (w3, h3) in lims and (w4, h4) in lims:
#             sizes[(i, j)] = size

# print(max(sizes.values()))


# # 136365126 too low


n = len(data)
max_area = 0

edges = [(data[i], data[(i + 1) % n]) for i in range(n)]

for i in range(n):
    x1, y1 = data[i]
    for j in range(i + 1, n):
        x2, y2 = data[j]

        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)

        intersects = False
        for (x3, y3), (x4, y4) in edges:
            if (max(y3, y4) > ymin and
                min(y3, y4) < ymax and
                max(x3, x4) > xmin and
                min(x3, x4) < xmax):
                intersects = True
                break

        if intersects:
            continue

        width  = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height

        if area > max_area:
            max_area = area

print(max_area)
