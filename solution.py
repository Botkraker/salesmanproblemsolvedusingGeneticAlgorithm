import random
from typing import List

from salesman import Salesman


class Solution:
    salesman = Salesman()
    # route=[names...], distance int

    def __init__(self, route:List[str], distance:int):
        self.route = route
        self.distance = distance

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
    def mutate(self,route):
        # simple mutation
        x, y = random.randint(0, len(route)), random.randint(
            0, len(route))
        route[x], route[y] = route[y], route[x]
    def testSolution(self):
        self.distance = Salesman.testRoute(self.route)
