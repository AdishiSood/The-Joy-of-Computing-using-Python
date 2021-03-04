#Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order. 

#Input Format:
#The first line of the input contains N distinct integers of list A separated by a space.

#Output Format
#Print the minimum number of moves required to sort the elements.

#Example:

#Input:
#1 3 2 4 5

#Output:
#3

#Explanation:
#In the first move, we move 3 to the end of the list. In the second move, we move 4 to the end of the list, and finally, in the third movement, we move 5 to the end.

arr = [int(x) for x in input().split()]
arr1 = sorted(arr)
count = 0
for i in range(len(arr)):
    if arr[i] == arr1[count]:
        count+=1
print(len(arr)-count)
