#!/usr/bn/env python3

import unittest
import Crossover
import Creature
                                          
class CrossoverTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Testing Crossover")
    
    @classmethod
    def tearDownClass(self):
        print("Crossover testing is complete")

    def setUp(self):
        self.crossover = Crossover.Crossover()

    def tearDown(self):
        del self.crossover

    def test_01_SetEqualCrossover(self):
        value = -1
        self.crossover.setEqualCrossover(value)
        self.assertEqual(type(self.crossover.equal_crossover), bool)

    def test_02_SetMutantChromosomesIsPositive(self):
        value = -1
        self.crossover.setMutantChromosomes(value)
        self.assertGreaterEqual(self.crossover.mutant_chromosomes, 1)

    def test_03_SetMutantChromosomesIsInt(self):
        value = "string"
        self.crossover.setMutantChromosomes(value)
        self.assertEqual(type(self.crossover.mutant_chromosomes), int)

    def test_04_SetInbreeding(self):
        value = 1
        self.crossover.setInbreeding(value)
        self.assertEqual(type(self.crossover.inbreeding), bool)

    def test_05_SetParents(self):
        mother = Creature.Creature()
        father = Creature.Creature()
        self.crossover.setParents(mother, father)
        self.assertIs(self.crossover.mother, mother)
        self.assertIs(self.crossover.father, father)
        self.crossover.setParents(mother, mother)
        self.assertNotEqual(self.crossover.mother, self.crossover.father)

    def test_06_TypeSetParents(self):
        mother = Creature.Creature()
        father = Creature.Creature()
        self.crossover.setParents(mother, father)
        self.assertIs(type(self.crossover.mother), Creature.Creature)
        self.assertIs(type(self.crossover.father), Creature.Creature)

    def test_07_CheckInbreeding(self):
        mother = Creature.Creature()
        father = Creature.Creature()
        mother.setChromosomes("1234")
        father.setChromosomes("5678")
        self.crossover.setParents(mother, father)
        self.assertIs(type(self.crossover.checkInbreeding()), bool)
        self.assertFalse(self.crossover.checkInbreeding())
        father.setChromosomes("1234")
        self.crossover.setParents(mother, father)
        self.assertTrue(self.crossover.checkInbreeding())

    def test_08_GenerateWithEqualCrossover(self):
        mother = Creature.Creature()
        father = Creature.Creature()

        mother.setChromosomes("1234")
        father.setChromosomes("5678")
        self.crossover.setParents(mother, father)
        child = self.crossover.generateWithEqualCrossover()
        self.assertIs(type(child), Creature.Creature)

        mother_chromosomes = [1,2,3,4]
        father_chromosomes = [5,6,7,8]
        mother.setChromosomes(mother_chromosomes)
        father.setChromosomes(father_chromosomes)
        self.crossover.setParents(mother, father)
        child = self.crossover.generateWithEqualCrossover()
        self.assertIs(type(child.chromosomes), type(mother.chromosomes))
        self.assertIs(type(child.chromosomes), type(father.chromosomes))
        self.assertEqual(len(child.chromosomes), len(mother.chromosomes))    
        self.assertEqual(len(child.chromosomes), len(mother.chromosomes))

        i = 0
        for e in child.chromosomes:
            if e in mother_chromosomes:
                i += 1
        self.assertEqual(i, len(mother_chromosomes) / 2.0)
        self.assertEqual(i, len(father_chromosomes) / 2.0)

    def test_09_GenerateWithRandomCrossover(self):
        mother = Creature.Creature()
        father = Creature.Creature()

        mother.setChromosomes("1234")
        father.setChromosomes("5678")
        self.crossover.setParents(mother, father)
        child = self.crossover.generateWithRandomCrossover()
        self.assertIs(type(child), Creature.Creature)

        mother_chromosomes = [1,2,3,4]
        father_chromosomes = [5,6,7,8]
        mother.setChromosomes(mother_chromosomes)
        father.setChromosomes(father_chromosomes)
        self.crossover.setParents(mother, father)
        child = self.crossover.generateWithRandomCrossover()
        self.assertIs(type(child.chromosomes), type(mother.chromosomes))
        self.assertIs(type(child.chromosomes), type(father.chromosomes))
        self.assertEqual(len(child.chromosomes), len(mother.chromosomes))    
        self.assertEqual(len(child.chromosomes), len(mother.chromosomes))

    def test_10_Generate(self):
        mother = Creature.Creature()
        father = Creature.Creature()
        mother_chromosomes = [1,2,3,4]
        father_chromosomes = [5,6,7,8]
        mother.setChromosomes(mother_chromosomes)
        father.setChromosomes(father_chromosomes)
        self.crossover.setParents(mother, father)
        child = self.crossover.generate()
        self.assertIs(type(child), Creature.Creature)
    
        self.crossover.setEqualCrossover(True)
        n = 0
        while n < 10:
          child = self.crossover.generate()
          i = 0
          for e in child.chromosomes:
                  if e in mother_chromosomes:
                      i += 1
          self.assertEqual(len(mother_chromosomes) / 2.0, i)
          n += 1
    
        differents = 0
        n = 0
        while n < 10:
            self.crossover.setEqualCrossover(False)
            child = self.crossover.generate()
            i = 0
            for e in child.chromosomes:
                if e in mother_chromosomes:
                    i += 1
            if i != len(mother_chromosomes) / 2.0:
                differents += 1
            n += 1
        self.assertNotEqual(differents, 0)
