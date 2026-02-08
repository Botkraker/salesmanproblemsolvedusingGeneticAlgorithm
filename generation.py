from solution import Solution

class Generation:
    # solutions= [solution...]
    def __init__(self, solutions):
        self.solutions = solutions

    def sortByBestPerformingSolution(self):
        self.solutions.foreach(lambda x: x.testSolution())
        self.solutions.sort(key=lambda x: x.distance)

    def nextGeneration(self, numberOfParents=10):
        newGeneration = []
        for firstparent in range(numberOfParents):
            for secondparent in range(firstparent, numberOfParents):
                newGeneration.append(
                    self.solutions[firstparent].produce(
                        self.solutions[secondparent]))
        return Generation(newGeneration)

    def firstGeneration(numberOfSolution=500):
        gen=[]
        for _ in range(numberOfSolution):
            pass   
        return Generation(gen)

