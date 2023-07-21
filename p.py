#       what we will learn today 
#   what is numpy ?
# what is numpy array ?
# numpy vs python list ?
# installation and import numpy ?
# importance of numpy in python ?
            # what is numpy
#   > numpy is the fundamental package for scientific computing in python
#   > numpy is a python library that provides a multidimensional array object,
# various derives object

#  >


#  what is numpy array
# > An array is a grid of values and it contain information about the raw 
# data,  how to locate an element, and how to interpret an element 
# 1 d array shape(2) , axis(0)
# 2d array shape(3,4) , axis(0,1)
# 3d array shape(4,5,4), axis(0,1,2)


# Numpy vs Python list
# > consumers less memory.
# > fast as compared to the python list.
# > convinient to use.


#  installation  and import numpy
# > pip install numpy 

# import Numpy 
# > import numpy as np 
import numpy as np # checking numpy install or not
a = np.array([1,2,3,4,5,6]) # making an array in numpy
print(a)  # printing the array
print(type(a)) # printing the type 
b = [1,2,3,4,5,6]  # making a list in python 
print(b) # printing a list in python
print(type(b)) # printing the type

#                         importance of numpy in python 
#  > wide variety of mathematical operations 
#  > it supplies an enotmous library of high-level mathematical functions that operates on these arrays and matrices.
#  > matematical , logical , shape manipulation , sorting , selecting , I/O , discrete fourier tranforms , 
#  basic linear algebra , basic statistical operations , random simulation and much more .

#                    Python lists vs numpy arrays 
#  difference between numpy array and lists in python
# > Data type storage  in lists we can work with both strings and numbers  but not in array of numpy 
# > importing module   we have to fist import the numpy package in our python 
# > numerical operations 
# > modification capability 
# > consumes less memory 
# > fast as compared to the pyhton list 
# > convinient to use#

#        creating numpy arrays 

c = np.array([1,2,3,4,5,6]) #  creating an array of numpy
print(c) #  printing the array
print(type(c))
print(c.ndim) # checking the dimensions

l = []
for i in range(1,5):
    int_1 = int(input("Enter : "))
    l.append(int_1)
print(np.array(l))

#          Dimensions of array 
#  > 1-D arrays
#  > 2-D arrays
#  > 3-D arrays 
#  > higher dimensionals array 
#             making two dimensional array 
ar2 = np.array([[1,2,3,4,],[1,2,3,4]])
print(ar2)
print(ar2.ndim)
#         making three dimensional array 
ar3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(ar3)

#       making multi dimensional array
arn = np.array([1,2,3,4],ndmin = 10)
print(arn)
print(arn.ndim) 

#  creating numpy array using numpy functins

#  special numpy arrays 

#  > Array filled with 0's
#  > Array filled with 1's
#  > Create an empty array
#  > An array with a range of elements 
#  > Array diagonal element filled with 1's
#  > Create an array with the values that are spaced linearly in a specifed interval
ar_zero = np.zeros(4)
print(ar_zero)
ar_zero1 = np.zeros((3,4))
print(ar_zero1)

ar_one = np.ones(4)
print(ar_one)

ar_em = np.empty(4)
print(ar_em)

ar_rn = np.arange(4)
print(ar_rn)

ar_dia = np.eye(3)
print(ar_dia)

# linspace

ar_lin = np.linspace(0,10,num=5)
print(ar_lin)

# create numpy array with random numbers
#  > rand() : the function is used to generate a random value between 0 to 1.
#  > randn() : the function is used to generate a random value close to zero . this may return positive or negative numbers as well.
#  > ranf() : the functions for doing random sampling in numpy.it returns an array of specified shape and fills
#  it with random floats in the half-open interval [0.0,1.0]
#  > randint() : the functions is used to generate a random between a given range.


var = np.random.rand(4)
print(var)

var1 = np.random.rand(2,5)
print(var1)

var2 = np.random.randn(5)
print(var2)

var3 = np.random.ranf(5)
print(var3)

var4 = np.random.randint(5,20,10)  # min max total_values
print(var4)

        #     Numpy data types

#  1 - bool_       Boolean (True,false) stored as a byte
#  2 - int_        Default integer type (same as C long normally either int64 or int32)
#  3 - intc        identical to C int (normally int32 and int64)
#  4 - intp        integer used for indexing (same as C ssize_t; normally either int32 or int64)
#  5 - int8        Byte (-128 to 127 )
#  6 - int16       integer (-32768 to 32767)
#  7 - int32       integer (-2147483648 to 2147483647)
#  8 - int64       integer (-9223372036854775808 to 9223372036854775807)
#  9 - uint        unsigned integer (0 to 255)
#  10 - unit16     unsigned integer (0 to 65535)
#  11 - unit32     unsigned integer (0 to 4294967295)
#  12 - unit64     unsirgned integer (0 to 18446744073709551615)
#  13 - float_     Shothand for float64
#  14 - float16    half precision float: sign bit, 5 bits exponent , 10 bits mantissa
#  15 - float32    Single precision float: sign bit, 8 bits exponent 
#  16 - float64    Double precision float : sign bit, 11 bits exponent
#  17 - complex    shorthand for complex128
#  18 - complex64  Complex number , represented by two 32-bit floats (real and imaginal components)
#  19 - complex128 Conplex number,  represented by two 64-bit float (real and imaginary components)
 #

var5 = np.array([1,2,3,4,5,6,7])
print("Data type : ",var5.dtype)

var6 = np.array([23,23,45,67,56,45,34])
new = np.float64(var6)
print(new)
print("Data Type : ",new.dtype)

#    shape and reshappe in numpy

var7 = np.array([[1,2],[1,2]])
print(var7)
print(var7.shape)

#      Reshape

var8 = np.array([1,2,3,4,5,6])
x = var8.reshape(2,3)
print(x)

#      arithmetic operations in numpy array

# > a+b    np.add(a,b)
# > a-b    np.subtract(a,b)
# > a*b    np.multiply (a,b)
# > a/b    np.divide(a,b)
# > a%b    np.mod(a,b)
# > a**b   np.power(a,b)
# > 1/a    np.reciprocal(a)


var9 = np.array([1,2,3,4])
varadd = var9 + 5
print(varadd)

var10 = np.array([1,2,3,4])
var11 = np.array([1,2,3,4])
varadd1 = var10+var11
print(varadd1)

