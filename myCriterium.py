#!/usr/bin/env python3

"""
   It is an example file. Please implement your own. thx :)
"""

def criterium(creature):
    s = "BBAAABBAAA"
    fitness = 0
    i = 0
    for c in creature.chromosomes:
        if c != s[i]:
            fitness += 1
        i += 1
    return fitness

def get():
    return criterium
