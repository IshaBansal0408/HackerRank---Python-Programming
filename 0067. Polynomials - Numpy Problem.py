import numpy as np
n=list(map(float,input().split()))
x=int(input())

print(np.polyval(n,x))
