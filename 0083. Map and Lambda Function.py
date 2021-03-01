cube = lambda x: x*x*x

def fibonacci(n):
  a=[]
  for i in range(n) :
    if i <= 1 :
      a.append(i)
    else:
      f = int(a[i-2])+int(a[i-1])
      a.append(f)
  return a
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
