import math


class City(object):
    """
    a representation of a city
    """

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def distance(self, other: "City") -> float:
        """distance between two cities"""
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"{self.name}({self.x}, {self.y})"
