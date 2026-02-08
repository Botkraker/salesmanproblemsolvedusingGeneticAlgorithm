

class Salesman:
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
            traveledDistance += currentnode.goToNode(self.nodes[nextnode])
            currentnode = self.nodes[nextnode]
        traveledDistance += currentnode.goToNode(self.startNode)
        return traveledDistance

    def getNodeByName(self, name):
        if name not in self.nodes.keys():
            raise Exception("NameNode doesn't exists")
        return self.nodes[name]
    def getNodeNames(self):
        return self.nodes.keys()
    def getStartNode(self):
        return self.firstNode