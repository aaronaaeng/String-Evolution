import Population


def main():
    target = input("Enter target string: ")
    pop_max = int(input("Enter population size: "))
    mutation_rate = int(input("Enter mutation rate: "))
    finished = False

    population = Population.Population(target, mutation_rate, pop_max)

    while not finished:
        population.calc_population_fitness()
        population.create_gene_pool()
        population.create_generation()
        finished = population.evaluate()

if __name__ == '__main__':
    main()
