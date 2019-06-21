import numpy as np
import matplotlib.pyplot as plt
axes_values=np.arange(-100,100,10)
dx,dy=np.meshgrid(axes_values,axes_values)
print(dx)
print('\n',dy)
function =2*dx+3*dy
print('\n',function)
plt.imshow(function)
plt.title("function polt of 2dx+3dy")
plt.colorbar()
plt.savefig('fig1.png')
#function2 =np.cos(dx)+np.cos(dy)
#print('\n',function2)
#plt.imshow(function2)
#plt.title("function cos plot")
#plt.colorbar()
#plt.savefig('fig2.png')