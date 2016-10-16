import DNA
from decimal import Decimal
import random


class Population:
    target = ""
    mutationRate = 0
    popMax = 0
    length = None

    finishedEvolving = False
    generations = 0

    population = []
    genePool = []

    closestString = ""

    def __init__(self, _target, _mutationrate, _popmax):
        self.target = _target
        self.mutationRate = _mutationrate
        self.popMax = _popmax
        self.length = len(_target)

        for i in range(0, self.popMax):
            self.population.append(DNA.DNA(self.length))
            self.population[i].randomize()

        for j in range(0, self.popMax):
            print("".join(self.population[j].genes))

    def calcFitness(self):
        for i in range(0, self.popMax):
            self.population[i].calcFitness(self.target)


    def naturalSelection(self):
        maxfitness = 0
        index = 0
        for i in range(0, self.popMax):
            if self.population[i].getFitness() > maxfitness:
                maxfitness = self.population[i].getFitness()
                self.closestString = "".join(self.population[i].genes)

            currentfitness = (100 * round(Decimal(self.population[i].getFitness()), 2))
            currentfitness = int(currentfitness)

            print("".join(self.population[i].genes))

            for j in range(index, (index + currentfitness)):
                self.genePool.append(i)

            index += currentfitness


    def generate(self):
        for i in range(0, self.popMax):
            #poolsize = len(self.genePool)
            index0 = random.choice(self.genePool)
            index1 = random.choice(self.genePool)

            parent0 = self.population[index0]
            parent1 = self.population[index1]

            child = parent0.crossover(parent1)
            self.population[i] = child

        self.generations += 1
        print(self.generations)
        self.genePool = []


    def evaluate(self):
        print(self.closestString)
        if self.closestString == self.target:
            return True
        else:
            return False
