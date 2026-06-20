"""Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - int8 (signed byte integer)
? - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )"""

"""Checking the Data Type of an Array
The NumPy array object has a property called dtype that returns the data type of the array:"""
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
print('\n')

#Get the data type of an array containing strings:
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
print('\n')

"""Creating Arrays With a Defined Data Type
We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:

"""
#Create an array with data type string:
arr = np.array([1,2,3,4,5],dtype="S")
print(arr)
print(arr.dtype)
print('\n')

#For i, u, f, S and U we can define size as well.
#Create an array with data type 4 bytes integer:
arr = np.array([1,2,3,4,5],dtype='i4')
print(arr)
print(arr.dtype)
print('\n')

"""What if a Value Can Not Be Converted?
If a type is given in which elements can't be casted then NumPy will raise a ValueError.

ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

Example
A non integer string like 'a' can not be converted to integer (will raise an error):

import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')"""

"""Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer."""
arr = np.array([1.1,2.1,3.1])
arr2 = arr.astype('i')
print(arr2)
print(arr2.dtype)
print('\n')

#Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])
arr2 = arr.astype(int)
print(arr2)
print(arr2.dtype)
print('\n')

#Change data type from integer to boolean:
arr = np.array([1, 0, 3])
arr2 = arr.astype(bool)
print(arr2)
print(arr2.dtype)
print('\n')

