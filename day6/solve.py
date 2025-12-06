import os
import operator
import numpy as np
from functools import reduce
import re


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data.txt"), "r") as f:
    data = [line.strip().split() for line in f.readlines()]


operators = data[-1]
data = np.array(data[:-1])

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

# part 1

tot = 0
for i in range(len(data[0])):
    operands = [int(x) for x in data[:,i]]  # convert every item to int
    tot += reduce(ops[operators[i]], operands)
print(tot)

# part 2
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = [line.rstrip("\n") for line in f.readlines()]

tot = 0
a = []
for i in range(-1, -len(data[0]) - 1, -1):
    n = ""
    for j in range(len(data) -1):
        if data[j][i] != " ":
            n += data[j][i]

    if n != "":
        a.append(n)

    if data[-1][i] != " ":
        tot += reduce(ops[data[-1][i]], [int(x) for x in a])
        a = []

print(tot)
