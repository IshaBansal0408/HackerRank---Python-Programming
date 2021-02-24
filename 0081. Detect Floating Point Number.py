n,l=int(input()),list()
for i in range(n):
  t=input()
  l.append(t)
for i in l:
  try:
    if(float(i)==0):
      ans=False
    else:
      i=float(i)
      ans=True
  except ValueError:
    ans=False
  finally:
    print(ans)
