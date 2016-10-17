import Population


def main():
    target = "Hello"
    mutationRate = 3
    popMax = 100

    population = Population.Population(target, mutationRate, popMax)

    draw(population)


def draw(population):
    finished = False
    while not finished:

        population.calcFitness()

        population.naturalSelection()

        population.generate()

        finished = population.evaluate()


main()
