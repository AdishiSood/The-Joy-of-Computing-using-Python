"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Input Format:
The first line of the input contains a statement.

Output Format:
Print the number of upper case and lower case respectively separated by a space.

Example:

Input:
Hello world!

Output:
1 9
"""
istr=input()
countu=0
countl=0
for i in istr:
  val=ord(i)
  if(val>=65 and val<=90):
    countu+=1
  if(val>=97 and val<=122):
    countl+=1
print(countu,countl,end="")

or

s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print(d['UPPER CASE'],d['LOWER CASE'])
