"""Uniform Distribution
Used to describe probability where every event has equal chances of occuring.

E.g. Generation of random numbers.

It has three parameters:

low - lower bound - default 0.0

high - upper bound - default 1.0

size - The shape of the returned array

ExampleGet your own Python Server
Create a 2x3 uniform distribution sample:"""
from numpy import random as rd
x = rd.uniform(size=(2,3))
print(x)
print('\n')

#Visualization of Uniform Distribution
import seaborn as sns
import matplotlib.pyplot as plt
x = rd.uniform(size=(1000))
sns.displot(x,kind='kde')
plt.show()
print('\n')
