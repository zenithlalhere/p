#ques 1 

import numpy as np
from numpy import random

arr = np.random.randint(0,100, size=(5,2))
print("The random array is: ")
print(arr)

random_mean = np.mean(arr, axis=1)
print("Mean: ",random_mean)

random_std = np.std(arr, axis=1)
print("Standard Deviation: ",random_std)

random_var = np.var(arr, axis=1)
print("Variance: ",random_var)

m = eval(input("Enter the value of M: "))
n = eval(input("Enter the value of N: "))

arr2 = np.random.randint(0,100,size=(m,n))
print("New array:")
print(arr2)
print('Shape of array:',arr2.shape)
print('Type: ',type(arr2))
print('Data type: ',arr2.dtype)

arr3 = arr2.reshape(n,m)
print("Transposed matrix: ")
print(arr3)

arr4 = np.array([1,2,3,0,0,3,np.nan,0,np.nan,np.nan,2])
print("One D array is: ")
print(arr4)
print("Indecies of zero")
zero_indecies = np.where(arr4==0)[0]
print(zero_indecies)

print("Indecies of Non Zero")
non_zero_indecies = np.where(arr4!=0)[0]
print(non_zero_indecies)

print("Indecies of NaN")
nan_indecies= np.where(np.isnan(arr4))[0]
print(nan_indecies)


Array1 = np.random.randint(100,size=(3,4))
Array2 = np.random.randint(100,size=(3,4))
Array3 = np.random.randint(100,size=(3,4))
print("Array1: ")
print(Array1)
print("Array2: ")
print(Array2)
print("Array3: ")
print(Array3)

print("Array4: ")
Array4 = Array3 - Array2
print(Array4)

print("Array5: ")
Array5 = Array1*2
print(Array5)

print("Covariance between Array1 and Array4: ",np.cov(Array1, Array4))
print("Correlation between Array1 and Array5: ",np.corrcoef(Array1, Array5))

new_Array1 = np.random.randint(100,size=(10))
print("Array. 1: ", new_Array1)

new_Array2 = np.random.randint(100,size=(10))
print("Array. 2: ", new_Array2)

sum_array_half = new_Array1[:5]+new_Array2[:5]
print("Sum of first halfs for the array: ",sum_array_half)

product_array_half = new_Array1[5:]*new_Array2[5:]
print("Product of second halfs for the array: ",product_array_half)
