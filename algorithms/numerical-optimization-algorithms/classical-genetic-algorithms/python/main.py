Sure, here's a basic implementation of a classic genetic algorithm (GA) in Python without using any third-party libraries beyond the standard library:

python

import random

# Define parameters
POPULATION_SIZE = 10
CHROMOSOME_LENGTH = 8
MUTATION_RATE = 0.1
NUM_GENERATIONS = 100

# Define objective function (fitness function)
def fitness(chromosome):
    return sum(chromosome)

# Generate initial population
def generate_population():
    return [[random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)] for _ in range(POPULATION_SIZE)]

# Crossover operator (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation operator (bit flip mutation)
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Main GA loop
population = generate_population()
for generation in range(NUM_GENERATIONS):
    # Evaluate fitness of each individual in the population
    fitness_scores = [fitness(chromosome) for chromosome in population]
    
    # Select parents for crossover (roulette wheel selection)
    total_fitness = sum(fitness_scores)
    parent1 = random.choices(population, weights=fitness_scores, k=1)[0]
    parent2 = random.choices(population, weights=fitness_scores, k=1)[0]
    
    # Perform crossover to produce offspring
    child1, child2 = crossover(parent1, parent2)
    
    # Perform mutation on offspring
    child1 = mutate(child1)
    child2 = mutate(child2)
    
    # Replace two worst individuals with offspring
    population.remove(max(population, key=fitness))
    population.remove(max(population, key=fitness))
    population.extend([child1, child2])

# Print final population
print("Final population:")
for individual in population:
    print(individual, "Fitness:", fitness(individual))

In this implementation:

    The objective function (fitness()) evaluates the fitness of a chromosome. In this example, the fitness is calculated as the sum of the elements of the chromosome.
    The initial population is generated randomly using the generate_population() function.
    The crossover operator (crossover()) performs single-point crossover between two parent chromosomes.
    The mutation operator (mutate()) flips each bit in a chromosome with a certain probability.
    In each generation, the population is evaluated for fitness, parents are selected using roulette wheel selection, crossover and mutation are applied to produce offspring, and the two worst individuals in the population are replaced by the offspring.
    After a fixed number of generations, the final population and their fitness scores are printed.

This implementation provides a basic example of a classic genetic algorithm in Python without relying on any third-party libraries beyond the standard library.