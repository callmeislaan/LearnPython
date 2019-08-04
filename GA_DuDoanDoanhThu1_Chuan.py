import random
import matplotlib.pyplot as plt

n = 2
m = 100
n_generations = 100

losses = []

# ham load data
def load_data():
    file = open('FileDemo/data_house_price.csv')
    lines = file.readlines()
    areas = []
    prices = []
    for i in range(len(lines)):
        string = lines[i].split(',')
        areas.append(float(string[0]))
        prices.append(float(string[1]))
    file.close()
    return areas, prices

# load data
areas, prices = load_data()

plt.plot(areas, prices, 'ro')
def generate_random_value(bound = 100):
    return (random.random())*bound

def compute_loss(individual):
    a = individual[0]
    b = individual[1]

    estimated_prices = [a*x + b for x in areas]
    estimated_prices = [abs(x) for x in estimated_prices]

    losses = [abs(y_est - y_gt) for y_est, y_gt in zip(estimated_prices, prices)]
    return sum(losses)

def compute_finess(individual):
    loss = compute_loss(individual)
    fitness = 1 / (1 + loss)
    return fitness

def create_individual():
    return [generate_random_value() for _ in range(n)]

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
    sorted_population = sorted(old_population, key = compute_finess)
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

individual_best =population[-1]
a = individual_best[0]
b = individual_best[1]
gra = [a*x + b for x in areas]
plt.plot(areas, gra)
plt.show()