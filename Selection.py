#!/usr/bin/env python3

import Population

"""
   Strategies:
   - Stochastic (Every creature can produce children)
   - Deterministic (Just the elits can produce children)
   
   - Bests alive strategy (need to set a limit for the bests)
   
   - It have to support the multi-population strategy
   - possibility to copy the elits to an other population 
   
   - Elit rate
   
"""

class Selection():
    def __init__(self):
        self.sorted = False
  
    def setElitRate(self, elit_rate):
        if type(elit_rate) is int:
            if elit_rate > 0:
                self.elit_rate = elit_rate
  
    def setPopulation(self, population):
        if type(population) is Population.Population:
            self.population = population
    
    def setDeterministic(self, status):
        if type(status) is bool:
            self.deterministic_strategy = status
    
    def setBestsAlive(self, status):
        if type(status) is bool:
           self.bests_alive_strategy = status
    
    def setBestsAliveLimit(self, limit):
        if type(limit) is int:
           self.bests_alive_limit = limit
        
    def sorting(self):
        self.population.sorting()
        self.sorted = True
    
    def getBests(self, n):
        if self.sorted:
            return self.population.creatures[:n]

    def deleteWorsts(self, n):
        if self.sorted:
            del self.population.creatures[-n:]
    
    def setMigrants(self, migrants):
        if type(migrants) is list:
            for e in migrants:
                self.population.addCreature(e)

    def runBestsAliveStrategy(self):
        if self.sorted and self.bests_alive_strategy:
            self.survivors = self.population.creatures[:self.bests_alive_limit]

    def runDeterministicStrategy(self):
        if self.sorted and self.deterministic_strategy:
            del self.population.creatures[self.elit_rate:]

    def runSelection(self):
        self.survivors = []
        self.runBestsAliveStrategy()
        self.runDeterministicStrategy()
        self.sorted = False
        return self.survivors
