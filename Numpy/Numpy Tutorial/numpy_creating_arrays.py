"""Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.

"""
import numpy as np
arr = np.array([1,2,3,4,5])
arr2 = np.array((1,2,3,4,5)) #To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
print(arr)
print(type(arr))
print('\n')

"""Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements."""

"""0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

"""
arr = np.array(32)
print(arr)
print('\n')

"""1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays."""
arr = np.array([1,2,3,4,5])
print(arr)
print('\n')

"""2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.

NumPy has a whole sub module dedicated towards matrix operations called numpy.mat"""
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print('\n')

"""3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor."""
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)
print('\n')

"""Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have."""
a = np.array(32)
b = np.array([1,2,3,4,5,6])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print('\n')


"""Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument."""
arr = np.array([1,2,3,4], ndmin=5) #there are two ndmin and ndim , so be careful while using them
print(arr)
print(arr.ndim)
print('\n')