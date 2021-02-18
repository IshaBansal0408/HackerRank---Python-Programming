from itertools import product
A=input().split()
B=input().split()
A=list(map(int,A))
B=list(map(int,B))
C=list(product(A,B))
for i in C:
  print(i,end=" ")
