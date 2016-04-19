#!/usr/bin/env python3

class Creature():
    def __init__(self, chromosomes=None):
        self.fitness = None
        self.chromosomes = chromosomes

    def __del__(self):
        pass

    def setChromosomes(self, chromosomes):
        self.chromosomes = chromosomes
  
    def setFitness(self, fitness):
        if type(fitness) == int and fitness >= 0:
            self.fitness = fitness  
