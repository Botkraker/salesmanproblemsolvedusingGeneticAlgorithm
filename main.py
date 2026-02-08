from node import node 
from salesman import salesman

A = node('A', {"B": 10, "C": 15, "D": 20})
B = node('B', {'A': 10, 'C': 35, 'D': 25})
C = node('C', {'A': 15, 'B': 35, 'D': 30})
D = node('D', {'A': 20, 'B': 25, 'C': 30})

nodes = {
    'A': A,
    'B': B,
    'C': C,
    'D': D
}

s = salesman(nodes, A)

routes = [
    ['B', 'C', 'D'],
    ['C', 'B', 'D'],
    ['D', 'B', 'C'],
    ['B', 'D', 'C'],
    ['B', 'C'],         # invalid (does not return properly)
]

for r in routes:
    print(f'Route A -> {r} -> A = {s.testRoute(r)}')
