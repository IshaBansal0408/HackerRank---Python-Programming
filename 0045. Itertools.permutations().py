from itertools import permutations

n=input().split()
print(n)
res=permutations(n[0],int(n[1]))
for i in sorted(res):
    string=""
    for j in i:
        string+=j
    print(string)
