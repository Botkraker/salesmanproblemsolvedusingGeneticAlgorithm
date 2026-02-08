import math
class Node:
    def __init__(self, name, coords):
        self.name = name
        self.coords= coords

    def goToNode(self, nextNode):
        return math.sqrt((self.coords[0]-nextNode.coords[0])**2+((self.coords[1]-nextNode.coords[1])**2))
    def getMinDistanceNeighbor(self):
        return min(self.neighbors)
