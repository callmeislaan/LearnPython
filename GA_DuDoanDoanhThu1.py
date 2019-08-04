# du doan gia nha dua vao giai thuat di truyen
import random
import matplotlib.pyplot as plt

n = 2   # so luong nst
m = 100 # so luong 
n_generation = 100 # so doi
fitnesses_map = []   # de ve do thi

# lay du lieu tu FileDemo/data_house_price.csv
def get_data():
    areas = []  # dien tich
    prices = [] # gia nha 
    data = open('FileDemo/data_house_price.csv', 'r')
    lines = data.readlines()
    for i in range(len(lines)):
        areas.append(float(lines[i].split(',')[0]))
        prices.append(float(lines[i].split(',')[1]))
    data.close()
    return areas, prices

areas, prices = get_data()

plt.plot(areas, prices, 'ro')
# ve bieu do de xac dinh loai
# plt.plot(areas, prices, 'ro')
# plt.xlabel('dien tich')
# plt.ylabel('gia')
# plt.show()

# sau khi thay bieu do ta xac dinh giong mot duong thang -> gia co the tinh bang: price = ax + b
# ta tim a, b gan voi gia thuc nhat

# tao gia tri cho nst
def create_gen_value(bound = 100):
    return random.random()*bound

# tao nhien sac the
def create_individual():
    return [create_gen_value() for _ in range(n)]

# tao ham lose
def calculate_lose(individual):
    a = individual[0]
    b = individual[1]
    estimated_prices = [a*x + b for x in areas]
    estimated_prices = [abs(x) for x in estimated_prices]
    loses = [abs(y_gt - y_est) for y_gt, y_est in zip(prices, estimated_prices)]
    return sum(loses)

# tao ham fitness
def calculate_fitness(individual):
    lose = calculate_lose(individual)
    fitness = 1 / (1 + lose)
    return fitness

# tao ham tinh fitnesses
def create_fitnesses(population):
    return [calculate_fitness(individual) for individual in population]

# chon loc: chon loc theo phuong phap quay banh xe so
def selection(population, fitnesses):
    s = sum(fitnesses)
    ran = random.random()*s
    s1 = 0
    individual = population[0]
    for i in range(m):
        s1 += fitnesses[i]
        if s1 >= ran:
            individual = population[i]
            break
    return individual

# lai ghep
def crossoer(individual1, individual2, crossoer_rate = 0.9):
    individual_c1 = individual1.copy()
    individual_c2 = individual2.copy()
    i = 1
    if random.random() < crossoer_rate:
        individual_c1[i] = individual2[i]
        individual_c2[i] = individual1[i]
    return individual_c1, individual_c2

# dot bien
def mutute(individual, mutute_rate = 0.05):
    individual_copy = individual.copy()
    for i in range(n):
        if random.random() < mutute_rate:
            individual_copy[i] = create_gen_value()    
    # ran = random.random()
    # if ran < mutute_rate:
    #     index = random.randint(0, 1)
    #     individual_copy[index] = create_gen_value()
    return individual_copy

# tao quan the moi
def create_new_population(old_population, fitnesses):
    new_population = []
    sorted_old_population = sorted(old_population, key = calculate_fitness)
    fitnesses_map.append(calculate_lose(sorted_old_population[m-1]))
    print('best: ', calculate_lose(sorted_old_population[m-1]))
    for _ in range(int(m / 2)):
        # chon loc
        individual1 = selection(old_population, fitnesses)
        individual2 = selection(old_population, fitnesses)

        # lai ghep
        individual_c1, individual_c2 = crossoer(individual1, individual2)

        # dot bien
        individual_m1 = mutute(individual_c1)
        individual_m2 = mutute(individual_c2)

        # cho vao quan the moi
        new_population.append(individual_m1)
        new_population.append(individual_m2)
    return new_population

population = [create_individual() for _ in range(m)]
fitnesses = create_fitnesses(population)
for _ in range(n_generation):
    population = create_new_population(population, fitnesses)
    fitnesses = create_fitnesses(population)

# plt.plot(fitnesses_map)
# plt.xlabel('generation')
# plt.ylabel('loses')
# plt.show()

best = sorted(population, key = calculate_fitness)[-1]
a = best[0]
b = best[1]
gra = [a*x + b for x in areas]
plt.plot(areas, gra)
plt.show()
