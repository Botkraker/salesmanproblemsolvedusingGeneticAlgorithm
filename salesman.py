from math import inf

from node import node


class salesman:
    _instance = None
    # nodes= {name:node...}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, nodes, startNode):
        if hasattr(self, '_initialized') and self._initialized:
            return

        self.startNode = startNode
        self.nodes = nodes
        self._initialized = True

    def testRoute(self, route):
        currentnode = self.startNode
        traveledDistance = 0
        for nextnode in route:
            traveledDistance += currentnode.goToNeighbor(nextnode)
            currentnode = self.nodes[nextnode]
        try:
            traveledDistance += currentnode.goToNeighbor(self.startNode.name)
        except Exception:
            print("this route doesn't end at the starting point")
            return inf
        return traveledDistance

    