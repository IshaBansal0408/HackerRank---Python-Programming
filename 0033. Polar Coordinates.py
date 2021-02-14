from cmath import *
n=complex(input())
r=n.real
i=n.imag
print(abs(complex(int(r),int(i))))
print(phase(complex(int(r),int(i))))
