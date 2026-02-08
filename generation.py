import random
from solution import Solution
from typing import List
from salesman import Salesman


class Generation:
    salesman = Salesman()
    # solutions= [solution...]

    def __init__(self, solutions: List[Solution]):
        self.solutions = solutions

    def sortByBestPerformingSolution(self):
        self.solutions.foreach(lambda x: x.testSolution())
        self.solutions.sort(key=lambda x: x.distance)

    def nextGeneration(self):
        newGeneration = []
        parentPool = self.solutions[:len(self.solutions)]
        while len(parentPool) < 3:
            firstparent = random.randint(0, 3)
            secondparent = random.randint(0, 3)
            child=self.solutions[firstparent].produce(
                    self.solutions[secondparent])
            child.mutate()
            newGeneration.append(child)
            parentPool.pop(firstparent)
            parentPool.pop(secondparent)
        return Generation(newGeneration+self.solutions[:len(parentPool)])

    def firstGeneration(numberOfSolution=None):
        names=Salesman.getNodeNames()
        if numberOfSolution == None:
            numberOfSolution = len(names)/2
        gen = []
        for _ in range(numberOfSolution):
            gen.append(random.shuffle(names))
        return Generation(gen)
