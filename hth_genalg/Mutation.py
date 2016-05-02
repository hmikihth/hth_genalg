#!/usr/bin/env python3

from hth_genalg import Creature
import random

class Mutation():
    def __init__(self):
        pass
  
    def __del__(self):
        pass

    def setMutantChromosomes(self, mutant_chromosomes):
        if type(mutant_chromosomes) is int:
            self.mutant_chromosomes = mutant_chromosomes

    def setCreature(self, creature):
        if type(creature) is Creature.Creature:
            self.creature = creature

    def setValueset(self, valueset):
        if type(valueset) is list:
            self.valueset = valueset
    
    def mutate(self):
        chromosomes_n = len(self.creature.chromosomes)
        chromosomes = list(self.creature.chromosomes)
        mutated_positions = []
        i = 0
        while i < self.mutant_chromosomes:
            while True:
                pos = random.randint(0, chromosomes_n - 1)
                if pos not in mutated_positions:
                    mutated_positions.append(pos)
                    break
            chromosomes[pos] = random.choice(self.valueset)
            i += 1
        if type(self.creature.chromosomes) is str:
            chromosomes = str(chromosomes)
        self.creature.setChromosomes(chromosomes)
