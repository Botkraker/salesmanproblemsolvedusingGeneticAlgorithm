import random

from salesman import salesman


class solution:
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
                childsroute.append()


class generation:
    # solutions= [solution...]
    def __init__(self, solutions):
        self.solutions = solutions

    # def
