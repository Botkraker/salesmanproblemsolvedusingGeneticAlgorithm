from generation import Generation

class GeneticsAlgorithm:
    # FirstGeneration is optional if you want to set the first generation instead of random generation
    def __init__(self, firstgeneration=None):
        if firstgeneration != None:
            self.generations = [firstgeneration]
        else:
            self.generations = [Generation.firstGeneration()]

    def run():
        pass
