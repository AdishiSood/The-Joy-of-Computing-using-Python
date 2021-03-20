"""
Given a string, you need to convert all lowercase letters to uppercase letters and vice versa.

Input Format:
A single line containing a string S.

Output Format:
Print the modified string S.

Sample Input:
Hello World!!

Sample Output:
hELLO wORLD!!
"""
s = input()


def convert(ss):
    # Convert it into list and then change it
    newSS = list(ss)
    for i,c in enumerate(newSS):
        newSS[i] = c.upper() if c.islower() else c.lower()
    # Convert list back to string
    return ''.join(newSS)


print(convert(s))
