"""Chi Square Distribution
Chi Square distribution is used as a basis to verify the hypothesis.

It has two parameters:

df - (degree of freedom).

size - The shape of the returned array.

ExampleGet your own Python Server
Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:"""
from numpy import random as rd
x = rd.chisquare(df=2,size=(2,3))
print(x)
print('\n')

#Visualization of Chi Square Distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(rd.chisquare(df=1, size=1000), kind="kde")
plt.show()

