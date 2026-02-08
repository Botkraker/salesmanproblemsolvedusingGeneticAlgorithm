

class node:
    # neighbors = {"name" : distance}
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

    def goToNeighbor(self, name):
        if name in self.neighbors.keys():
            return self.neighbors[name]
        else:
            raise Exception(f"{name} is not a neighbor")
