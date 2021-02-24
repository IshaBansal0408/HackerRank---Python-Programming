import re
n=int(input())
for i in range(n):
  case=input()
  try:
    re.compile(case)
    print(True)
  except re.error:
    print(False)
