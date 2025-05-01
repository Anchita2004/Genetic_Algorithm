import random
from collections import namedtuple

Thing = namedtuple('Thing', ['name', 'value', 'weight'])

second_example = [
    Thing("laptop", 500, 2200),
    Thing("headphones", 150, 160),
    Thing("coffee mug", 60, 350),
    Thing("notepad", 40, 333),
    Thing("water bottle", 30, 192),
]

def from_genome(genome, things):
    return [things[i] for i, bit in enumerate(genome) if bit == 1]

def fitness(genome, things, weight_limit):
    weight = 0
    value = 0
    for i, bit in enumerate(genome):
        if bit == 1:
            weight += things[i].weight
            value += things[i].value
            if weight > weight_limit:
                return 0
    return value

def print_stats(things):
    value = sum(t.value for t in things)
    weight = sum(t.weight for t in things)
    for t in things:
        print(f"- {t.name}: {t.value}p, {t.weight}g")
    print(f"Total value: {value}")
    print(f"Total weight: {weight}g")
