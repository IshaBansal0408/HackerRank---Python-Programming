import math
AB=int(input())
BC=int(input())
AC=AB*AB+BC*BC
AC=math.sqrt(AC)
MC=AC/2
angle=math.atan2(AB,BC)
ans=str(round(math.degrees(angle)))
print(ans+"°")
