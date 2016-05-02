#!/usr/bin/env python3

import unittest
from hth_genalg import Evaluation
from hth_genalg import Creature
from inspect import isfunction

def func(creature):
    return creature.chromosomes.count('a')

class EvaluationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Testing Evaluation")
        self.evaluation = Evaluation.Evaluation()

    @classmethod
    def tearDownClass(self):
        print("Evaluation test is complete")
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testSetCriteriumFunction(self):
        self.evaluation.setCriteriumFunction(func)
        self.assertIs(self.evaluation.criterium_function, func)    
        self.evaluation.setCriteriumFunction(1)
        self.assertTrue(isfunction(self.evaluation.criterium_function))
    
    def testSetCreature(self):
        creature = Creature.Creature()
        self.evaluation.setCreature(creature)
        self.assertIs(type(self.evaluation.creature), Creature.Creature)  
        self.assertIs(self.evaluation.creature, creature)    

    def testSetFitness(self):
        self.evaluation.setFitness(123)
        self.assertEqual(self.evaluation.creature.fitness, 123)
    
    def testExecuteCriteriumFunction(self):
        creature = Creature.Creature()
        chromosomes = "abba"
        creature.setChromosomes(chromosomes)
        self.evaluation.setCreature(creature)
        self.evaluation.setCriteriumFunction(func)
        self.evaluation.executeCriteriumFunction()
        self.assertEqual(self.evaluation.creature.fitness, chromosomes.count("a"))

      