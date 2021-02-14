m=int(input())
M=input().split()
n=int(input())
N=input().split()

M1=list(map(int,M))
N1=list(map(int,N))

S1=set()
S2=set()
for i in M1:
  S1.add(i)
for i in N1:
  S2.add(i)

S3=S2.difference(S1)
S4=S1.difference(S2)
for i in S3:
  S4.add(i)
S4=sorted(S4)
for i in S4:
  print(i)
