import string
import random


class DNA:
    fitness = 0
    geneCount = 0

    Genes = []

    def __init__(self, _genecount):
        self.geneCount = _genecount
        self.Genes = [None] * self.geneCount

    def randomize(self):
        for i in range(0, self.geneCount):
            ascii_value = random.randint(31, 127)
            self.Genes[i] = chr(ascii_value)

    def calc_personal_fitness(self, target):
        matches = 0
        target_list = list(target)

        for i in range(0, self.geneCount):
            if self.Genes[i] == target_list[i]:
                matches += 1

        self.fitness = matches / float(self.geneCount)

    def get_fitness(self):
        return self.fitness

    def crossover(self, parent1):
        child = DNA(self.geneCount)
        midpoint = random.randint(0, self.geneCount)
        for i in range(0, self.geneCount):
            if i > midpoint:
                child.Genes[i] = self.Genes[i]
            else:
                child.Genes[i] = parent1.Genes[i]
        return child

    def mutate(self, rate):
        for i in range(0, self.geneCount):
            if random.randint(0, 100) < rate:
                self.Genes[i] = random.choice(string.ascii_letters)
