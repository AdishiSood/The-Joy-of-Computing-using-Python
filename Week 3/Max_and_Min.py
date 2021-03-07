"""
Given a list of numbers (integers), find second maximum and second minimum in this list.

Input Format:
The first line contains numbers separated by a space.

Output Format:
Print second maximum and second minimum separated by a space
"""

a = [int(x) for x in input().split()]
a.sort() #this command sorts the list in ascending order
print(a[-2],a[1])
