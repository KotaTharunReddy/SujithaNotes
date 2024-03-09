# Contents
# np.array (distance_traveled) -> np.array is used to convert list into array
# print(d_arr.itemsize,' bytes') -> itemsize: returns size of single element from given array.
# np.arange(SIZE) -> arange() function in NumPy is used to create ndarray with evenly spaced values within a specified range.
# DataType -> w_arr.dtype
# Shape (Rows x Cols) -> w_arr.shape
# Dimensions -> w_arr.ndim
# Count of Elements -> w_arr.size
# Memory Occupied by 1 element -> w_arr.itemsize,' bytes'
# Memory Occupied by whole Matrix ', w_arr.nbytes, ' bytes'
# Reshape -> one_arr.reshape(5,4)
# converting 2d array into 1d array flat array -> two_arr.flatten()
# all ones -> np.ones((5,5))
# all zeros -> np.zeros((5,5))
# np.eye(5,5) -> used to generated identity matrix
# np.full((5,5),7) -> generating matix with your choice of value
# np.linalg.solve() -> is used to solve the linear equations

# NumPy is a Python library for numerical computing, providing powerful data
# structures and operations for handling large arrays and matrices.


# Matplotlib is a Python library for creating static, interactive, 
# and animated visualizations in a variety of formats.

# Five important methods in Matplotlib:

# 1. plt.plot(x,y): Plot lines and/or markers on a graph.
# 2. plt.scatter(x,y): Create a scatter plot of x vs y.
# 3. plt.xlabel('X-axis'): Set the label for the x-axis.
# 4. plt.ylabel('Y-axix'): Set the label for the y-axis.
# 5. plt.title('Example Plot'): Set the title of the plot.

# Numpy
# previous python involves = Data + Logics
# Data + Science (Missing) 
# in our approach science is missing i.e, usage of compute and analyze data
# not processing data using scientific methods 
# so this science factor is missing.

# first approach should be adding maths to our coding
# i.e, analyzing data statistically

# solid example detol kills 99% of Germs!
# They Conducted Multiple Statistical Test /
# Produced Evidences / Validated if 
# Evidence are supporting the statement.

# Dettol kills 99% of Germs! then only approved
# for printing.

# basic python functions aren't enough for all the
# mathematical computations
# like logarithms, mathamatical or statistical features.

# therefore here comes numpy

# Numpy

# What is Numpy?
# Numpy is a fundamental library that provides mainly 2 functionalities.
# 1. it provides build in functinalities that help you extract / work with mathematical operations
# say for eg. logarithms, trignometry, algebra etc.

# 2. it provides funtionalities to create arrays of any dimension (1D/2D/3D/ND) and provides rich
# built in functionalities to manipulate arrays.

# Numpy provides its own Data Structure for storing & processing of Data, it is called ND Array.
# (N Dimensional)

import numpy as np

# sample data : distance traveled by 5 bike riders
distance_traveled = [210, 250, 110, 150, 160]

# np.array is used to convert list into array

d_arr = np.array (distance_traveled)

# what is d_arr?
type(d_arr)

#what does it contains?
d_arr

# Let us do Data Analysis using mathematics

# Data
print(d_arr)

print('Longest Distance traveled ', d_arr.max())
print('Shortest distance traveled ',d_arr.min())
print('Total distance traveled ', d_arr.sum())
print('Average distance traveled ', d_arr.mean())
print('Distance median value ', np.median(d_arr))
print('Standard Deviation ', d_arr.std())

# Python vs Numpy

# Python list
print(distance_traveled)

# nd array
print(d_arr)

# objective: you are asked to increment each element by 1

d_arr + 1

# Vectorization
# Vectorization enables us to compute each element of given array without requiring a for loop

# Memory Utilization Test
# Objective: you are asked to find how much memory is consumed by 1 integer in python vs numpy

# Python test
import sys
print(sys.getsizeof(5),' bytes')

# Numpy test
print(d_arr.itemsize,' bytes') # itemsize: returns size of single element from given array.

# Speed Test | Which is Faster?
# objective: you are asked to add 1 million numbers using python vs numpy

# one taking less time will be the winner.

import time

SIZE = 1000000

A1 = range(SIZE)
A2 = range(SIZE)

L1 = np.arange(SIZE)
L2 = np.arange(SIZE)

# python test
start = time.time() #capturing current time
result = [x+y for x,y in zip(A1,A2)]
stop = time.time()

print('Python Took ', (stop-start) * 1000, 'ms')

