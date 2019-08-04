import random
import matplotlib.pyplot as plt

n = 4   # so luong gen trong nst
m = 100 # so luong nst trong quan the
n_generations = 200 # so vong doi
losses = [] # de ve bieu do loss

# lay du lieu tu file advertising.csv trong thu muc FileDemo
def load_data():
    file = open('FileDemo/advertising.csv', 'r')
    lines = file.readlines()
    features = []   # luu cac thong so
    prices = []     # luu cac ung voi moi thong so gia tri sale
    for i in range(1, 201):
        strings = lines[i].split(',')
        feature = [float(s.strip()) for s in strings[:(len(strings) - 1)]]
        feature.append(1.0)
        features.append(feature)
        price = float(strings[-1])
        prices.append(price)
    file.close()
    return features, prices

# lay du lieu
features, prices = load_data()

# tao gia tri nst ngau nhien
def create_random_value(bound = 100):
    return random.random()*bound

# tinh loss
def compute_loss(individual):
    estimated_prices = []
    for feature in features:
        estimated_price = sum(c*x for x, c in zip(feature, individual))
        estimated_prices.append(estimated_price)
    losses = [abs(y_est - y_gt) for y_est, y_gt in zip(estimated_prices, prices)]
    return sum(losses)

# tinh fitness
def compute_fitness(individual):
    fitness = 1 / (compute_loss(individual) + 1)
    return fitness

# tao mang fitnesses
def create_fitnesses(population):
    return [compute_fitness(individual) for individual in population]

# tao ca the
def create_individual():
    return [create_random_value() for _ in range(n)]

# # chon loc
# def selection(population, fitnesses):
#     s = sum(fitnesses)
#     ran = random.random()*s
#     s1 = 0
#     individual = population[0]
#     for i in range(len(fitnesses)):
#         s1 += fitnesses[i]
#         if s1 >= ran:
#             individual = population[i]
#             break
#     return individual

# # lai ghep
# def crossoer(individual1, individual2, crossoer_rate = 0.9):
#     individual_c1 = individual1.copy()
#     individual_c2 = individual2.copy()
#     if random.random() < crossoer_rate:
#         index = random.randint(1, n-2)
#         for i in range(index):
#             individual_c1[i] = individual2[i]
#             individual_c2[i] = individual1[i]
#     return individual_c1, individual_c2

# # dot bien
# def mutate(individual, mutation_rate = 0.1):
#     individual_n = individual.copy()
#     for _ in range(n):
#         if random.random() < mutation_rate:
#             index = random.randint(0, n-1)
#             individual_n[index] = create_random_value()
#     return individual_n

# # tao quan the moi
# def create_new_population(old_population, fitnesses):
#     sorted_old_population = sorted(old_population, key = compute_fitness)
#     losses.append(compute_loss(sorted_old_population[-1]))
#     print('bess: ', losses[-1])
#     new_population = []
#     for _ in range(int(m/2) - 2):
#         # chon loc
#         individual1 = selection(old_population, fitnesses)        
#         individual2 = selection(old_population, fitnesses)        

#         # lai ghep
#         individual_c1, individual_c2 = crossoer(individual1, individual2)

#         # dot bien
#         individual_n1 = mutate(individual_c1)
#         individual_n2 = mutate(individual_c2)

#         # cho vao quan the moi
#         new_population.append(individual_n1)
#         new_population.append(individual_n2)
#     new_population.append(sorted_old_population[-1])
#     new_population.append(sorted_old_population[-2])
#     return new_population

# thuc hien
# population = [create_individual() for _ in range(m)]
# fitnesses = create_fitnesses(population)
# for _ in range(n_generations):
#     population = create_new_population(population, fitnesses)
#     fitnesses = create_fitnesses(population)
    
#     sorted_population = sorted(population, key = compute_fitness)
#     individual = sorted_population[-1]
#     estimated_prices = []
#     for feature in features:
#         estimated_price = sum(c*x for x, c in zip(feature, individual))
#         estimated_prices.append(estimated_price)

# plt.plot(losses)
# plt.xlabel('generation')
# plt.ylabel('loss')
# plt.show()

def generate_random_value(bound = 100):
    return random.random()*bound

def crossoer(individual1, individual2, crossoer_rate = 0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()

    for i in range(n):
        if random.random() < crossoer_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]
    return individual1_new, individual2_new

def mutate(individual, mutate_rate = 0.05):
    individual_m = individual.copy()
    for i in range(n):
        if random.random() < mutate_rate:
            individual_m[i] = generate_random_value()
    return individual_m

def selection(sorted_old_population):
    index1 = random.randint(0, m - 1)
    while True:
        index2 = random.randint(0, m - 1)
        if index2 != index1:
            break
    individual_s = sorted_old_population[index1]
    if index2 > index1:
        individual_s = sorted_old_population[index2]
    return individual_s

def create_new_population(old_population, elitism = 2, gen = 1):
    sorted_population = sorted(old_population, key = compute_fitness)
    if gen%1 == 0:
        losses.append(compute_loss(sorted_population[-1]))
        print('loss best: ', compute_loss(sorted_population[-1]))
    new_population = []
    while len(new_population) < m - elitism:
        # selection
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)

        # crossoer
        individual_c1, individual_c2 = crossoer(individual_s1, individual_s2)

        # mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2)
    for ind in sorted_population[m - elitism:]:
        new_population.append(ind.copy())
    return new_population

population = [create_individual() for _ in range(m)]
for i in range(n_generations):
    population = create_new_population(population, 2, i)
    sorted_population = sorted(population, key = compute_fitness)
    individual = sorted_population[-1]
    estimated_prices = []
    for feature in features:
        estimated_price = sum(c*x for x, c in zip(feature, individual))
        estimated_prices.append(estimated_price)

fig, ax = plt.subplots(figsize = (10, 6))
plt.plot(prices, c = 'red')
plt.plot(estimated_prices, c = 'blue')
plt.show()