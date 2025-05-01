import random

def generate_genome(length):
    return [random.randint(0, 1) for _ in range(length)]

def generate_population(size, genome_length):
    return [generate_genome(genome_length) for _ in range(size)]

def selection_pair(population, fitness_func):
    weights = [fitness_func(g) for g in population]
    return random.choices(population, weights=weights, k=2)

def single_point_crossover(a, b):
    if len(a) < 2:
        return a[:], b[:]
    p = random.randint(1, len(a) - 1)
    return a[:p] + b[p:], b[:p] + a[p:]

def mutation(genome, num=1, prob=0.5):
    for _ in range(num):
        index = random.randrange(len(genome))
        if random.random() < prob:
            genome[index] = 1 - genome[index]
    return genome

def run_evolution(populate_func, fitness_func, fitness_limit, generation_limit=100):
    population = populate_func()
    for generation in range(generation_limit):
        population = sorted(population, key=fitness_func, reverse=True)

        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[:2]
        for _ in range((len(population) // 2) - 1):
            parents = selection_pair(population, fitness_func)
            offspring_a, offspring_b = single_point_crossover(*parents)
            next_generation += [mutation(offspring_a), mutation(offspring_b)]

        population = next_generation

    population = sorted(population, key=fitness_func, reverse=True)
    return population, generation
