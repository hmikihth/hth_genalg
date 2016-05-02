#!/usr/bin/env python3

import unittest
from hth_genalg import Population, Creature

class PopulationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Testing Population")
        self.population = Population.Population()
    
    @classmethod
    def tearDownClass(self):
        print("Population testing is complete")
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_1_SetLimit(self):
        limit = 3
        self.population.setLimit(limit)
        self.assertEqual(self.population.limit, limit)
        self.population.setLimit("asd")
        self.assertIs(type(self.population.limit), int)
  
    def test_2_AddCreature(self):
        creature = Creature.Creature()
        self.population.addCreature(creature)
        self.assertIs(self.population.creatures[0], creature)
        self.population.addCreature(1)
        self.assertEqual(len(self.population.creatures), 1)
    
    def test_3_DeleteCreature(self):
        creature = self.population.creatures[0]
        self.population.deleteCreature(creature)
        self.assertEqual(len(self.population.creatures), 0)
    
    def test_4_GenerationCounterShift(self):
        self.population.generationCounterShift()
        self.assertEqual(self.population.generation_counter, 1)  

    def test_5_Sorting(self):
        fitness_list = [3,1,7,5]
        for e in fitness_list:
            creature = Creature.Creature()
            creature.setFitness(e)
            self.population.addCreature(creature)
        greater_is_better = False
        self.population.setSortingGreaterIsBetter(greater_is_better)
        self.population.sorting()
        self.assertTrue(
            all(
                self.population.creatures[i].fitness <= self.population.creatures[i+1].fitness for i in range(len(self.population.creatures)-1)
            )
        )
        greater_is_better = True
        self.population.setSortingGreaterIsBetter(greater_is_better)
        self.population.sorting()
        self.assertTrue(
            all(
                self.population.creatures[i].fitness >= self.population.creatures[i+1].fitness for i in range(len(self.population.creatures)-1)
            )
        )

    def test_6_Clear(self):
        self.population.clear()
        self.assertEqual(len(self.population.creatures), 0)
