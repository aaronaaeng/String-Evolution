import DNA


class Population:
    target = None
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


   # def calcFitness(self):


    def naturalSelection(self):
        maxfitness = 0
        for i in range (0, len(self.population)):
            if self.population[i].getFitness() > maxfitness:
                maxfitness = self.population[i].getFitness()


   # def generate(self):


  #  def evaluate(self):
