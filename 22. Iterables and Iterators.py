n=int(input())
s=input()
t=int(input())
letters=[]
l=[]
letters=s.split()
for i in range(1,n+1):
    for j in range(i+1,n+1):
        l.append((i,j))
ind=[]
for i in range(len(letters)):
    if(letters[i]=='a'):
        ind.append(i+1)
print(l)
print(ind)
fl=[]
for i in ind:
    if(i<=t):
        fl.append(i)
print(fl)
for i in l:
    
