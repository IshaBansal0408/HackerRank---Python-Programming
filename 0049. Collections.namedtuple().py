from collections import namedtuple
n = int(input())
scol = ','.join(input().split())
Student =namedtuple('Student',scol)
sum = 0
for i in range(n):
    row = input().split()
    student = Student(*row)
    sum += int(student.MARKS)
print(sum/n)
