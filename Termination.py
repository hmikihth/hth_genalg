#!/usr/bin/env python3

import bPdev
import Population

class Termination():
    def __init__(self): 
        pass
  
    def setPopulation(self, population):
        if type(population) is Population.Population:
            self.population = population
  
    def setTerminationFunction(self, func):
        if bPdev.isFunction(func):
            self.func = func
  
    def check(self):
        return self.func(self.population) 
