"""Visualize Distributions With Seaborn
Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
Displots
Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array."""
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0,1,2,3,4,5])
plt.show()

#Plotting a Displot Without the Histogram
sns.displot([0,1,2,3,4,5],kind='kde')
plt.show()
#Note: We will be using: sns.displot(arr, kind="kde") to visualize random distributions in this tutorial.
