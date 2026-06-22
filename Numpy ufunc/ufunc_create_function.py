"""How To Create Your Own ufunc
To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
ExampleGet your own Python Server
Create your own ufunc for addition:"""
import numpy as np
def myadd (x,y) :
        return x + y
myadd = np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[5,6,7,8]))
print('\n')


"""Check if a Function is a ufunc
Check the type of a function to check if it is a ufunc or not.

A ufunc should return <class 'numpy.ufunc'>.

Example
Check if a function is a ufunc:"""
print(type(np.add))
print(type(np.concatenate))
print('\n')

"""To test if the function is a ufunc in an if statement, use the numpy.ufunc value (or np.ufunc if you use np as an alias for numpy):

Example
Use an if statement to check if the function is a ufunc or not:"""
if type(np.add) == np.ufunc :
        print("This is a ufunc function")
else :
        print("error")

