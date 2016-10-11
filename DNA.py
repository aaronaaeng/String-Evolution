import string
import random
from difflib import SequenceMatcher


class DNA:
    fitness = 0
    geneCount = None

    genes = []

    def _init_(self, _genecount):
        self.geneCount = _genecount
        for i in range(0, self.geneCount):
            self.genes[i] = random.choice(string.ascii_letters)

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def calcFitness(self, target):
        self.fitness = self.similar("".join(self.genes), target)


    def getFitness(self):
        return self.fitness
