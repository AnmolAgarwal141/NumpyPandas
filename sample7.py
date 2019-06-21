import numpy as np

x=np.array([110,100,90,80])
y=np.array([10,20,30,40])
condition=np.array([True,True,False,False])

z=[a if cond else b for a,cond,b in zip(x,condition,y)]
print(z)
z2=np.where(condition,x,y)
print(z2)
z3=np.where(x>=0,0,-1)
print(z3)

print(x.sum())

n=np.array([[1,2,3],[4,5,6]])
print(n.sum(0))
    print(x.mean())
    print(x.std())
    print(x.var())

print(condition.any()) #or
print(condition.all()) #and

unsort=np.array([6,-1,5,2,10,0])
unsort.sort()
print(unsort)
arr2=np.array(["solid","liquid","liquid","solid","gas","gas","gas"])
print(np.unique(arr2))
print(np.in1d(["solid","plasma","gas"],arr2))

