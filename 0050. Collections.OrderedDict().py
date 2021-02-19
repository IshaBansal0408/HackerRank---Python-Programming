from collections import OrderedDict
od=OrderedDict()
n=int(input())
for i in range(n):
  s=input().split()
  item=' '.join(s[:-1])
  price=s[-1]
  if(item in od):
    od[item]+=int(price)
  else:
    od[item]=int(price)
for i in od:
  print(i,od[i])
