#!/usr/bin/env python3

import unittest
import Selection
import Population
import Creature

class SelectionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print ("Testing selection")
        self.selection = Selection.Selection()
  
    @classmethod
    def tearDownClass(self):
        print ("Selection testing is complete")
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_01_SetElitRate(self):
        elit_rate = 2
        self.selection.setElitRate(elit_rate)
        self.assertEqual(self.selection.elit_rate, elit_rate)
        self.selection.setElitRate(0)
        self.assertGreater(self.selection.elit_rate, 0)
        self.selection.setElitRate('x')
        self.assertEqual(type(self.selection.elit_rate), int)    

    def test_02_SetPopulation(self):
        population = Population.Population()
        self.selection.setPopulation(population)
        self.assertIs(self.selection.population, population)
        self.selection.setPopulation(1)
        self.assertIs(type(self.selection.population), Population.Population)

    def test_03_SetDeterministic(self):
        status = True
        self.selection.setDeterministic(status)
        self.assertIs(self.selection.deterministic_strategy, status)
        status = False
        self.selection.setDeterministic(status)
        self.assertIs(self.selection.deterministic_strategy, status)
        self.selection.setDeterministic("x")
        self.assertIs(type(self.selection.deterministic_strategy), bool)

    def test_04_SetBestsAlive(self):
        status = True
        self.selection.setBestsAlive(status)
        self.assertIs(self.selection.bests_alive_strategy, status)
        status = False
        self.selection.setBestsAlive(status)
        self.assertIs(self.selection.bests_alive_strategy, status)
        self.selection.setBestsAlive("x")
        self.assertIs(type(self.selection.bests_alive_strategy), bool)

    def test_05_SetBestsAliveLimit(self):
        self.selection.setBestsAliveLimit(2)
        self.assertIs(type(self.selection.bests_alive_limit), int)
        self.selection.setBestsAlive("x")
        self.assertIs(type(self.selection.bests_alive_limit), int)

    def test_06_GetBests(self):
        self.selection.population.setLimit(5)
        self.selection.population.setSortingGreaterIsBetter(False)
        self.selection.setBestsAliveLimit(2)
        for e in [0,1,2,3,4]:
            creature = Creature.Creature()
            creature.setFitness(e)
            self.selection.population.addCreature(creature)
        self.selection.sorting()
        self.assertEqual(len(self.selection.getBests(2)), 2)

    def test_07_SetMigrants(self):
        self.selection.population.setLimit(6)
        creature = Creature.Creature()
        creature.setFitness(5)
        self.selection.setMigrants([creature])
        self.assertEqual(len(self.selection.population.creatures), 6)

    def test_08_DeleteWorsts(self):
        self.selection.deleteWorsts(1)
        self.assertEqual(len(self.selection.population.creatures), 5)
    
    def test_09_RunBestsAliveStrategy(self):
        self.selection.setBestsAlive(False)
        self.selection.setBestsAliveLimit(4)
        self.selection.runBestsAliveStrategy()
        try:
            survivors_length = len(self.selection.survivors) 
        except:
            pass
        if "survivors_length" in locals():
            self.assertEqual(survivors_length, 0)
        self.selection.setBestsAlive(True)
        self.selection.runBestsAliveStrategy()
        self.assertEqual(len(self.selection.survivors), 4)
    
    def test_10_RunDeterministicStrategy(self):
        elit_rate = 3
        self.selection.setElitRate(elit_rate)
        self.selection.setDeterministic(False)
        self.selection.runDeterministicStrategy()
        self.assertEqual(len(self.selection.population.creatures), 5)
        self.selection.setDeterministic(True)
        self.selection.runDeterministicStrategy()
        self.assertEqual(len(self.selection.population.creatures), elit_rate)
    
    def test_11_RunSelection(self):
        elit_rate = 2
        self.selection.setElitRate(elit_rate)
        self.selection.setDeterministic(True)
        self.selection.setBestsAliveLimit(1)
        self.selection.setBestsAlive(True)
        self.selection.runSelection()
        self.assertEqual(len(self.selection.population.creatures), elit_rate)
        self.assertEqual(len(self.selection.survivors), 1)
        self.assertFalse(self.selection.sorted)
    