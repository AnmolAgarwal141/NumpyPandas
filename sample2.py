import numpy as np
arr=np.arange(0,11)
print(arr)
print(arr[0:5])
print(arr[10])
arr[0:3]=1
print(arr)

arr1=arr[0:5]
print(arr1)
arr1[:]=10
print(arr1)
print(arr)
arr2=arr.copy()
arr2[:]=5
print(arr2)
print(arr)