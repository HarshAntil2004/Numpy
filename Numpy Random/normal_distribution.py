"""Normal Distribution
The Normal Distribution is one of the most important distributions.

It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.

It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.

ExampleGet your own Python Server
Generate a random normal distribution of size 2x3:"""
import numpy as np
from numpy import random as rd
x = rd.normal(size=(2,3))
print(x)
print('\n')

"""Example
Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:"""
x = rd.normal(size=(2,3),loc=1,scale=2)
print(x)
print('\n')

#Visualization of Normal Distribution
import matplotlib.pyplot as plt
import seaborn as sns
x = rd.normal(size=(2,3),loc=1,scale=2)
sns.displot(x,kind='kde')
plt.show()

#Note: The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.
sns.displot(rd.normal(size=1000),kind='kde')
plt.show()