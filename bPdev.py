#!/usr/bin/env python3

def isFunction(input):
    """
     Return with true if the input is a function.
    """
    def temp():
        pass
    return type(input) is type(temp)
