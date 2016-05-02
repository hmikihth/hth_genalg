#!/usr/bin/env python3

from hth_genalg import Creature

class Population():
    def __init__(self):
        self.limit = 0
        self.creatures = []
        self.generation_counter = 0
    
    def __del__(self):
        pass
    
    def setLimit(self, limit):
        if type(limit) is int:
            self.limit = limit
    
    def addCreature(self, creature):
        if type(creature) is Creature.Creature:
            if len(self.creatures) <= self.limit:
                self.creatures.append(creature)
    
    def deleteCreature(self, creature):
        if type(creature) is Creature.Creature:
            self.creatures.remove(creature)

    def generationCounterShift(self):
        self.generation_counter += 1

    def setSortingGreaterIsBetter(self, status):
        if type(status) is bool:
            self.sorting_greater_is_better = status

    def sorting(self):
        self.creatures.sort(key=lambda e: e.fitness, reverse=self.sorting_greater_is_better)
  
    def clear(self):
        del self.creatures[:]
