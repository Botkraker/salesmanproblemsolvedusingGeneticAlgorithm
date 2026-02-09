import random
from solution import Solution
from typing import List, Optional
from salesman import Salesman


class Generation:
    # solutions= [solution...]

    def __init__(self, solutions: List[Solution]):
        self.solutions = solutions

    def sortByBestPerformingSolution(self):
        self.solutions.sort(key=lambda x: x.testSolution())

    def select(self,k=3):
        tournamnet = random.sample(self.solutions,k)
        self.solutions.sort(key=lambda x: x.testSolution())
        return tournamnet[0]

    def nextGeneration(self,popSize=10):
        newGeneration = []

        for _ in range(popSize):
                parent1=self.select()
                parent2=self.select()
                child =parent1.produce(parent2)
                child.mutate()
                newGeneration.append(child)
        return Generation(newGeneration)

    def show(self):
        print("My 20 best-Performing Children : ", end="")
        for index, solution in enumerate(self.solutions[:20]):
            print(f"{index}:", end="")
            solution.show()
        print()
    def get_top_routes(self,num:int):
        self.sortByBestPerformingSolution()
        return self.solutions[:num]
    
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
