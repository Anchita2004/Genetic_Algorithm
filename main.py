# Import necessary modules
from functools import partial
import knapsack
import genetic
from timer import timer

# Example items and weight limit
things = knapsack.second_example
weight_limit = 3000

# Display the weight limit
print("Weight Limit: %dkg" % weight_limit)

# Running the Genetic Algorithm
print("\nGENETIC ALGORITHM")
print("-----------------")

# Timer for performance measurement
with timer():
    population, generations = genetic.run_evolution(
        populate_func=partial(genetic.generate_population, size=10, genome_length=len(things)),
        fitness_func=partial(knapsack.fitness, things=things, weight_limit=weight_limit),
        fitness_limit=1000,  # Optional: Set high so evolution runs full course
        generation_limit=100
    )

# Get the best items from the best genome
best_items = knapsack.from_genome(population[0], things)

# Display the results
knapsack.print_stats(best_items)
print(f"\nGenerations run: {generations}")
