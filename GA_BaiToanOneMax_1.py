# làm lại bài toán one max bằng cách khác

import random
import matplotlib.pyplot as plt

n = 10   # so gen trong nst
m = 10  # so nst trong quan the
n_generation = 10   # so doi

fitnesses_map = []  # dung de ve bieu do

def gene_value():
    return random.randint(0, 1)

# tao nhiem sac the ngau nhien
def create_random_individual():
    return [gene_value() for _ in range(n)]

# tinh do thich nghi
def calculate_fitness(individual):
    return sum(individual)

# tao quan the ban dau
def create_population():
    return [create_random_individual() for _ in range(m)]

# tao mang luu do thich nghi
def create_fitnesses(population):
    return [calculate_fitness(population[i]) for i in range(m)]

# dot bien voi kha nang la 5%
def mutate(individual, mutate_rate = 0.05):
    if random.random() < mutate_rate:
        index = random.randint(0, n-1)
        individual[index] = 1 - individual[index]
    return individual

# lai ghep voi kha nang la 90%
def crossoer(individual1, individual2, crossoer_rate = 0.9):
    individual_c1 = individual1.copy()
    individual_c2 = individual2.copy()
    if random.random() < crossoer_rate:
        index = random.randint(1, n - 1)
        for i in range(index):
            individual_c1[i] = individual2[i]
            individual_c2[i] = individual1[i]
    return individual_c1, individual_c2

# lua chon theo kieu quay banh xe so
def seletion(fitnesses):
    s = sum(fitnesses)
    ran = random.randint(0, s)
    s1 = 0
    index = 0
    for i in range(m):
        s1 += fitnesses[i]
        if s1 >= ran:
            index = i
    return index

# tao quan the moi
def create_new_population(old_population, fitnesses):
    sorted_fitnesses = sorted(fitnesses)
    sorted_old_population = sorted(old_population, key = calculate_fitness)
    # in ra nst tot nhat
    print('best: ', sorted_fitnesses[m - 1])
    fitnesses_map.append(sorted_fitnesses[m - 1])
    new_population = []
    for _ in range(int(m / 2)):
        # lua chon
        individual1 = sorted_old_population[seletion(sorted_fitnesses)]
        individual2 = sorted_old_population[seletion(sorted_fitnesses)]

        # lai ghep
        individual_c1, individual_c2 = crossoer(individual1, individual2)

        # dot bien
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        # dua vao quan the moi
        new_population.append(individual_m1)
        new_population.append(individual_m2)
    return new_population

# main
population = create_population()
fitnesses = create_fitnesses(population)
for _ in range(n_generation):
    population = create_new_population(population, fitnesses)
    fitnesses = create_fitnesses(population)
plt.plot(fitnesses_map)
plt.show()