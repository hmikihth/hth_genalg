#!/usr/bin/env python3

import random
import Creature
import Population

import Evaluation
import Termination
import Selection
import Reproduction
import Crossover
import Mutation

class Initialization():
    def __init__(self, settings):
        self.settings = settings

    def chromGen(self):
        chromosomes = []
        i = 0
        while i < self.settings.chromosomes_n:
            c = random.choice(self.settings.valueset)
            chromosomes.append(c)
            i += 1
        return chromosomes      

    def makePopulation(self, population_index):
        population = Population.Population()
        population.setLimit(self.settings.populations[population_index].population_limit)
        population.setSortingGreaterIsBetter(self.settings.populations[population_index].sorting_greater)
        i = 0
        while i < self.settings.populations[population_index].population_limit:
            creature = Creature.Creature()
            creature.setChromosomes(self.chromGen())
            population.addCreature(creature)
            i += 1
        return population

    def createPopulations(self):
        self.populations = []
        i = 0
        while i < self.settings.populations_n:
            self.populations.append(self.makePopulation(i))
            i += 1
        return self.populations
    
    def createEvaluations(self):
        self.evaluations = []
        i = 0
        while i < self.settings.populations_n:
            evaluation = Evaluation.Evaluation()
            evaluation.setCriteriumFunction(self.settings.populations[i].criterium_function)
            self.evaluations.append(evaluation)
            i += 1
        return self.evaluations

    def createTermination(self):
        self.termination = Termination.Termination()
        self.termination.setTerminationFunction(self.settings.termination_function)
        return self.termination
    
    def createSelections(self):
        self.selections = []
        i = 0
        while i < self.settings.populations_n:
            selection = Selection.Selection()
            selection.setElitRate(self.settings.populations[i].elit_rate)
            selection.setDeterministic(self.settings.populations[i].deterministic)
            selection.setBestsAlive(self.settings.populations[i].bests_alive)
            selection.setBestsAliveLimit(self.settings.populations[i].bests_alive_limit)
            selection.setPopulation(self.populations[i])
            self.selections.append(selection)
            i += 1
        return self.selections

    def createCrossovers(self):
        self.crossovers = []
        i = 0
        while i < self.settings.populations_n:
            crossover = Crossover.Crossover()
            crossover.setEqualCrossover(self.settings.populations[i].equal_crossover)      
            crossover.setMutantChromosomes(self.settings.populations[i].mutant_chromosomes) #
            crossover.setInbreeding(self.settings.populations[i].inbreeding)
            self.crossovers.append(crossover)
            i += 1
    
    def createReproductions(self):
        self.createCrossovers()
        self.reproductions = []
        i = 0
        while i < self.settings.populations_n:
            reproduction = Reproduction.Reproduction()
            reproduction.setCrossover(self.crossovers[i])
            reproduction.setPopulation(self.populations[i])
            reproduction.setElitRate(self.settings.populations[i].elit_rate)
            reproduction.setNumberOfElitChildren(self.settings.populations[i].elit_children)
            reproduction.setNumberOfNormalChildren(self.settings.populations[i].normal_children)
            self.reproductions.append(reproduction)
            i += 1
        return self.reproductions
    
    def createMutations(self):
        self.mutations = []
        i = 0
        while i < self.settings.populations_n:
            mutation = Mutation.Mutation()
            mutation.setMutantChromosomes(self.settings.populations[i].mutant_chromosomes) #
            mutation.setValueset(self.settings.valueset)
            self.mutations.append(mutation)
            i += 1
        return self.mutations
   