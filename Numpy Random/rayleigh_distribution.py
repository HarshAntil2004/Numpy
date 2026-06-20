"""Rayleigh Distribution
Rayleigh distribution is used in signal processing.

It has two parameters:

scale - (standard deviation) decides how flat the distribution will be default 1.0).

size - The shape of the returned array.

ExampleGet your own Python Server
Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:"""
from numpy import random as rd
x = rd.rayleigh(scale=2,size=(2,3))
print(x)
print('\n')

#Visualization of Rayleigh Distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(rd.rayleigh(size=1000), kind="kde")
plt.show()

"""Similarity Between Rayleigh and Chi Square Distribution
At unit stddev and 2 degrees of freedom rayleigh and chi square represent the same distributions."""
