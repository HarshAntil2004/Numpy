"""Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

A boolean index list is a list of booleans corresponding to indexes in the array.

If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array."""
"""ExampleGet your own Python Server
Create an array from the elements on index 0 and 2:"""
import numpy as np
arr = np.array([41,42,43,44])
x = [True,False,True,False]
newarr = arr[x]
print(newarr) #The example above will return [41, 43], why? Because the new array contains only the values where the filter array had the value True, in this case, index 0 and 2.
print('\n')

"""Creating the Filter Array
In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions."""
#Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
x = [] # Create an empty list
for i in arr : # go through each element in arr
        if i > 42 : # if the element is higher than 42, set the value to True, otherwise False:
                x.append(True)
        else : x.append(False)
newarr = arr[x]
print(x)
print(newarr)
print('\n')

#Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_array = []
for i in arr :
        if i % 2 == 0 :
                filter_array.append(True)
        else : filter_array.append(False)
newarr = arr[filter_array]
print(filter_array)
print(newarr)
print('\n')

"""Creating Filter Directly From Array
The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to."""
"""Example
Create a filter array that will return only values higher than 42:"""
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print('\n')

#Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print('\n')