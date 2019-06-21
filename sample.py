import numpy as np
my_list=[1,2,3]
my_list1=[2,3,4]
#my_array1 = np.array(my_list)
my_array1=np.array([my_list,my_list1])
print(my_array1)
print("\n",my_array1.shape)
print("\n",my_array1.dtype)
my_array2=np.zeros(4)
my_array3=np.ones([2,3])
my_array4=np.empty(4)
my_array5=np.eye(4)
my_array6=np.arange(4,20,2)
print(my_array2)
print(my_array3)
print(my_array4)
print(my_array5)
print(my_array6)

