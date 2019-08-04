import random
import matplotlib.pyplot as plt

n = 14  # so luong gen trong nst
m = 100 # so luong nst trong quan the
n_generations = 1000 # so luong doi xet

losses = [] # luu cac gia tri loss tot nhat

# lay du lieu ra
def load_data():
    file = open('FileDemo/Boston_Dataset.csv', 'r')
    lines = file.readlines()
    features = []   # luu tru cac gia tri
    prices = []   # luu tru gia nha thuc
    for i in range(1, len(lines)):
        strings = lines[i].split(',')
        feature = [float(s.strip()) for s in strings[1:(len(strings) - 1)]]
        feature.append(1.0)
        features.append(feature)
        price = float(strings[-1].strip())
        prices.append(price)
    file.close()
    return features, prices

features, prices = load_data()

# tao gia tri gen ngau nhien
def generate_random_value(bound = 100):
    return random.random()*bound

# tao nhiem sac the
def create_individual():
    return [generate_random_value() for _ in range(n)]

# tinh loss
def compute_loss(individual):
    estimated_prices = []
    for feature in features:
        estimated_price = sum(c*x for c, x in zip(individual, feature))
        estimated_prices.append(estimated_price)
    losses = [abs(y_gt - y_est) for y_gt, y_est in zip(prices, estimated_prices)]
    return sum(losses)

# tinh fitness
def compute_fitness(individual):
    fitness = 1 / (1 + compute_loss(individual))
    return fitness

# chon loc: boc hai cai, cai nao ngon hon thi lay
def selection(sorted_population):
    index1 = random.randint(0, m-1)
    while True:
        index2 = random.randint(0, m-1)
        if index1 != index2:
            break
    individual = sorted_population[index1]
    if index1 < index2:
        individual = sorted_population[index2]
    return individual

# lai ghep
def crossoer(individual1, individual2, crossoer_rate = 0.9):
    individual_c1 = individual1.copy()
    individual_c2 = individual2.copy()
    if random.random() < crossoer_rate:
        index = random.randint(1, n-2)
        for i in range(index):
            individual_c1[i] = individual2[i]
            individual_c2[i] = individual1[i]
    return individual_c1, individual_c2

# dot bien
def mutate(individual, mutation_rate = 0.1):
    individual_new = individual.copy()
    if random.random() < mutation_rate:
        index = random.randint(0, n-1)
        individual_new[index] = generate_random_value()
    return individual_new

# tao quan the moi
def create_new_population(old_population, i):
    sorted_population = sorted(old_population, key = compute_fitness)
    # lay gia tri loss tot nhat
    losses.append(compute_loss(sorted_population[-1]))
    print('lan: ', i, ' best: ', losses[-1])
    new_population = []
    while len(new_population) < m:
        # lua chon
        individual1 = selection(sorted_population)
        individual2 = selection(sorted_population)

        # lai ghep
        individual_c1, individual_c2 = crossoer(individual1, individual2)

        # dot bien
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        # cho vao quan the moi
        new_population.append(individual_m1)
        new_population.append(individual_m2)
    return new_population

# chay
population = [create_individual() for _ in range(m)]
for i in range(n_generations):
    population = create_new_population(population, i)
    s_p = sorted(population, key = compute_fitness)
    estimated_prices = []
    for feature in features:
        estimated_price = sum(c*x for c, x in zip(s_p[-1], feature))
        estimated_prices.append(estimated_price)

fig, ax = plt.subplots(figsize = (10, 6))
plt.plot(prices, c = 'red')
plt.plot(estimated_prices, c = 'green')
plt.show()