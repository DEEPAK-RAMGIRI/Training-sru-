# cheap travels
# Time Complexcity O(1)
# space Complexcity O(1)
# n,m,a,b = map(int,input().split()) 
# cost1= (n // m)* b + (n % m) * a
# cost2 = n*a
# cost3 =  ((n // m) + 1) * b
# print(min(cost1,cost2,cost3))


# # a 2d list 
# arr = [
#     [3,8],
#     [1,2],
#     [2,7],
#     [6,3]
# ]

# # Time Complexcity O(m^2 * n)
# # Space Complexity O(1)
# for i in range(len(arr)):
#     index = 0
#     for j in range(i,len(arr) - 1):
#         if arr[j][0] > arr[j + 1][0]:
#             arr[j],arr[j + 1] = arr[j + 1],arr[j]
#         while arr[j][index] == arr[j + 1][index]:
#             index+=1
#         if index < len(arr[0]) and arr[j][index] > arr[j + 1][index]:
#             arr[j],arr[j + 1] = arr[j + 1],arr[j]

# print(arr)
            
# from collections import deque       
# arr = deque([4,8,2,3,6,1,5])
# k = 3
# for i in range(k):
#     arr.appendleft(arr.pop())

# print(arr)
# arr = [4,8,2,3,6,1,5]
# k = 3
# for i in range(k):
#     arr.insert(0,arr.pop())


# nums= [4,8,2,3,6,1,5] 
# def function(left,right):
#     while left < right:
#         nums[left],nums[right] = nums[right],nums[left]
#         left+=1
#         right-=1

# k %= len(nums)
# function(0,len(nums) - 1)
# function(0,k - 1)
# function(k,len(nums) - 1)

# print(nums)


# nums= [4,8,2,3,6,1,5]
# k = 3
# # ans = 3 6 1 5 4 8 2

# # thinking reverse the nums y
# def function(left,right):
#     while left < right:
#         nums[left],nums[right] = nums[right],nums[left]
#         left+=1
#         right-=1
       
# k %= len(nums)
# function(0,len(nums) - 1)  # firstly i reverse the the total nums
# function(0,len(nums) - k - 1) # reverse the first len(nums) - k elements and reverse next k + 1 to len(nums) elements
# function(k + 1,len(nums) - 1)
# print(nums) # this will help to get the final output


# Given a 4 x 4 square matrix

arr = [
[1, 2, 3, 4],
[5,6,7,8],
[9,0,1,4],
[5,2,3,9]
]

# Transpose of matrix
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
# print(arr)

# 90 deg rotation
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
#     arr[i] = arr[i][::-1]
# print(arr)

arr = [
[1, 2, 3, 4],
[5,6,7,8],
[9,0,1,4],
[5,2,3,9]
]

left = 0
right = len(arr) - 1

#used to pointer approach
# swapping arr[left] first values with the arr[right] last values
 
# while left < right:
#     for i in range(len(arr[0])):
#         arr[left][i],arr[right][~i] = arr[right][~i],arr[left][i]
#     left+=1
#     right-=1
# print(arr)


# anagram
s1 =  'students'
s2 =  'destntsu'

s1 = 'teams'
s2 = 'meat'

s1= 'apple'
s2 = 'leepa'

def anagram():
    seen = dict()
    for i in s1:
        seen[i] = seen.get(i,0)+1
        
    for j in s2:
        if j not in seen:
            return False
        seen[j] -= 1
        if seen[j] == 0:
            del seen[j]
    return not seen

# print(anagram())


# string of alphabets and digits
string = 'asw2edqsc4wdvrm21aawenejrg3e'

digits = 2
left = 0
maxi = 0
for right in range(len(string)):
    
    if string[right].isnumeric():
        digits-=1
    while digits < 0:
        if string[left].isnumeric():
            digits+=1
        left+=1
    maxi = max(maxi,right - left + 1)

print(maxi)
        
    
        
        
        
    

    


