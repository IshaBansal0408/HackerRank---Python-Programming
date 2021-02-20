import numpy
n=input().split()
arr=[]
for i in range(int(n[0])):
  s=list(map(int,input().split()))
  arr.append(s)
arr=numpy.array(arr)
s=numpy.min(arr,axis=1)
t=numpy.max(numpy.array(s))
print(t)

