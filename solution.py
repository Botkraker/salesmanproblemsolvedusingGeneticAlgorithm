import random
from typing import List

from salesman import Salesman


class Solution:
    # route=[names...], distance int

    def __init__(self, route: List[str]):
        self.route = route
        self.distance: int = None

    def produce(self, parent):
        childsroute = []
        for index, currentNode in enumerate(self.route):
            if currentNode == parent.route[index]:
                childsroute.append(currentNode)
            else:
                # next is random choice from [parent1,parent2]
                childsroute.append(
                    random.choice(
                        [parent.route[index],
                         currentNode
                         ]))
        return Solution(route=childsroute)

    def mutate(self):
        # simple mutation
        x, y = random.sample(range(len(self.route)), 2)
        self.route[x], self.route[y] = self.route[y], self.route[x]

    def testSolution(self):
        self.distance = Salesman().testRoute(self.route)

    def show(self):
        print("{Route:", self.route, ",Distance:", self.distance, "}", end="")
