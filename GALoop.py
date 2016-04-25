#!/usr/bin/env python3

import Initialization

class GALoop():
    def __init__(self, settings):
        self.settings = settings
        ini = Initialization.Initialization(self.settings)
        self.populations = ini.createPopulations()
        self.evaluations = ini.createEvaluations()
        self.termination = ini.createTermination()
        self.selections = ini.createSelections()
#        self.crossovers = ini.createCrossovers()
        self.reproductions = ini.createReproductions()
        self.mutations = ini.createMutations()
  
    def runEvaluations(self):
        index = 0
        for evaluation in self.evaluations:
            for creature in self.populations[index].creatures:
                evaluation.setCreature(creature)
                evaluation.executeCriteriumFunction()
            self.selections[index].sorting()
            index += 1
  
    def runTermination(self):
        result = False
        for population in self.populations:
            self.termination.setPopulation(population)
            result = self.termination.check()
            if result:
                break
        return result
  
    def runSelections(self):
        self.survivors = []
        for selection in self.selections:
            self.survivors += selection.runSelection()
      
    def setSurvivors(self):
        index = 0
        for reproduction in self.reproductions:
            if self.settings.populations[index].bests_alive:
                size = len(self.survivors)
                self.reproductions[index].setSurvivors(self.survivors)
            index += 1

    def runReproductions(self):
        for reproduction in self.reproductions:
            reproduction.running()
    
    def runMutations(self):
        index = 0
        for mutation in self.mutations:
            for creature in self.populations[index].creatures:
                mutation.setCreature(creature)
                mutation.mutate()
            index += 1

    def loop(self):
        while True:
            self.runEvaluations()
            if self.runTermination():
                break
            self.runSelections()
            self.setSurvivors()
            self.runReproductions()
            self.runMutations()
        return False
