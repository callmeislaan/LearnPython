# phát biểu bài toán: Cho một véc tơ gồm n phần tử gồm 2 số
# là 0 và 1, vector sắp xếp thế nào để giá trị vector là lớn nhất
# lời giải: vd n = 5 thì lớn nhất là: [1 1 1 1 1]

# giai bang giai thuat di truyen:
import random

n = 6   # kich thuoc nhiem sac the
m = 10  # kich thuoc cua quan the

n_generation = 40   # so doi can chay
fitnesses = []  # de ve bieu do qua trinh toi uu

# khoi tao quan the ban dau
def generate_random_value():
    return random.randint(0, 1)

def create_individual():
    return [generate_random_value() for _ in range(n)]

# tinh fitness
def compute_fitness(individual):
    return sum(individual)

# ham lai ghep voi ti le lai ghep la 90%
def crossoer(individual1, individual2, crossover_rate = 0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()

    for i in range(n):
        if random.random() < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]
    return individual1_new, individual2_new

# ham dot bien voi ti le dot bien la 5%
def mutate(individual, mutation_rate = 0.05):
    individual_m = individual.copy()
    for i in range(n):
        if random.random() < mutation_rate:
            individual_m[i] = generate_random_value()
    return individual_m

# ham lua chon
def selection(sorted_old_population):
    index1 = random.randint(0, m-1)
    while True:
        index2 = random.randint(0, m-1)
        if index2 != index1:
            break
    
    individual_s = sorted_old_population[index1]
    if index2 > index1:
        individual_s = sorted_old_population[index2]
    return individual_s

def create_new_population(old_population, elitism = 2, gen = 1):
    sorted_population = sorted(old_population, key=compute_fitness)
    if gen%1 == 0:
        fitnesses.append(compute_fitness(sorted_population[m-1]))
        print('best: ', compute_fitness(sorted_population[m-1]))
    new_population = []
    while len(new_population) < m-elitism:
        # chon loc
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)

        # lai ghep
        individual_c1, individual_c2 = crossoer(individual_s1, individual_s2)

        # dot bien
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2)
    for ind in sorted_population[m-elitism:]:
        new_population.append(ind.copy())
    return new_population

population = [create_individual() for _ in range(m)]
for i in range(n_generation):
    population = create_new_population(population, 2, i)
