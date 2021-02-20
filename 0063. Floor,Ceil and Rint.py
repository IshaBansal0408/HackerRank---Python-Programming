import numpy
numpy.set_printoptions(sign=' ')
n=input().split()
arr=[]
for i in n:
  arr.append(float(i))
n=numpy.array(arr)
print(numpy.floor(n))
print(numpy.ceil(n))
print(numpy.rint(n))
