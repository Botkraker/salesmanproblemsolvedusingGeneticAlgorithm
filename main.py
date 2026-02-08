from node import Node 
from salesman import Salesman

A = Node('A', (0,0)) 
B = Node('B', (5,5))
C = Node('C', (4,-6))
D = Node('D', (8,8))

nodes = {
    'A': A,
    'B': B,
    'C': C,
    'D': D
}

s = Salesman(nodes, A)

routes = [
    ['B', 'C', 'D'],
    ['C', 'B', 'D'],
    ['D', 'B', 'C'],
    ['B', 'D', 'C'],
    ['B', 'C'],        
]

for r in routes:
    print(f'Route A -> {r} -> A = {s.testRoute(r)}')
