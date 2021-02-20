import numpy as np
n,m=list(map(int,input().split()))
arr=[]
for i in range(n):
  values=list(map(int,input().split()))
  arr.append(values)
arr=np.array(arr)
print(np.transpose(arr))
print(arr.flatten())
