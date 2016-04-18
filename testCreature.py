#!/usr/bin/env python3

import unittest
import Creature

class CreatureTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Testing Creature")

    @classmethod
    def tearDownClass(self):
        print("Creature testing is complete")

    def setUp(self):
        self.creature = Creature.Creature()

    def tearDown(self):
        del self.creature

    def testDefaultFitness(self):
        self.assertIsNone(self.creature.fitness)

    def testDefaultChromosomes(self):
        self.assertIsNone(self.creature.chromosomes)

    def testSetGenes(self):
        chromosomes = "chromosomes"
        self.creature.setChromosomes(chromosomes)
        self.assertEqual(self.creature.chromosomes, chromosomes)

    def testSetFitness(self):
        fitness = 1
        self.creature.setFitness(fitness)
        self.assertEqual(self.creature.fitness, fitness)

    def testFitnessIsInt(self):
        fitness = "it is not an int"
        try:
            self.creature.setFitness(fitness)
        except:
            pass
        self.assertNotEqual(self.creature.fitness, fitness)

    def testFitnessIsNotNegative(self):
        fitness = -2
        try:
            self.creature.setFitness(fitness)
        except:
            pass
        self.assertNotEqual(self.creature.fitness, fitness)

