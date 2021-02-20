import numpy
n=input().split()
arr=[]
for i in range(int(n[0])):
  s=list(map(int,input().split()))
  arr.append(s)
arr=numpy.array(arr)

s=numpy.sum(arr,axis=0)
t=numpy.prod(numpy.array(s))
print(t)

