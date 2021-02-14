n = int(input())
s = set(map(int, input().split())) 
a = int(input())

for i in range(a):
  k = []
  k = input().split()
  if k[0] == 'pop':
    s.pop()
  elif k[0] == 'remove':
    s.remove(int(k[1]))
  elif k[0] == 'discard':
    s.discard(int(k[1]))
  else:
    print('not a command')

print(sum(s))
