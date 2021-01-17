list1=input()
#print(list1)
x=list1.count('1')
y=list1.count('0')
l=len(list1)
#print(x,y,l)
if x==l-1 and y==1:
  print("YES",end='')
elif x==1 and y==l-1:
  print("YES",end="")
else:
  print("NO",end="")
