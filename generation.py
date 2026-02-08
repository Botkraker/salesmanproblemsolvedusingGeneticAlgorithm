import random
from solution import Solution
from typing import List, Optional
from salesman import Salesman


class Generation:
    # solutions= [solution...]

    def __init__(self, solutions: List[Solution]):
        self.solutions = solutions

    def sortByBestPerformingSolution(self):
        for solution in self.solutions:
            solution.testSolution()
        self.solutions.sort(key=lambda x: x.distance)

    def nextGeneration(self):
        self.sortByBestPerformingSolution()
        newGeneration = []

        if len(self.solutions) > 10:
            parentPool = self.solutions[:len(self.solutions)//2]
        else:
            parentPool = self.solutions[:]
        
        while len(parentPool) > 1:
            for _ in range(2):
                if not len(parentPool)<=3:
                    firstparent = random.randint(0, 3)
                    secondparent = random.randint(0, 3)
                else :
                    firstparent=0;secondparent=1
                child = self.solutions[firstparent].produce(
                    self.solutions[secondparent])
                child.mutate()
                newGeneration.append(child)
            parentPool.pop(secondparent if secondparent>firstparent else firstparent)
            parentPool.pop(firstparent if secondparent>firstparent else secondparent)
        return Generation(newGeneration+self.solutions[:len(parentPool)])

    def show(self):
        print("My 20 best-Performing Children : ", end="")
        for index, solution in enumerate(self.solutions[:20]):
            print(f"{index}:", end="")
            solution.show()
        print()
    @staticmethod
    def firstGeneration(popSize:Optional[int]=None):
        names = Salesman().getNodeNames()
        if popSize is None:
            popSize = len(names)
        gen = []
        for _ in range(popSize):
            lNames = names[:]
            random.shuffle(lNames)
            gen.append(Solution(lNames))
        return Generation(gen)
