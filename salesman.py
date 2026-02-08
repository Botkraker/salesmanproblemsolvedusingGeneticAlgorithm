

from typing import List

from node import Node


class Salesman:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    # nodes= {name:node...}
    def __init__(self, nodes:dict[str,Node]=None, startNode:Node=None):
        if self._initialized:
            return

        if nodes is not None and startNode is not None:
            self.initialize(nodes, startNode)

    def initialize(self, nodes:dict[str,Node], startNode:Node):
        if self._initialized:
            return

        self.nodes = nodes
        self.startNode = startNode
        self._initialized = True

    def testRoute(self, route: List[str]):
        currentnode = self.startNode
        traveledDistance = 0
        for nextnode in route:
            traveledDistance += currentnode.goToNode(self.nodes[nextnode])
            currentnode = self.nodes[nextnode]
        traveledDistance += currentnode.goToNode(self.startNode)
        return traveledDistance

    def getNodeByName(self, name):
        if name not in self.nodes.keys():
            raise Exception("NameNode doesn't exists")
        return self.nodes[name]

    def getNodeNames(self):
        l=list(self.nodes.keys())
        l.remove(self.startNode.name)
        return l

    def getStartNode(self):
        return self.startNode
