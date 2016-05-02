#!/usr/bin/env python3

from inspect import isfunction
from hth_genalg import Population

class Termination():
    def __init__(self): 
        pass
  
    def setPopulation(self, population):
        if type(population) is Population.Population:
            self.population = population
  
    def setTerminationFunction(self, func):
        if isfunction(func):
            self.func = func
  
    def check(self):
        return self.func(self.population) 
