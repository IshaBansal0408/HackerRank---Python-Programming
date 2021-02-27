import re
n=int(input())
for i in range(n):
    no=input()
    if(len(no)!=10):
        print("NO")
    else:
        for i in no:
            if(not i.isdigit()):
                print("NO")
                break
        else:
            x=re.search('^[789]',no)
            if(x is not None):
                print("YES")
            else:
                print("NO")
