#!/usr/bin/env python3

import unittest

import Initialization

import Population
import Creature

def cr_func(x):
    return 1

def t_func(x):
    return True

class PopulationSettings1():
    def __init__(self):
        self.population_limit = 8
        self.sorting_greater = True
        self.criterium_function = cr_func
        self.elit_rate = 2
        self.deterministic = False
        self.bests_alive = False
        self.bests_alive_limit = 1
        self.equal_crossover = False
        self.mutant_chromosomes = 1
        self.inbreeding = True
        self.elit_children = 3
        self.normal_children = 2

class SettingsTest():
    def __init__(self):
        self.valueset = ['A','B','C','D','E','F']
        self.chromosomes_n = 10
        self.populations = [PopulationSettings1()]
        self.populations_n = 1
        self.termination_function = t_func

class InitializationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Testing Initialization")
        self.settings = SettingsTest()
        self.initialization = Initialization.Initialization(self.settings)
    
    @classmethod
    def tearDownClass(self):
        print("Initialization testing is complete")
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_01_chromGen(self):
        chromosomes = self.initialization.chromGen()
        self.assertEqual(len(chromosomes), self.settings.chromosomes_n)
    
    def test_02_makePopulation(self):
        population = self.initialization.makePopulation(0)
        self.assertIs(type(population), Population.Population)
        self.assertEqual(len(population.creatures), self.settings.populations[0].population_limit)
        for creature in population.creatures:
            with self.subTest(creature=creature):
                self.assertIs(type(creature), Creature.Creature)
    
    def test_03_createPopulations(self):
        self.initialization.createPopulations()
        self.assertEqual(len(self.initialization.populations), self.settings.populations_n)
    
    def test_04_createEvaluations(self):
        self.initialization.createEvaluations()
        self.assertEqual(len(self.initialization.evaluations), self.settings.populations_n)
    
    def test_05_createTermination(self):
        self.initialization.createTermination()
    
    def test_06_createSelections(self):
        self.initialization.createSelections()
        self.assertEqual(len(self.initialization.selections), self.settings.populations_n)
    
    def test_07_createCrossovers(self):
        self.initialization.createCrossovers()
        self.assertEqual(len(self.initialization.crossovers), self.settings.populations_n)
    
    def test_08_createReproductions(self):
        self.initialization.createReproductions()
        self.assertEqual(len(self.initialization.reproductions), self.settings.populations_n)
    
    def test_09_createMutations(self):
        self.initialization.createMutations()
        self.assertEqual(len(self.initialization.mutations), self.settings.populations_n)

