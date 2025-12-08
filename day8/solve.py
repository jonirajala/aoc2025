import os
import operator
import numpy as np
from functools import reduce
import re
import math
import itertools



with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = [(int(x), int(y), int(z)) for line in f.readlines() for x, y, z in [line.strip().split(',')]]

print(data)
pairs = list(itertools.combinations(data, 2))
print(pairs)

distance_dict = {}
for p1, p2 in itertools.combinations(data, 2):
    key = frozenset((p1, p2))      # unordered key
    distance_dict[key] = math.dist(p1, p2)

belongs_to_jucntion = dict()
junctions = dict()

for key, dist in sorted(distance_dict.items(), key=lambda x: x[1])[:1000]:
    p1, p2 = tuple(key)
    if p1 in belongs_to_jucntion.keys() and not p2 in belongs_to_jucntion.keys():
        junctions[belongs_to_jucntion[p1]].append(p2)
        belongs_to_jucntion[p2] = belongs_to_jucntion[p1]
    elif not p1 in belongs_to_jucntion.keys() and p2 in belongs_to_jucntion.keys():
        junctions[belongs_to_jucntion[p2]].append(p1)
        belongs_to_jucntion[p1] = belongs_to_jucntion[p2]
    elif p1 in belongs_to_jucntion.keys() and p2 in belongs_to_jucntion.keys():
        if belongs_to_jucntion[p1] == belongs_to_jucntion[p2]:
            pass
        else:
            # combine junctions
            a = belongs_to_jucntion[p1]
            b = belongs_to_jucntion[p2]

            a_junctions = junctions[a]
            b_junctions = junctions[b]
            
            k = max(belongs_to_jucntion.values(), default=0) + 1
            junctions[k] = a_junctions + b_junctions
            for j in a_junctions + b_junctions:
                belongs_to_jucntion[j] = k
            del junctions[a]
            del junctions[b]

    else:
        k = max(belongs_to_jucntion.values(), default=0) + 1
        belongs_to_jucntion[p1] = k
        belongs_to_jucntion[p2] = k
        junctions[k] = [p1, p2]

tots = []
for key, dist in sorted(junctions.items(), key=lambda x: len(x[1]), reverse=True)[:3]:
    tots.append(len(dist))

print(reduce(operator.mul, tots))


# part 2

i = 0
for key, dist in sorted(distance_dict.items(), key=lambda x: x[1]):
    print(i, len(distance_dict))

    p1, p2 = tuple(key)
    if p1 in belongs_to_jucntion.keys() and not p2 in belongs_to_jucntion.keys():
        junctions[belongs_to_jucntion[p1]].append(p2)
        belongs_to_jucntion[p2] = belongs_to_jucntion[p1]
    elif not p1 in belongs_to_jucntion.keys() and p2 in belongs_to_jucntion.keys():
        junctions[belongs_to_jucntion[p2]].append(p1)
        belongs_to_jucntion[p1] = belongs_to_jucntion[p2]
    elif p1 in belongs_to_jucntion.keys() and p2 in belongs_to_jucntion.keys():
        if belongs_to_jucntion[p1] == belongs_to_jucntion[p2]:
            pass
        else:
            # combine junctions
            a = belongs_to_jucntion[p1]
            b = belongs_to_jucntion[p2]

            a_junctions = junctions[a]
            b_junctions = junctions[b]
            
            k = max(belongs_to_jucntion.values(), default=0) + 1
            junctions[k] = a_junctions + b_junctions
            for j in a_junctions + b_junctions:
                belongs_to_jucntion[j] = k
            del junctions[a]
            del junctions[b]

    else:
        k = max(belongs_to_jucntion.values(), default=0) + 1
        belongs_to_jucntion[p1] = k
        belongs_to_jucntion[p2] = k
        junctions[k] = [p1, p2]

    if len(junctions) == 1 and len(belongs_to_jucntion) == len(data):
        break

    i += 1

print(key, len(belongs_to_jucntion), len(junctions))
p1, p2 = tuple(key)
print(p1[0] * p2[0])


# 1282052331 too low
# 6995409267 too high
