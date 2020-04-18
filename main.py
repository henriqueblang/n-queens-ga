import matplotlib.pyplot as plt

import modules.genetics.operators as operators
import modules.problem as problem
import modules.genetics.utils as utils
from modules.genetics.chromossome import Chromossome

if __name__ == "__main__":
    population = [Chromossome() for _ in range(10)]

    generation = 0
    population_score = problem.g_average(population)
    print(f"Generation # {generation} -> Average population score = {population_score:.3f}\n")

    generation_plot = []
    generation_plot.append(generation)

    population_score_plot = []
    population_score_plot.append(population_score)

    while generation < 50:
        parent1, parent2 = operators.selection(population)

        operators.crossover(population, parent1, parent2)
        operators.mutation(population)
        operators.elitism(population)

        generation += 1
        population_score = problem.g_average(population)

        generation_plot.append(generation)
        population_score_plot.append(population_score)

        print(f"Generation # {generation} -> Average population score = {population_score:.3f}\n")

    best_chromossome = utils.find_best_chromossome(population)
    print(f"Best individual: {utils.format_chromossome(best_chromossome)}")

    board = Chromossome.get_fenotype(best_chromossome.get_genes())

    for row in range(problem.N_QUEENS):
        row_str = ""

        for column in range(problem.N_QUEENS):
            row_str += str(int(board[row][column])) + " "

        print(row_str)
    
    plt.gca().set_xlabel("Generation")
    plt.gca().set_ylabel("Average fitness")
    plt.gca().set_title("Average fitness per generation")
    plt.plot(generation_plot, population_score_plot)
    plt.show()