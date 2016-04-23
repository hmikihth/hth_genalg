#!/usr/bin/env python3

import Creature
import bPdev

class Evaluation():
    def __init__(self):
        pass
    
    def __del__(self):
        pass
  
    def setCreature(self, creature):
        if type(creature) is Creature.Creature:
            self.creature = creature
  
    def setCriteriumFunction(self, criterium_function):
        if bPdev.isFunction(criterium_function):
            self.criterium_function = criterium_function
    
    def setFitness(self, fitness):
        self.creature.setFitness(fitness)

    def executeCriteriumFunction(self):
        fitness = self.criterium_function(self.creature)
        self.setFitness(fitness)
    