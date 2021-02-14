"""Problem 10:
        Given the names and grades for each student in a class of  students,
        store them in a nested list and print the name(s) of any student(s)
        having the second lowest grade.
"""
if __name__ == '__main__':

# Create List
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    l.sort(key=lambda x:x[1])

# Find second highest score
    temp=l[0][1]
    for i in range(1,len(l)):
        if(temp!=l[i][1]):
            temp=l[i][1]
            break

# Get names of second highest scorers
    n=[]
    for i in range(len(l)):
        if(temp==l[i][1]):
            n.append(l[i][0])

# Print the names in alphabetical order
    n.sort()
    for i in n:
        print(i)
            
            
        
