#!/usr/bin/env python3

import unittest
from hth_genalg import Mutation, Creature

class MutationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print ("Testing Mutation")
    
    @classmethod
    def tearDownClass(self):
        print ("Mutation testing is complete")
    
    def setUp(self):
        self.mutation = Mutation.Mutation()
    
    def tearDown(self):
        del self.mutation

    def testSetMutantChromosomes(self):
        mutant_chromosomes = 2
        self.mutation.setMutantChromosomes(mutant_chromosomes)
        self.assertEqual(mutant_chromosomes, self.mutation.mutant_chromosomes)
        mutant_chromosomes = 'b'
        self.mutation.setMutantChromosomes(mutant_chromosomes)
        self.assertIs(int, type(self.mutation.mutant_chromosomes))    

    def testSetCreature(self):
        creature = Creature.Creature()
        self.mutation.setCreature(creature)
        self.assertIs(self.mutation.creature, creature)
        self.mutation.setCreature("abc")
        self.assertIs(type(self.mutation.creature), Creature.Creature)
    
    def testSetValueset(self):
        valueset = ["a","b"]
        self.mutation.setValueset(valueset)
        self.assertEqual(self.mutation.valueset, valueset)
        valueset = 1
        self.mutation.setValueset(valueset)
        self.assertEqual(type(self.mutation.valueset), list)

    def testMutate(self):
        mutant_chromosomes = 1
        self.mutation.setMutantChromosomes(mutant_chromosomes)
        chromosomes = "abba"
        creature = Creature.Creature()
        creature.setChromosomes(chromosomes)
        self.mutation.setCreature(creature)
        valueset = ["c","d","e"]
        self.mutation.setValueset(valueset)
        self.mutation.mutate()
        self.assertNotEqual(self.mutation.creature.chromosomes, chromosomes)
        self.assertEqual(type(self.mutation.creature.chromosomes), type(chromosomes))

        mutant_chromosomes = 3
        self.mutation.setMutantChromosomes(mutant_chromosomes)
        chromosomes = "aaaaa"
        creature = Creature.Creature()
        creature.setChromosomes(chromosomes)
        self.mutation.setCreature(creature)
        valueset = ["b"]
        self.mutation.setValueset(valueset)
        self.mutation.mutate()
        self.assertEqual(self.mutation.creature.chromosomes.count(valueset[0]), mutant_chromosomes)
    