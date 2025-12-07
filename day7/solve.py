import os
import operator
import numpy as np
from functools import reduce
import re


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = [line.strip() for line in f.readlines()]

start = data[0].index('S')


# part 1

splits = 0
beams = [start]
for i in range(1, len(data)):
    new_beams = []
    for beam in beams:
        if data[i][beam] == "^":
            if beam - 1 >= 0 and beam - 1 not in new_beams:
                new_beams.append(beam - 1)
            if beam + 1 < len(data[i]) and beam + 1 not in new_beams:
                new_beams.append(beam + 1)
            splits += 1
        elif beam not in new_beams:
            new_beams.append(beam)
    beams = new_beams

print(splits)

# part 2

beams = {start: 1}
for i in range(1, len(data)):
    new_beams = dict()
    for beam, count in beams.items():
        moves = []
        if data[i][beam] == "^":
            if beam - 1 >= 0:
                moves.append(beam - 1)
            if beam + 1 < len(data[i]):
                moves.append(beam + 1)
        else:
            moves.append(beam)
        for m in moves:
            new_beams[m] = new_beams.get(m, 0) + count

    beams = new_beams

print(sum(beams.values()))
