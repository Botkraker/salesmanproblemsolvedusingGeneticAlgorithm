import math
from typing import Tuple


class Node:
    def __init__(self, name: str, coords:Tuple[int,int]):
        self.name = name
        self.coords = coords

    def goToNode(self, nextNode:"Node"):
        return self.distance(nextNode)

    def distance(self, nextNode:"Node"):
        return math.sqrt((self.coords[0]-nextNode.coords[0])**2+((self.coords[1]-nextNode.coords[1])**2))
