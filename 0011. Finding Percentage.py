if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    l=student_marks[query_name]
    l=list(l)
    ans=0
    for i in l:
        ans=ans+i
    ans=ans/len(l)
    print(format(ans,'.2f'))
