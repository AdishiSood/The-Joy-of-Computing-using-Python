"""
Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates. 

Input Format:
The first line contains n-1 numbers with each number separated by a space.

Output Format:
Print the missing number

Example:

Input:
1 2 4 6 3 7 8

Output:
5

Explanation:
In the above list of numbers 5 is missing and hence 5 is the input
"""
l=[int(i) for i in input().split()]
n=(len(l)+1)*(len(l)+2)//2
for i in l:
  n=n-i
print(n,end="")


or
