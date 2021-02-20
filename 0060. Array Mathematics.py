import numpy
n=input().split()
arr=[]
arr1=[]
for j in range(int(n[0])):
    s=list(map(int,input().split()))
    arr.append(s)
for j in range(int(n[0])):
    s=list(map(int,input().split()))
    arr1.append(s)
arr=numpy.array(arr)
arr1=numpy.array(arr1)

r1=numpy.add(arr,arr1)
r2=numpy.subtract(arr,arr1)
r3=numpy.multiply(arr,arr1)
print(r1)
print(r2)
print(r3)

r4=numpy.divide(arr,arr1)
r4=r4.astype('int64') 
r5=numpy.mod(arr,arr1)
r5=r5.astype('int64') 
print(r4)
print(r5)

r6=numpy.power(arr,arr1)
print(r6)
