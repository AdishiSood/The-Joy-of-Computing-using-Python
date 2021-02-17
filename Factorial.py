/*

Given an integer number n, you have to print the factorial of this number. 

Input Format:

A number n.

Output Format:

Print the factorial of n.

Example:

Input:
4

Output:
24

*/

k = int(input())
fac = 1
for i in range(1,k+1):
    if(k==0):
        break
    fac=fac*i
print(fac)
