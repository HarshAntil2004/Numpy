"""Multinomial Distribution
Multinomial distribution is a generalization of binomial distribution.

It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

It has three parameters:

n - number of times to run the experiment.

pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).

size - The shape of the returned array.

ExampleGet your own Python Server
Draw out a sample for dice roll:"""
from numpy import random as rd
import seaborn as sns
import matplotlib.pyplot as plt
x = rd.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
sns.displot(x,kind='kde')
print(x)
plt.show()
print('\n')

"""Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval.

Note: As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as that of multiple binomial distributions."""
