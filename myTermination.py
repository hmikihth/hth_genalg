#!/usr/bin/env python3

def termination(population):
    for creature in population.creatures:
        if creature.fitness == 0:
            print(creature.chromosomes, creature.fitness, population.generation_counter)
            return True
    return False

def get():
    return termination
