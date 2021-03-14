"""
Given a string S of lowercase letters, remove consecutive vowels from S.
After removing, the order of the list should be maintained.

Input Format:
Sentence S in a single line

Output Format:
Print S after removing consecutive vowels

Example:
Input:
your article is in queue

Output:
yor article is in qu

Explanation:
In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed.
In the fifth word, 'u', 'e', 'u' and 'e' are appearing together, hence 'e', 'u', 'e' are removed.
"""
def isVowel(x):
  if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    return True
  else:
    return False

s=input()
r=""
i=0
while(i<len(s)):
  
  if(isVowel(s[i])):
      r= r + s[i]
      while(i<len(s) and isVowel(s[i])):
           i=i+1
  else:
      r=r + s[i]
      i=i+1      
           
print(r,end="")
