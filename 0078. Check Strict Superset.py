A=list(map(int,input().split()))
A=set(A)
n=int(input())
l=[]
for i in range(n):
  s=list(map(int,input().split()))
  s=set(s)
  l.append(A.issuperset(s))
for i in l:
  if(i is False):
    print(False)
    break
else:
  print(True)    
