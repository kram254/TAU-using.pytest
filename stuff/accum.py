"""
 This module contains a basic accumulator class.
 Shows how to use pytest to test classes...
"""

# class Accumulator

class Accumulator:
    def __init__(self) -> None:
        self._count = 0

#@property controls how developers can get and set values
    @property
    def count(self):
        return self._count

    def add (self, more=1):
        self._count += more