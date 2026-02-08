import random
from typing import List

from salesman import Salesman


class Solution:
    # route=[names...], distance int

    def __init__(self, route: List[str]):
        self.route = route
        self.distance: float = 0

    def produce(self, parent):
        childroute= [str | None] * len(self.route)
        childroute[0]= self.route[0]
        s= random.randint(1,len(self.route)-2)
        e = random.randint(s,len(self.route)-1)
        childroute[s:e]=self.route[s:e]
        setChildNodes=set(self.route[s:e])
        fill = [n for n in parent.route if n not in setChildNodes]
        i =0
        for n in fill:
            while childroute[i] is not None:
                i+=1
            childroute[i]=n
        return Solution(route=childroute)
    
    def mutate(self,factor=0.1):
        # simple mutation
        while random.random()<factor:
            x, y = random.sample(range(len(self.route)), 2)
            self.route[x], self.route[y] = self.route[y], self.route[x]

    def testSolution(self):
        self.distance = Salesman().testRoute(self.route)

    def show(self):
        print("{Route:", self.route, ",Distance:", self.distance, "}", end="")
