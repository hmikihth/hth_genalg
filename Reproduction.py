#!/usr/bin/env python3

import random

import Population
import Crossover
import Creature

class Reproduction():
    def __init__(self):
        self.children = []
    
    def setCrossover(self, crossover):
        if type(crossover) is Crossover.Crossover:
            self.crossover = crossover
    
    def setPopulation(self, population):
        if type(population) is Population.Population:
            self.population = population
    
    def setSurvivors(self, survivors):
        if type(survivors) is list:
            self.children = survivors
    
    def setElitRate(self, elit_rate):
        if type(elit_rate) is int:
            self.elit_rate = elit_rate
    
    def setNumberOfElitChildren(self, n):
        if (type(n) is int) and (n >= 2):
            self.number_of_elit_children = n

    def setNumberOfNormalChildren(self, n):
        if (type(n) is int) and (n >= 1):
           self.number_of_normal_children = n

    def makeChild(self, mother):
        if type(mother) is Creature.Creature:
            father = random.choice(self.population.creatures)
            self.crossover.setParents(mother, father)
            child = self.crossover.generate()
            self.children.append(child)
  
    def running(self):
        children_counter = len(self.children)
        pos = 0
        for mother in self.population.creatures:
            if pos < self.elit_rate:
                i = 0
                while i < self.number_of_elit_children:
                    self.makeChild(mother)
                    children_counter += 1
                    if children_counter == self.population.limit:
                        break
                    i += 1
            else: 
                i = 0
                while i < self.number_of_normal_children:
                    self.makeChild(mother)
                    children_counter += 1
                    if children_counter == self.population.limit:
                        break
                    i += 1 
                    if children_counter == self.population.limit:
                        break
                pos += 1
            self.population.clear()
        for child in self.children:
            self.population.addCreature(child)
        self.population.generationCounterShift()
