#!/usr/bin/env python3

import unittest
import Crossover, Population, Reproduction, Creature

class ReproductionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Reproduction testing")
        self.reproduction = Reproduction.Reproduction()
    
    @classmethod
    def tearDownClass(self):
        print("Reproduction test is complete")
    
    def test_01_SetCrossover(self):
        crossover = Crossover.Crossover()
        self.reproduction.setCrossover(crossover)
        self.reproduction.setCrossover("x")
        self.assertIs(type(self.reproduction.crossover), Crossover.Crossover)

    def test_02_SetPopulation(self):
        population = Population.Population()
        self.reproduction.setPopulation(population)
        self.reproduction.setPopulation("x")
        self.assertIs(type(self.reproduction.population), Population.Population)
    
    def test_03_SetSurvivors(self):
        survivors = []
        self.reproduction.setSurvivors(survivors)
        self.reproduction.setPopulation("x")
        self.assertIs(type(self.reproduction.children), list)
    
    def test_04_SetElitRate(self):
        elit_rate = 3
        self.reproduction.setElitRate(elit_rate)
        self.reproduction.setElitRate("x")
        self.assertIs(type(self.reproduction.elit_rate), int)
        self.assertEqual(self.reproduction.elit_rate, elit_rate)
        
    def test_05_SetNumberOfElitChildren(self):
        n = 3
        self.reproduction.setNumberOfElitChildren(n)
        self.reproduction.setNumberOfElitChildren(0)
        self.reproduction.setNumberOfElitChildren("x")
        self.assertIs(type(self.reproduction.number_of_elit_children), int)    
        self.assertEqual(self.reproduction.number_of_elit_children, n)
    
    def test_06_SetNumberOfNormalChildren(self):
        n = 2
        self.reproduction.setNumberOfNormalChildren(n)
        self.reproduction.setNumberOfNormalChildren(0)
        self.reproduction.setNumberOfNormalChildren("x")
        self.assertIs(type(self.reproduction.number_of_normal_children), int)    
        self.assertEqual(self.reproduction.number_of_normal_children, n)
    
    def test_07_MakeChild(self):
        population = Population.Population()
        crossover = Crossover.Crossover()
        reproduction = Reproduction.Reproduction()

        population.setLimit(2)
        for c in ["AAAAAA", "BBBBBB"]:
            creature = Creature.Creature()
            creature.setChromosomes(c)
            population.addCreature(creature)
    
        mother = Creature.Creature()
        mother.setChromosomes("CCCCCC")
    
        reproduction.setPopulation(population)
        reproduction.setCrossover(crossover)
        reproduction.setSurvivors([])
        reproduction.makeChild(mother)
        self.assertEqual(len(reproduction.children), 1)
    
    @unittest.skip("Random error...")
    def test_08_Running(self):
        elit_rate = 1
        population_size = 6
        population = Population.Population()
        population.setLimit(population_size)
        crossover = Crossover.Crossover()
        reproduction = Reproduction.Reproduction()
        for c in ["AAAA", "BBBB", "CCCC", "DDDD", "EEEE", "FFFF"]:
            creature = Creature.Creature()
            creature.setChromosomes(c)
            creature.setFitness(1)
            population.addCreature(creature)
        reproduction.setCrossover(crossover)
        reproduction.setSurvivors([])
        reproduction.setElitRate(elit_rate)
        reproduction.setNumberOfElitChildren(3)
        reproduction.setNumberOfNormalChildren(2)
        reproduction.setPopulation(population)
        reproduction.running()
        self.assertEqual(len(reproduction.children), population_size)
   
