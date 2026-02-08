import random
from solution import Solution
from typing import List
from salesman import Salesman


class Generation:
    # solutions= [solution...]

    def __init__(self, solutions: List[Solution]):
        self.solutions = solutions

    def sortByBestPerformingSolution(self):
        self.solutions.foreach(lambda x: x.testSolution())
        self.solutions.sort(key=lambda x: x.distance)

    def nextGeneration(self):
        newGeneration = []
        parentPool = self.solutions[:len(self.solutions)//2]
        while len(parentPool) > 3:
            firstparent = random.randint(0, 3)
            secondparent = random.randint(0, 3)
            child=self.solutions[firstparent].produce(
                    self.solutions[secondparent])
            child.mutate()
            newGeneration.append(child)
            parentPool.pop(firstparent)
            parentPool.pop(secondparent)
        return Generation(newGeneration+self.solutions[:len(parentPool)])
    def show(self):
        print("My 20 best-Performing Children : ",end="")
        for index,solution in enumerate(self.solutions[:20]):
            print(f"{index}:",end="")
            print(solution)
            solution.show()
    def firstGeneration(numberOfSolution=None):
        names=Salesman().getNodeNames()
        if numberOfSolution == None:
            numberOfSolution = len(names)
        gen = []
        for _ in range(numberOfSolution):
            l=names
            random.shuffle(l)
            gen.append(Solution(l))
        return Generation(gen)
