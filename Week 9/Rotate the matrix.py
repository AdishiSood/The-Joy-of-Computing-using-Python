"""
Given a square matrix with n rows and n columns, you have to write a program to rotate this matrix such that each element is shifted by one place in a clockwise manner.
For example, given the following matrix

1 2 3
4 5 6
7 8 9

The output should be

4 1 2
7 5 3
8 9 6

Input Format:
The first line of the input contains a number n representing the number of rows and columns.
After this, there are n rows with each row containing n elements separated by a space

Output Format:
Print the elements of the modified matrix with each row in a new line and all the elements in each row is separated by a space.
Example 1:

Input:
3
1 2 3
4 5 6
7 8 9

Output:
4 1 2
7 5 3
8 9 6

Example 2:
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
5 1 2 3
9 10 6 4
13 11 7 8
14 15 16 12

Explanation: 
In the first example, there is an odd number of rows and columns hence excluding the middle element i.e. 5 all the elements were shifted by one position in a clockwise manner.
In the second example, there are even number of rows and columns hence all the elements were shifted by one position in a clockwise manner

"""
n=int(input())
m=[]
for i in range(n):
  l=list(map(int,input().split()))
  m.append(l)
output=[[0 for i in range(n)] for j in range(n)]
x=0;xe=n;y=0;ye=n
if(n%2==1):
  output[n//2][n//2]=m[n//2][n//2]
while(x<xe):
  for i in range(x+1,xe):
    output[y][i]=m[y][i-1]
  y=y+1
  for i in range(y,ye):
    output[i][xe-1]=m[i-1][xe-1]
  xe=xe-1
  for i in range(xe-1,x-1,-1):
    output[ye-1][i]=m[ye-1][i+1]
  ye=ye-1
  for i in range(ye-1,y-2,-1):
    output[i][x]=m[i+1][x]
  x=x+1 
for i in range(n):
  for j in range(n):
    print(output[i][j],end="")
    if(j!=n-1):
      print(" ",end="")
  if(i!=n-1):
    print()
