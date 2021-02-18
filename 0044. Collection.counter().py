from collections import Counter

n=int(input())
shoe_list=input().split()
shoe_list=list(map(int,shoe_list))
shoe_list=Counter(shoe_list)

nc=int(input())

profit=0
for i in range(nc):
    c=list(map(int,input().split()))
    for i in shoe_list.keys():
        if(i==c[0]):
            temp=shoe_list[i]
            if(temp!=0):
                temp=temp-1
                shoe_list[i]=temp
                profit+=c[1]
print(profit)
    
