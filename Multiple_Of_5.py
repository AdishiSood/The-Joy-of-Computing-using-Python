a = [int(x) for x in input().split()]
b = []
for i in a:
    if(i%5!=0):
        b.append(i)
for i in range(len(b)):
    if(i==len(b)-1):
        print(b[i],end="")
    else:
        print(b[i],end=" ")
