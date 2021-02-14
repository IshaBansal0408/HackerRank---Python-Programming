if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    l.sort(reverse=True)
    temp=l[0]
    for i in range(1,len(l)):
        if(l[i]!=temp):
            temp=l[i]
            break
    print(temp)
