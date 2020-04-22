MUTATION_PROBABILITY = 0.05

import random

from modules import problem
from modules.genetics import utils
from modules.genetics.chromossome import Chromossome

def selection(population):
    # Fitness proportionate selection AKA roulette wheel selection
    # https://en.wikipedia.org/wiki/Fitness_proportionate_selection

    chromossome_roulette = []

    population_fitness = problem.g_average(population)

    previous_probability = 0
    for chromossome in population:
        chromossome_probability = previous_probability + (problem.g(chromossome) / population_fitness)

        chromossome_roulette.append((chromossome, chromossome_probability))

        previous_probability = chromossome_probability

    parents = [None] * 2

    for i in range(2):
        random_number = random.uniform(0, 1)

        for bet in chromossome_roulette:
            chromossome, probability = bet

            if random_number < probability:
                parents[i] = chromossome
                chromossome_roulette.remove(bet)

                break

    print(f"1st parent chosen for crossover: {utils.format_chromossome(parents[0])}")
    print(f"2nd parent chosen for crossover: {utils.format_chromossome(parents[1])}")

    return parents

def crossover(population, parent1, parent2):
    # K-point crossover
    # https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)#Two-point_and_k-point_crossover

    k = random.randint(1, problem.N_QUEENS - 1)

    crossover_points = []
    for _ in range(k):
        point = random.randint(1, problem.N_QUEENS - 1)

        while point in crossover_points:
            point = random.randint(1, problem.N_QUEENS - 1)

        crossover_points.append(point)

    crossover_points.sort()

    crossover_points_str = ", ".join(map(str, crossover_points))
    print(f"{k} crossover(s) will happen at point(s) {crossover_points_str}")

    crossover_points.append(problem.N_QUEENS)

    parents_genes = [parent1.get_genes(), parent2.get_genes()]

    child1_genes = [None] * problem.N_QUEENS
    child2_genes = [None] * problem.N_QUEENS

    last_point = 0
    parent_control = 0
    for point in crossover_points:
        child1_genes[last_point:point] = parents_genes[parent_control][last_point:point]
        child2_genes[last_point:point] = parents_genes[not parent_control][last_point:point]

        last_point = point
        parent_control = not parent_control

    child1 = Chromossome()
    child1.set_genes(child1_genes)
    print(f"1st child generated from crossover: {utils.format_chromossome(child1)}")

    child2 = Chromossome()
    child2.set_genes(child2_genes)
    print(f"2nd child generated from crossover: {utils.format_chromossome(child2)}")

    population.append(child1)
    population.append(child2)

def mutation(population):
    # Swap mutation

    prob = random.uniform(0, 1)

    if prob >= MUTATION_PROBABILITY:
        return

    target = random.choice(population)

    mutation_point_1 = mutation_point_2 = -1
    while mutation_point_1 == mutation_point_2:
        mutation_point_1 = random.randint(0, problem.N_QUEENS - 1)
        mutation_point_2 = random.randint(0, problem.N_QUEENS - 1)

    print(f"Invididual {target.to_string()} will mutate at points ({mutation_point_1}, {mutation_point_2})")

    genes = target.get_genes()
    genes[mutation_point_1], genes[mutation_point_2] = genes[mutation_point_2], genes[mutation_point_1]

    print(f"Individual {target.to_string()} mutated at points ({mutation_point_1}, {mutation_point_2})")

def elitism(population):
    for _ in range(2):
        worst_individual = utils.find_worst_chromossome(population)
        print(f"Removing worst individual from population: {utils.format_chromossome(worst_individual)}")
        population.remove(worst_individual)