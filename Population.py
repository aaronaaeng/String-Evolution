import DNA
from decimal import Decimal
import random


class Population:
    Target = ""
    MutationRate = None
    PopMax = None
    Length = None

    FinishedEvolving = False
    Generations = 0

    Population = []
    GenePool = []

    ClosestString = ""

    def __init__(self, _target, _mutationrate, _popmax):
        self.Target = _target
        self.MutationRate = _mutationrate
        self.PopMax = _popmax
        self.Length = len(_target)

        for i in range(0, self.PopMax):
            self.Population.append(DNA.DNA(self.Length))
            self.Population[i].randomize()

    def calc_population_fitness(self):
        for i in range(0, self.PopMax):
            self.Population[i].calc_personal_fitness(self.Target)

    def create_gene_pool(self):
        max_fitness = 0
        index = 0
        for i in range(0, self.PopMax):
            if self.Population[i].get_fitness() > max_fitness:
                max_fitness = self.Population[i].get_fitness()
                self.ClosestString = "".join(self.Population[i].Genes)

            current_fitness = int(100 * round(Decimal(self.Population[i].get_fitness()), 2))

            for j in range(index, (index + current_fitness)):
                self.GenePool.append(i)

            index += current_fitness

    def create_generation(self):
        for i in range(0, self.PopMax):
            first_index = random.choice(self.GenePool)
            second_index = random.choice(self.GenePool)

            first_parent = self.Population[first_index]
            second_parent = self.Population[second_index]

            child = first_parent.crossover(second_parent)
            self.Population[i] = child
            self.Population[i].mutate(self.MutationRate)
            print("".join(self.Population[i].Genes))

        self.Generations += 1
        print(self.Generations)
        self.GenePool = [0]

    def evaluate(self):
        print(self.ClosestString)
        if self.ClosestString == self.Target:
            return True
        else:
            return False
