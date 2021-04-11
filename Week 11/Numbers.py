"""
Write a program, which will find all such numbers between m and n (both included) such that each digit of the number is an even number.

Input Format:
The first line contains value m and n separated by a comma.

Output Format:
The numbers obtained should be printed in a comma-separated sequence on a single line.

Constraints:
1000<=m<=9000
1000<=n<=9000
"""

(b,e)=input().split(',')
(b,e)=(int(b),int(e))
f=[]
for i in range(b,e+1,2):
  l=list(str(i))
  for x in l:
    if int(x)%2!=0:
      break
  else:
    f.append(str(i))
print(",".join(f),end="")

or

m,n = input().split(',')
m = int(m)
n = int(n)

values = []
for i in range(m, n+1):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
