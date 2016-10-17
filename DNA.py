import string
import random
from difflib import SequenceMatcher


class DNA:
    fitness = 0
    geneCount = 0

    genes = []

    def __init__(self, _genecount):
        self.geneCount = _genecount
        self.genes = [None] * self.geneCount

    def randomize(self):
        for i in range(0, self.geneCount):
            self.genes[i] = random.choice(string.ascii_letters)

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def calcFitness(self, target):
        self.fitness = self.similar("".join(self.genes), target)

    def getFitness(self):
        return self.fitness

    def crossover(self, parent1):
        child = DNA(self.geneCount)
        midpoint = random.randint(0, self.geneCount)
        for i in range(0, self.geneCount):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = parent1.genes[i]
        return child

    def mutate(self, rate):
        for i in range(0, self.geneCount):
            if random.randint(0, 100) < rate:
                self.genes[i] = random.choice(string.ascii_letters)
