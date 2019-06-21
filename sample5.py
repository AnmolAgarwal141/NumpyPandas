import numpy as np
arr=np.arange(10)
print(arr)
np.save('saved_array',arr)
load_array=np.load('saved_array.npy')
print(load_array)

arr1=np.arange(15)
#np.savez('saved_archive.npz',x=load_array,y=arr1)
np.savez('saved_archive.npz',x=arr,y=arr1)
load_archive=np.load('saved_archive.npz')
arr2=load_archive['x']
print(arr2)
arr3=load_archive['y']
print(arr3)

np.savetxt('arraytxt.txt',arr3,delimiter=',')
txtarray=np.loadtxt('arraytxt.txt',delimiter=',')
print(txtarray)