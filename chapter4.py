# NumPy is awesome!

import numpy as np

# generate some random data
data = np.random.randn(2, 3)
print(data * 30)

# create a range of numbers w/ numpy. This is exponentially more efficient than built-in python list(range(100000))
my_arr = np.arange(100000)

my_list = list(range(100000))

%time for _ in range(10): my_arr2 = my_arr * 2

%time for _ in range(10): my_list2 = my_list * 2


data.shape # shows the shape of the data
data.dtype # shows the datatype of the numpy array
data.ndim #shows the n number of dimensions

np.zeros(100) # produces an array of 100 zeros
np.ones(123) # produces an array of 123 1s

x = np.array([1, 2, 3, 4, 5])

# numpy is all about vectorization
print(x*5)  


# .reshape reshapes the data
arr = np.arange(15).reshape((3, 5))

arr = arr.reshape(5, 3)

arr = arr.reshape(1, 15)

# .T transposes
arr.T 

# Using transpose with dot product
arr = np.random.randn(6, 3)
np.dot(arr.dot(arr.T, arr))

# unary ufunctions
np.square(arr)
np.log(arr)

# vectorization

arr = np.random.randn(4, 4)
arr > 0
np.where(arr > 0, 1, 0)

# Statistical methods

arr.mean()
np.mean(arr)
arr.sum()
