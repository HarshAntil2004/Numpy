"""The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

"""

#COPY:
#Make a copy, change the original array, and display both arrays:
import numpy as np
arr = np.array([1,2,3,4,5])
arr2 = arr.copy()
arr2[0] = 6
print(arr)
print(arr2) #The copy SHOULD NOT be affected by the changes made to the original array.
print('\n')

#VIEW:
#Make a view, change the original array, and display both arrays:
arr = np.array([1,2,3,4])
arr2 = arr.view()
arr2[0] = 7
print(arr)
print(arr2) #The view SHOULD be affected by the changes made to the original array.
print('\n')

#Make Changes in the VIEW:
#Make a view, change the view, and display both arrays:
arr = np.array([1,2,3,4])
arr2 = arr.view()
arr2[0] = 0
print(arr)
print(arr2) #The original array SHOULD be affected by the changes made to the view.
print('\n')

"""Check if Array Owns its Data
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object."""

arr = np.array([1,2,3,4])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
print('\n')