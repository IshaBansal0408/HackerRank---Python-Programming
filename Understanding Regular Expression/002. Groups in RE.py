"""
GROUPS IN REGULAR EXPRESSION
groups() return tuple containing all the captured groups
"""
import re
m=re.search('(\d+),(\d+),(\d+)','123,12763,773687')
print(m)
print(m.groups())

"""
GROUPS IN REGULAR EXPRESSION
group(n) return nth group
"""
print("Empty Group: ",m.group())
print("Group 0: ",m.group(0))
print("Group 1: ",m.group(1))
print("Group 2: ",m.group(2))

print("Group 1 and 2: ",m.group(1,2))
print("Group 2 and 3: ",m.group(2,3))
print("Group 3 and 2: ",m.group(3,2))
print("Group 1,2 and 3: ",m.group(1,2,3))




