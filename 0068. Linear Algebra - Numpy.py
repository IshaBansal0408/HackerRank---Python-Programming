import numpy as np
n=int(input())
arr=[]
for i in range(n):
  s=list(map(float,input().split()))
  arr.append(s)
arr=np.array(arr)
print(round(np.linalg.det(arr),3))
