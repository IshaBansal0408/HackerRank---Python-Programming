import calendar
n=input().split()
n=list(map(int,n))
val=calendar.weekday(n[2],n[0],n[1])
if(val==0):
  print("MONDAY")
elif(val==1):
  print("TUESDAY")
elif(val==2):
  print("WEDNESDAY")
elif(val==3):
  print("THURSDAY")
elif(val==4):
  print("FRIDAY")
elif(val==5):
  print("SATURDAY")
else:
  print("SUNDAY")
