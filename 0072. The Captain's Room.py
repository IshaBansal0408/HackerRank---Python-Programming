K = int(input())
set_S = set()
sumlist_S = 0
for i in input().split():
    I = int(i)
    set_S.add(I)
    sumlist_S+= I

print((sum(set_S)*K-sumlist_S)//(K-1))


"""
SOLUTION 1 : USING SETS (Rejected due to time)
n=int(input())
rooms=list(map(int,input().split()))
rooms_s = set(rooms)
l=[]
for i in rooms_s:
  l.append((i,rooms.count(i)))
for i in l:
  if(i[1]!=n):
    print(i[0])

SOLUTION 2 : USING DICTIONARIES (Rejected due to time)
n=int(input())
rooms=list(map(int,input().split()))
d={}
for i in rooms:
  l=list(d.keys())
  if(i in l):
    d[i]+=1
  else:
    d[i]=1
for i in list(d.keys()):
  if(d[i]!=n):
    print(i)
"""
