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

    
    or
    
    def fix( A, len): 
      
    for i in range(0, len):  
          
        if (A[i] != -1 and A[i] != i): 
            x = A[i]; 
  
            # check if desired place 
            # is not vacate 
            while (A[x] != -1 and A[x] != x): 
                #store the value from 
                # desired place 
                y = A[x] 
  
                # place the x to its correct 
                # position 
                A[x] = x 
  
                # now y will become x, now 
                # search the place for x 
                x = y 
              
            # place the x to its correct 
            # position 
            A[x] = x; 
  
            # check if while loop hasn't 
            # set the correct value at A[i] 
            if (A[i] != i) : 
                  
                # if not then put -1 at 
                # the vacated place 
                A[i] = -1; 
  
# Driver function. 
A = [] 
A= list(map(int, input ().split ())) 
  
fix(A, len(A)) 
  
for i in range(0, len(A)):
    if(i==len(A)-1):
        print(A[i],end = '')
    else:
        print (A[i],end = ' ') 
