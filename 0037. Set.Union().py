n=int(input())
N=set(input().split())
m=int(input())
M=set(input().split())
T=N.union(M)
print(len(T))
