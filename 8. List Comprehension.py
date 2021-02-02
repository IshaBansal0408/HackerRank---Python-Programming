"""Problem 8:Take 4 inputs: x,y,z and an integer n
        Print a list of all possible coordinates given by (i,j,k)
        where i+j+k is not equal to n
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print( [[i,j,k]
        for i in range( x + 1)
        for j in range( y + 1)
        for k in range(z+1)
        if ( ( i + j + k ) != n )])
