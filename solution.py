import random
from typing import List

from salesman import Salesman


class Solution:
    # route=[names...], distance int

    def __init__(self, route: List[str]):
        self.route = route
        self.distance: float = 0

    def produce(self, parent):
        childroute= [None] * len(self.route)
        start= random.randint(1,len(self.route)-2)
        end = random.randint(start,len(self.route)-1)
        childroute[start:end]=self.route[start:end]
        setChildNodes=set(self.route[start:end])
        genesMissing = [n for n in parent.route if n not in setChildNodes]

        index =0
        for gene in genesMissing:
            while childroute[index] is not None:
                index+=1
            childroute[index]=gene
        return Solution(route=childroute)
    
    def mutate(self,factor=0.1):
        # simple mutation
        while random.random()<factor:
            x, y = random.sample(range(len(self.route)), 2)
            self.route[x], self.route[y] = self.route[y], self.route[x]

    def testSolution(self):
        self.distance = Salesman().testRoute(self.route)
        return self.distance 

    def show(self):
        print("{Route:", self.route, ",Distance:", self.distance, "}", end="")
