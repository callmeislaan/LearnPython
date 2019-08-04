# ham sphere: f(x) = x1^2 + x2^2 + x3^2 + x4^2 + x5^2 + x6^2 --> min
# voi -20 <= x <= 20 va x thuoc R

import random
import matplotlib.pyplot as plt

n = 6   # so gene trong 1 nst
m = 10  # so nst trong 1 quan the
n_geneation = 10   # so vong doi
fitnesses_map = []    # de ve bieu do

# tao gia tri cho moi gene
def create_gene_value(bound = 20):
    return (random.random()*2 - 1)*bound

# tao gen ngau nhien
def create_random_gen():
    return [create_gene_value() for _ in range(n)]

# tao quan the ban dau
def create_population():
    return [create_random_gen() for _ in range(m)]

# ham tinh lose
def calculate_lose(individual):
    print(individual)
    return sum(gen**2 for gen in individual)

# tao mang do thich nghi
def calcultae_fitness(individual):
    return 1 / (1 + calculate_lose(individual))

# tao mang chua do thich nghi
def create_fitnesses(population):
    return [calcultae_fitness(i) for i in population]

# dot bien
def mutute(individual, mutute_rate = 0.05):
    if random.random() < mutute_rate:
        i = random.randint(0, n - 1)
        individual[i] = create_gene_value()
    return individual

# lai ghep
def crossoer(individual1, individual2, crossoer_rate = 0.9):
    individual_c1 = individual1.copy()
    individual_c2 = individual2.copy()

    if random.random() < crossoer_rate:
        for i in range(random.randint(1, n - 1)):
            individual_c1[i] = individual2[i]
            individual_c2[i] = individual1[i]
    return individual_c1, individual_c2

# chon loc banh xe
def selection(fitnesses):
    s = sum(fitnesses)
    ran = random.randint(0, int(s))
    s1 = 0
    index = 0
    for i in range(m):
        s1 += fitnesses[i]
        if s1 >= ran:
            index = i
    return index

# tao quan the moi
def create_new_population(population, fitnesses):
    sorted_old_population = sorted(population, key = calcultae_fitness)
    sorted_fitnesses = sorted(fitnesses)
    fitnesses_map.append(calculate_lose(sorted_old_population[m - 1]))
    new_population = []
    for _ in range(int(m / 2)):
        # lua chon
        individual1 = sorted_old_population[selection(sorted_fitnesses)]
        individual2 = sorted_old_population[selection(sorted_fitnesses)]

        # lai gep
        individual_c1, individual_c2 = crossoer(individual1, individual2)

        # dot bien
        individual_m1 = mutute(individual_c1)
        individual_m2 = mutute(individual_c2)

        # cho vao quan the moi
        new_population.append(individual_m1)
        new_population.append(individual_m2)
    return new_population
    
# main
population = create_population()
fitnesses = create_fitnesses(population)
for i in range(n_geneation):
    population = create_new_population(population, fitnesses)
    fitnesses = create_fitnesses(population)

sorted_population = sorted(population, key = calcultae_fitness)
print('best: ', sorted_population[m - 1])
plt.plot(fitnesses_map)
plt.show()