import os
from collections import defaultdict, deque

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt"), "r") as f:
    data = [(x, y.split(" ")) for line in f.readlines() for x, y in [line.strip().split(": ")]]
    data = dict(data)

print(data)


# part 1
def count_paths(start, end, graph):

    memo = {}
    visiting = set()

    def dfs(node):
        if node == end:
            return 1
        
        if node in memo:
            return memo[node]
        
        if node in visiting:
            return float('inf')

        visiting.add(node)
        total = 0
        
        for nxt in graph[node]:
            res = dfs(nxt)
            if res == float('inf'):
                return float('inf')
            total += res
        
        visiting.remove(node)
        memo[node] = total
        return total
    
    result = dfs(start)
    return result, (result == float('inf'))


print(count_paths("you", "out", data))


# part 2 

def count_paths(start, end, graph, required_nodes):
    required_nodes = set(required_nodes)

    memo = {}
    visiting = set()

    def dfs(node, visited_req):
        if node in required_nodes:
            visited_req = visited_req | {node}

        if node == end:
            return 1 if visited_req == required_nodes else 0

        state = (node, frozenset(visited_req))

        if state in memo:
            return memo[state]

        if state in visiting:
            return float('inf')

        visiting.add(state)
        total = 0

        for nxt in graph[node]:
            res = dfs(nxt, visited_req)
            if res == float('inf'):
                return float('inf')
            total += res

        visiting.remove(state)
        memo[state] = total
        return total
    
    result = dfs(start, frozenset())
    return result, (result == float('inf'))

print(count_paths("svr", "out", data, ["dac", "fft"]))