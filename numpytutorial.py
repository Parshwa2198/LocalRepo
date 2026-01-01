# Import NumPy library and give it a short name 'np'
# NumPy is used for fast numerical computations
import numpy as np

# Import time module to measure execution time
import time

# (These two imports are NOT used in this code)
# Tools.demo.sortvisu.steps -> unused
# fontTools.misc.psOperators.ps_array -> unused
from Tools.demo.sortvisu import steps
from fontTools.misc.psOperators import ps_array


# Create a very large number (10,000,000)
size = 1_000_0000

# Create a Python list containing numbers from 0 to size-1
py_list = list(range(size))


# --------- Python list square calculation ---------

# Start time measurement
start = time.time()

# Square each element in the Python list using list comprehension
sq_list = [x**2 for x in py_list]

# End time measurement
end = time.time()

# Print time taken by Python list operation
print(f"Python list time = {end - start} seconds")


# --------- NumPy array square calculation ---------

# Convert Python list into NumPy array
np_arr = np.array(py_list)

# Start time measurement
start = time.time()

# Square all elements of NumPy array at once (vectorized operation)
ps_array = np_arr**2

# End time measurement
end = time.time()

# Print time taken by NumPy operation
print(f"Numpy array time = {end - start} seconds")

# NumPy can square the entire array at once using **2 (much faster)

end = time.time()


# --------- Memory usage comparison ---------

# Import sys module to check memory size
import sys

# Total memory used by Python list (approximation)
print(f"Python list size = {sys.getsizeof(py_list) * len(py_list)} bytes")

# Memory used by the list object itself (not elements)
print(f"Python list size = {sys.getsizeof(py_list)} bytes")


# --------- Creating NumPy arrays ---------

# Create a NumPy array from a Python list
arr = np.array([1, 2, 3, 4, 5])
print(arr, type(arr))  # Shows array and its type


# NumPy array with mixed data types
# NumPy converts everything to string because of "prime"
arr2 = np.array([1, 2, 3, 4, 5, "prime"])
print(arr2, type(arr2), arr.dtype)


# Create a 2D NumPy array (matrix)
arr2D = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print(arr2D, arr2D.shape)  # shape = rows, columns


# --------- Special NumPy arrays ---------

# Create an array filled with zeros (2 rows, 3 columns)
arr1 = np.zeros((2, 3), dtype="int64")
print(arr1, arr1.shape)

# Create an array filled with ones
arr2 = np.ones((2, 3))
print(arr2, arr2.shape)

# Create an array filled with a fixed value (100)
arr3 = np.full((3, 4), 100)
print(arr3, arr3.shape)


# --------- Identity matrix ---------

# Create an identity matrix (diagonal = 1, rest = 0)
arr4 = np.eye(3)
print(arr4, arr4.shape)

# Identity matrix means:
# - Square matrix
# - Diagonal elements are 1
# - All other elements are 0


# --------- Range and evenly spaced values ---------

# Create values from 1 to 9 with step size 1
arr5 = np.arange(1, 10, 1)
print(arr5, arr5.shape)

# Create 4 evenly spaced values between 1 and 100
arr5 = np.linspace(1, 100, 4)
print(arr5, arr5.shape)

#properties
arr=np.array([[1, 2, 3],[4, 5, 6],[7,8,9]])
print(arr, arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.ndim)

float_arr=arr.astype(np.float64)
print(float_arr,float_arr.shape)

#operations on array
arr=np.array([[1, 2, 3],[4, 5, 6]])
print(arr,arr.shape)
reshaped=arr.reshape(3,2)
print(reshaped,reshaped.shape)


#indexing
arr=np.array([[1, 2, 3],[4, 5, 6]])
print(arr[0][2])  #1
  #4
print(arr[1],[1])
arr10=np.array([1,2,3,4,5])
print(arr[arr10>2])
print(arr[arr10%2==0])
print(arr[arr10%2!=0])
import numpy as np

# Create a 1D NumPy array
arr11 = np.array([1, 2, 3, 4, 5])

# Slice the array from index 1 to 3 (4 is excluded)
print(arr11[1:4])  # Output: [2 3 4]

# Slice the array with a step of 2 (every second element)
print(arr11[::2])  # Output: [1 3 5]
#
nums=[1,2,3,4,5]
print(nums)
sunlist=nums[1:3]

sublist=nums[::2]
arr= np
import numpy as np

arr11 = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])

arr23 = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])

print(arr11.shape)
print(arr23.shape)


arr40 = np.array([[1, 2],
                  [3, 4]])

mean = np.mean(arr40)
std_dev = np.std(arr40)

normalized_arr = (arr40 - mean) / std_dev

print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Normalized Array:")
print(normalized_arr)
print(mean)
print(std_dev)
arr45=np.array([1,2,3,4,5])
print(np.sum(arr45))
print(np.prod(arr45))
print(np.mean(arr45))
print(np.mean(arr45))
print(np.max(arr45))
print(np.argmin(arr45))
print(np.argmax(arr45))
print(np.mean(arr45))
print(np.median(arr45))
print(np.var(arr45))
#power function
print(np.array([1,2,3,4,5])) 

