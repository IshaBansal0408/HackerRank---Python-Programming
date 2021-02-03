# ONLY ONE PRINT STATEMENT ALLOWED

for i in range(1,int(input())+1): 
  print(int((10**i-1)/9)**2) 

"""
# MORE THAN ONE PRINT STATEMENT
n=int(input())
for i in range(1,n+1):
    k=1
    l=i-1
    for j in range(2*i-1):
        if(k<=i):
            print(k,end="")
            k=k+1
        elif(k>i):
            print(l,end="")
            l=l-1
    print("\n")
"""
