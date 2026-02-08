import random

from salesman import Salesman


class Solution:
    salesman = Salesman()
    # route=[names...], distance int

    def __init__(self, route, distance):
        self.route = route
        self.distance = distance

    def produce(self, parent):
        childsroute = []
        for index, currentNode in enumerate(self.route):
            if currentNode == parent.route[index]:
                childsroute.append(currentNode)
            else:
                # next is random choice from [parent1,parent2,shortest distant neighbor]
                childsroute.append(
                    random.choice(
                        [parent.route[index],
                         currentNode,
                         Salesman
                         .getNodeByName(childsroute[-1])
                         .getMinDistanceNeighbor()]))
        return Solution(route=childsroute)

    def testSolution(self):
        self.distance = Salesman.testRoute(self.route)

