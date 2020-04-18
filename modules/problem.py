import math

N_QUEENS = 10
WORST_CASE = N_QUEENS * (N_QUEENS - 1) / 2

def f(chromossome):
    genes = chromossome.get_genes()

    attacks = 0
    for column_chr1 in range(N_QUEENS):
        chr1_coordinates = (column_chr1, genes[column_chr1])

        for column_chr2 in range(column_chr1 + 1, N_QUEENS):
            chr2_coordinates = (column_chr2, genes[column_chr2])

            delta_x = chr2_coordinates[0] - chr1_coordinates[0]
            delta_y = chr2_coordinates[1] - chr1_coordinates[1]

            angle_chromossomes = math.atan2(delta_y, delta_x)
            angle_chromossomes = math.degrees(angle_chromossomes)
            angle_chromossomes = abs(angle_chromossomes)

            if angle_chromossomes == 0 or angle_chromossomes == 45:
                attacks += 1

    return attacks

# Fitness
def g(chromossome):
    return WORST_CASE - f(chromossome)

def f_average(population):
    avg = 0

    for chromossome in population:
        avg += f(chromossome)

    avg /= len(population)

    return avg

def g_average(population):
    avg = 0

    for chromossome in population:
        avg += g(chromossome)

    avg /= len(population)

    return avg