n,x=input().split()
l=[]
for i in range(int(x)):
  t=input().split()
  l+=[t]
for i in range(int(n)):
  val=0
  for j in l:
    val+=float(j[i])
  print(round(float(val)/(int(x)),1))
  
