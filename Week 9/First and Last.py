"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

Input Format:
The first line of the input contains the String S.

Output Format:
The first line of the output contains the modified string.

Sample Input:
Programming

Sample Output:
Prng
"""
s=input()
output=""
if(len(s)<2):
  print("",end="")
else:
  print(s[0:2]+s[-2:-1]+s[-1],end="")
