import re

# Take input
S = input()
k = input()

#search for pattern
m = re.search(k, S)
#compile the pattern and keep it saved
pattern = re.compile(k)

# if pattern is not found pring the req output
if not m:
    print("(-1, -1)")

while m:
    # Printing starting and ending of the pattern found
    print("({0}, {1})".format(m.start(),m.end()-1))
    
    # search the pattern in S starting after previous m.start()
    m = pattern.search(S,m.start()+1)
