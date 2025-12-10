import os
import itertools
from collections import Counter


parse_lights = lambda s: list(s.strip("[]"))
parse_tuple  = lambda s: tuple(map(int, s.strip("()").split(",")))
parse_set    = lambda s: list(map(int, s.strip("{}").split(",")))

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

with open(file_path) as f:
    data = [
        (
            parse_lights(parts[0]),
            [parse_tuple(b) for b in parts[1:-1]],
            parse_set(parts[-1])
        )
        for parts in (line.strip().split(" ") for line in f)
    ]

# part 1

tot = 0

for lights, buttons, jolt in data:
    on_indexes  = [i for i, val in enumerate(lights) if val == '#']

    all_combos = []
    for r in range(1, len(buttons)+1):
        all_combos.extend(itertools.combinations(buttons, r))
    min_val = float('inf')
    for combo in all_combos:
        presses = len(combo)
        counts = Counter(x for tup in combo for x in tup)
        odd_values = [key for key, count in counts.items() if count % 2 == 1]
        if sorted(odd_values) == sorted(on_indexes):
            if min_val > presses:
                min_val = presses
    
    tot += min_val
print(tot)

# part 2

import pulp


def solve_ilp(buttons, jolts):
    num_buttons = len(buttons)
    num_dims = len(jolts)

    jolts = list(jolts)

    prob = pulp.LpProblem("Button_Press_Optimization", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat='Integer') for i in range(num_buttons)]
    prob += pulp.lpSum(x)

    for d in range(num_dims):
        prob += pulp.lpSum(x[i] if d in buttons[i] else 0
                           for i in range(num_buttons)) == jolts[d]

    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

    if status != pulp.LpStatusOptimal:
        print("No solution found")
        return None  # No solution

    total_presses = sum(v.value() for v in x)
    press_counts = [v.value() for v in x]
    return total_presses, press_counts

tot = 0
for lights, buttons, jolts in data:
    total_presses, press_counts = solve_ilp(buttons, jolts)
    tot += total_presses
print(tot)