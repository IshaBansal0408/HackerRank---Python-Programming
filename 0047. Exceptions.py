n=int(input())
for i in range(n):
  inp=input().split()
  try:
    a=int(inp[0])
    b=int(inp[1])
    print(int(a//b))
  except ValueError as v:
    print("Error Code:",v)
  except ZeroDivisionError as z:
    print("Error Code:",z)
    
