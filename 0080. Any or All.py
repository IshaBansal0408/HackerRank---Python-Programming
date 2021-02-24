n,l=int(input()),input().split()
print((all([int(i)>0 for i in l]))and(any([i==i[::-1] for i in l])))
