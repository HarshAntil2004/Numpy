"""Random Permutations of Elements
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation().

Shuffling Arrays
Shuffle means changing arrangement of elements in-place. i.e. in the array itself."""
"""ExampleGet your own Python Server
Randomly shuffle elements of following array:"""
from numpy import random as rd
import numpy as np
x = np.array([1,2,3,4,5])
rd.shuffle(x)
print(x)
print('\n')
#The shuffle() method makes changes to the original array.

"""Generating Permutation of Arrays
Example
Generate a random permutation of elements of following array:"""
arr = np.array([1, 2, 3, 4, 5])
print(rd.permutation(arr)) 
print('\n')
#The permutation() method returns a re-arranged array (and leaves the original array un-changed).
