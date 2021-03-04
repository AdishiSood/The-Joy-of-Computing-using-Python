n,v1,v2=input().split(" ")
n,v1,v2=int(n),int(v1),int(v2)
tv1=(2**.5*n/v1)
tv2=(2*n/v2)
if(tv1>tv2):
  print("Cab",end="")
else:
  print("Walk",end="")
