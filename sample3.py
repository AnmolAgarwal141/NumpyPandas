import numpy as np
arr2d=np.array([[1,2,3],[2,3,4],[3,4,5]])
print(arr2d)
print(arr2d[0])
print(arr2d[0][1])
print(arr2d[0:2,0:2])
print(arr2d[:2,1:])
print(arr2d[:,1:])
arr2d[:2,1:]=50
print(arr2d)
arr_len=arr2d.shape
print(arr_len)
arr_len1=arr2d.shape[0]
print(arr_len1)
for i in range(arr_len1):
    arr2d[i]=i
print(arr2d)
print(arr2d[[0,1,2]])
print(arr2d[[2,0,1]])
