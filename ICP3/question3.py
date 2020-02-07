import numpy as np

a=np.random.randint(0,high=20,size=15,dtype=np.int32)
print(a)
#print(np.bincount(a).argmax())
b=a.reshape((3,5))
print(b)
c=np.amax(b, axis=1)
print(c)
b=np.where(b == np.max(b, axis=1).reshape(-1,1), 0, b)
print(b)
