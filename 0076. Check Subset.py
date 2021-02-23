t=int(input())
for i in range(t):
  n1=int(input())
  s1=list(map(int,input().split()))
  n2=int(input())
  s2=list(map(int,input().split()))
  s1=set(s1)
  s2=set(s2)
  print(s1.issubset(s2))
