from typing import List
from generation import Generation

class GeneticsAlgorithm:
    # FirstGeneration is optional if you want to set the first generation instead of random generation
    def __init__(self, firstgeneration:List[Generation]=None):
        if firstgeneration != None:
            self.generations:List[Generation] = [firstgeneration]
        else:
            self.generations:List[Generation] = [Generation.firstGeneration()]
    def show(self):
        print("Generation N:",len(self.generations)-1)
        self.generations[-2].show()
    def run(self):
        for i in range(10):
            self.generations.append(self.generations[-1].nextGeneration())
            self.show()

