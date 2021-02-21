import numpy as np
arr=np.array(list(map(int,input().split())))
arr1=np.array(list(map(int,input().split())))
print(np.inner(arr,arr1))
print(np.outer(arr,arr1))

