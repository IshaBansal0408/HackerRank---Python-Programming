def print_rangoli(size):
    row=2*size-1
    col=3*size+(size-3)
    print("No of rows: ",row)
    print("No of col: ",col)
    for i in range(row):
        for j in range(col):
            value=str(i)+str(j)
            print(value,end=" ")
        print("\n")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
