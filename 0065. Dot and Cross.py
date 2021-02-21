import numpy as np
n=int(input())
arr=[]
for i in range(n):
  s=list(map(int,input().split()))
  arr.append(s)
arr1=[]
for i in range(n):
  s=list(map(int,input().split()))
  arr1.append(s)
arr=np.array(arr)
arr1=np.array(arr1)

print(np.dot(arr,arr1))
