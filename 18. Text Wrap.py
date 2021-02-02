import textwrap

def wrap(string, max_width):
  str=""
  j=0
  while(j<len(string)):
    str=str+ string[j:j+4]
    if(j+4<len(string)-1):
      str=str+"\n"
    j=j+4
  return str
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
