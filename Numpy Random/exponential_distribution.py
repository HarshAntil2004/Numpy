"""Exponential Distribution
Exponential distribution is used for describing time till next event e.g. failure/success etc.

It has two parameters:

scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

size - The shape of the returned array.

ExampleGet your own Python Server
Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:"""
from numpy import random as rd
x = rd.exponential(scale=2,size=(2,3))
print(x)
print('\n')

#Visualization of Exponential Distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(rd.exponential(size=1000), kind="kde")
plt.show()

"""Relation Between Poisson and Exponential Distribution
Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events."""
