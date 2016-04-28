#!/usr/bin/env python3

import unittest
import Population, Termination, Creature
from inspect import isfunction

def func(population):
    for e in population.creatures:
        if e.fitness == 0:
            return True
    return False

class TerminationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.termination = Termination.Termination()
        print("Testing Termination")
    
    @classmethod
    def tearDownClass(self):
        print("Termination testing is complete")
    
    def test_01_SetPopulation(self):
        self.population = Population.Population()
        self.termination.setPopulation(self.population)
        self.termination.setPopulation("x")
        self.assertIs(type(self.termination.population), Population.Population)
    
    def test_02_SetTerminationFunction(self):
        self.termination.setTerminationFunction(func)
        self.termination.setTerminationFunction("x")
        self.assertTrue(isfunction(self.termination.func))
    
    def test_03_Check(self):
        creature = Creature.Creature()
        creature.setFitness(0)
        self.population = Population.Population()
        self.population.addCreature(creature)
        self.termination.setPopulation(self.population)
        self.assertTrue(self.termination.check())
