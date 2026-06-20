"""Poisson Distribution
Poisson Distribution is a Discrete Distribution.

It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

It has two parameters:

lam - rate or known number of occurrences e.g. 2 for above problem.

size - The shape of the returned array.

ExampleGet your own Python Server
Generate a random 1x10 distribution for occurrence 2:"""
from numpy import random as rd
x = rd.poisson(lam=2,size=10)
print(x)
print('\n')

"""Visualization of Poisson Distribution"""
import seaborn as sns
import matplotlib.pyplot as plt
sns.displot(rd.poisson(lam=2,size=1000))
plt.show()
print('\n')

"""Difference Between Normal and Poisson Distribution
Normal distribution is continuous whereas poisson is discrete.

But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean."""
data = {
        "normal" : rd.normal(loc=50,scale=7,size=1000),
        "poisson" : rd.poisson(lam=50,size=1000)
}
sns.displot(data,kind='kde')
plt.show()

"""Difference Between Binomial and Poisson Distribution
Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.

But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam."""
data = {
        "binomial" : rd.binomial(n=1000,p=0.01,size=1000),
        "poisson" : rd.poisson(lam=10,size=1000)
}
sns.displot(data,kind='kde')
plt.show()