#numpy test
start = time.time()
result = L1 + L2
stop = time.time()
print('Numpy Took ', (stop - start) * 1000, 'ms')

# Creating and Working with 2D Array

# we are provided with weather info
# columns represent year 1990, 1991, 1992
# row represents months jan/feb/mar/apr

weather_info = [
    [12, 11, 14],
    [11, 15, 19],
    [16, 14, 15],
    [13, 12, 19]
]

# technically above is a nested list

w_arr = np.array(weather_info)
print(w_arr)

# Learn to inspect matrix

print(w_arr)
print('DataType ',w_arr.dtype)

print('Shape (Rows x Cols) ', w_arr.shape)

print('Dimensions ', w_arr.ndim)

print('Count of Elements ', w_arr.size)

print('Memory Occupied by 1 element ', w_arr.itemsize,' bytes')

print('Memory Occupied by whole Matrix ', w_arr.nbytes, ' bytes')

# Indexing in Matrix
# Syntax: Array[RowIndex, ColIndex]

print(w_arr)
print(w_arr[2,2])

print(w_arr[3,0])

# Matrix Slicing

# fancy stunt

# 1d array
one_arr = np.arange(1,21)
# print(one_arr)

two_arr = one_arr.reshape(5,4)
# print(two_arr)

print(two_arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]

# targeted submatix: 1, 2
#                    5, 6
#                    9, 10

# Row index covered : 0,1,2 [ : 3]
# Col index covered : 0,1   [ : 2]

two_arr[: 3, :2]
# [[ 1  2  3  4]  
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]
print(two_arr[:3,:2])
# 1, 2
# 5, 6
# 9, 10

# [[ 1  2  3  4]  
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]

# Challenge: targeted array: 6 7
                        #    10 11
                        #    14 15
print(two_arr[1:4,1:3])

# Flip : left to right
# [[ 1  2  3  4]  
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]

print(two_arr[:,::-1])
# output:
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]
#  [16 15 14 13]
#  [20 19 18 17]]

print(two_arr[::-1,:])
# output:
# [[17 18 19 20]
#  [13 14 15 16]
#  [ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

# converting 2d array into 1d array flat array
flat_arr = two_arr.flatten()
print(flat_arr)

# Flitering elements

# elements < 6
flat_arr [ flat_arr < 6]
print(flat_arr)

# even elements
print(flat_arr[flat_arr % 2==0])

#odd elements
print(flat_arr[flat_arr%2!=0])

# negation (odd elements)
print(flat_arr[ ~ (flat_arr % 2 == 0)])

print(flat_arr[ ~ (flat_arr < 6)])

# Axis in Matrix

print(w_arr)

print('Maximum temperature Each Year, Column Wise Max ')
print(w_arr.max(axis=0))

print('Maximum temperature each month, row wise Max ')
print(w_arr.max(axis = 1))

# note : axis = 0 is representing Column orientation
# axis = 1 is representing Row orientation

# Bonus Functions

print(np.ones((5,5)))

print(np.zeros((5,5)))

print(np.eye(5,5))   # used to generated identity matrix

print(np.full((5,5),7)) # generating matix with your choice of value

print(np.ones((5,5),dtype=int)) # to explicetly specify value to be in int by default it takes float values

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x)
# [[1 2]
#  [3 4]]

print(y)
# [[5 6]
#  [7 8]]

print(np.hstack((x,y))) # horizontally stacked
# [[1 2 5 6]
#  [3 4 7 8]]

print(np.vstack((x,y))) # vertically stacked
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print(x+y)
print(x-y)
print(x/y)
print(x%y)
print(x*y)

# Solving Linear Equations using Numpy

# on day 1 i sold 6 type A mangoes and 3 type B mangoes for rs 27 INR.
# on day 2 i sold 9 type A mangoes and 4 type B mangoes for 4s 38 INR.

# you are asked to find the price of each type A and type B mango.

# 6A + 3B = 27
# 9A + 4B = 38

# define coefficients 
coeff = np.array ( [[6, 3], [9, 4]])

# define constants
const = np.array([27, 38])

# np.linalg.solve() is used to solve the linear equations

result = np.linalg.solve( coeff , const )
print(result)

# practice exercise
# 4a + 2b + 5c = 53
# 5a + 3b + 7c = 74
# 9a + 2b + 6c = 73

print(4 * 3 + 2 * 8 + 5 * 5 == 53)

# find the value of a,b,c
coeff = np.array ( [[4,2,5], [5,3,7], [9,2,6]])
const = np.array([53, 74, 73])
result = np.linalg.solve(coeff, const)
print(result)










