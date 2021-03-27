"""
Given a list A of elements of length N, ranging from 1 to N. All elements may not be present in the array. If the element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present display -1 at that place.

Input Format:
The first line contains n numbers with each number separated by a space.

Output Format:
Print the elements of the list after the modification.

Example:

Input:
-1 -1 6 1 9 3 2 -1 4 -1

Output:
-1 1 2 3 4 -1 6 -1 -1 9

Explanation:
The modified list contains elements such that A[i] = i.
"""
l=[int(i) for i in input().split()]
ans=[]
for i in range(len(l)):
  if (i in l):ans.append(i)
  else:ans.append(-1)
for i in ans:
  if i==len(ans)-1:
    print(i,end="")
  else:
    print(i,end=" ")
