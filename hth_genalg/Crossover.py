#!/usr/bin/env python3

import random

from hth_genalg import Mutation
from hth_genalg import Creature

class Crossover():
    def __init__(self, equal_crossover=True, mutant_chromosomes=1, inbreeding=True):
        self.setEqualCrossover(equal_crossover)
        self.setMutantChromosomes(mutant_chromosomes)
        self.setInbreeding(inbreeding)
    
    def __del__(self):
        pass

    def setEqualCrossover(self, equal_crossover):
        if type(equal_crossover) is bool:
            self.equal_crossover = equal_crossover
    
    def setMutantChromosomes(self, mutant_chromosomes):
        if type(mutant_chromosomes) is int:
            if mutant_chromosomes >= 1:
                self.mutant_chromosomes = mutant_chromosomes

    def setInbreeding(self, inbreeding):
        if type(inbreeding) is bool: 
            self.inbreeding = inbreeding

    def setParents(self, mother, father):
        if mother != father:  
            if type(mother) is Creature.Creature:
                self.mother = mother
            if type(father) is Creature.Creature:
                self.father = father

    def checkInbreeding(self):
        return self.mother.chromosomes == self.father.chromosomes 
 
    def generateWithEqualCrossover(self):
        """
        1st step: Create a new creature
        2nd step: Half of the chromosomes from the mother and half from the father. The position of the chromosomes may 
                  random but the cardinal number of these have to be equal.
        3rd step: Set the chromosomes of the new creature
        4th step: Call the checkinbreeding method and if it return with true call the Mutation.mutate
        5th step: Return with the new creature
        """
        creature = Creature.Creature()
        chromosomes = []
        chromosomes_from_mother = 0
        chromosomes_from_father = 0
        maxlen = len(self.mother.chromosomes)
        half = maxlen / 2
        i = 0
        while i < maxlen:
            if chromosomes_from_mother < half and chromosomes_from_father < half:
                if bool(random.getrandbits(1)):
                    chromosomes.append(self.mother.chromosomes[i])
                    chromosomes_from_mother += 1
                else:
                    chromosomes.append(self.father.chromosomes[i])
                    chromosomes_from_father += 1
            elif chromosomes_from_mother < half:
                chromosomes.append(self.mother.chromosomes[i])
                chromosomes_from_mother += 1
            else:
                chromosomes.append(self.father.chromosomes[i])
                chromosomes_from_father += 1
            i += 1
        if type(self.mother.chromosomes) is str:
            chromosomes = str(chromosomes)
        creature.setChromosomes(chromosomes)
        return creature
    
    def generateWithRandomCrossover(self):
        """
        1st step: Create a new creature
        2nd step: The chromosomes from the father and mother are by different (random) rate
        3rd step: Set the chromosomes of the new creature
        4th step: Call the checkinbreeding method and if it return with 
        true call the Mutation.mutate
        5th step: Return with the new creature
        """
        creature = Creature.Creature()
        chromosomes = []
        maxlen = len(self.mother.chromosomes)
        i = 0
        while i < maxlen:
            if bool(random.getrandbits(1)):
                chromosomes.append(self.mother.chromosomes[i])
            else:
                chromosomes.append(self.father.chromosomes[i])
            i += 1
        if type(self.mother.chromosomes) is str:
            chromosomes = str(chromosomes)
        creature.setChromosomes(chromosomes)
        return creature

    def generate(self):
        """
         Call the generateWithEqualCrossover method if self.equal_crossover is true.
         Otherwise call the generateWithRandomCrossover method.
        """
        if self.equal_crossover: 
            return self.generateWithEqualCrossover()
        else: 
            return self.generateWithRandomCrossover()
  
