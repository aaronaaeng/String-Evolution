import DNA
from decimal import Decimal


class Population:
    target = ""
    mutationRate = None
    popMax = None

    finishedEvolving = False
    generations = 0

    population = []
    genePool = []

    closestString = ""

    def _init_(self, _target, _mutationrate, _popmax):
        self.target = _target
        self.mutationRate = _mutationrate
        self.popMax = _popmax
        for i in range(0, self.popMax):
            self.population[i] = DNA.DNA(len(self.target))


    #def calcFitness(self):


    def naturalSelection(self):
        maxfitness = 0
        index = 0
        for i in range(0, len(self.population)):
            if self.population[i].getFitness() > maxfitness:
                maxfitness = self.population[i].getFitness()
        for j in range(0, self.popMax):
            currentfitness = (100 * round(Decimal(self.population[j].getFitness()), 2))
            for k in range(index, (index + currentfitness)):
                self.genePool[k] = j
            index += currentfitness

    #def generate(self):


    #def evaluate(self):
