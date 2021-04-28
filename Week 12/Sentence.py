"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalised.

Input Format:
The first line of the input contains a number n which represents the number of line.
From second line there are statements which has to be converted. Each statement comes in a new line.

Output Format:
Print statements with each word in capital letters.

Example:

Input:
2
Hello world
Practice makes perfect

Output:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

n=int(input())
for i in range(n):
  print(input().upper(),end="")
  if i!=n-1:
    print()
    
    
    or
    
    
lines = []
n = int(input())
for i in range(n):
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)    
