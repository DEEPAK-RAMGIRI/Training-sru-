# find the floor value of no
n = 54
left = 0
right = n//2
while left <=  right:
    mid = left + ((right - left) >> 1)
    square = mid * mid 
    if n == square:
        print(mid)
        break
    elif square <= n:
        left = mid + 1
    else:
        right = mid - 1
        
# print(left-1)



# given a rotated array
arr = [15,18,20,22,2,5,8,10,12,13]
# arr = [2,5,8,10,12,13,15,18,20,22]
# arr = [5,8,10,12,13,15,18,20,22,2]
arr = [2,3,4,5,6,7,8,9,1]  # Rotation at index 8


n = len(arr)
left = 1
right = len(arr) - 2
while left < right:
    mid = left + ((right - left) >> 1)
    if  arr[mid-1]  > arr[mid] < arr[mid+1]:
        # print(mid)
        break
    elif arr[left] < arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid -1
# else:
#     if arr[0] < arr[-1]:
#         # print(0)
#     else:
#         print(len(arr)-1)
        
# more optimised version use this
#Time Complexcity O(log n)
#Space Complexcity O(1)
arr=[1,2,3,4,5,6,7,8,9,10]
left = 0
right = len(arr) - 1
while left < right:
    mid = left + ((right - left) >> 1)
    if arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid
# print(left)

#paek element
arr = [2,3,4,6,3,2,1,5,8,10,1,4,2]
arr=[1,2,3,4,5,6,7,8,9,10]

ans = []
for i in range(1,len(arr)-1):
    if arr[i-1] < arr[i] > arr[i+1]:
        ans.append(arr[i])
# print(ans)


# we need to find only one  peak values from the arr
left = 0
right = len(arr)-1
while left < right:
    mid = left + ((right - left) >> 1)
    if arr[mid] < arr[right]:
        left = mid + 1
    else:
        right = mid
# print(arr[left])



# koko eating banana
def trueorfalse(piles,mid,h):
        count = 1
        for i in piles:
            count += i// mid if i % mid == 0 else (i// mid) + 1
            if count > h:
                return False
        return True
def minEatingSpeed(piles, h):
    left = 1 
    right = max(piles)
    while left <= right:
        mid  = left+ ((right - left) >> 1)
        if trueorfalse(piles,mid,h):
            right = mid -1
        else:
            left = mid + 1
    return left
arr = [3,6,7,11] 
h = 8
# print(minEatingSpeed(arr,h))
    
    
#Aggressive cows problem
def trueorfalse(arr,mid,cows):
    previous = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if arr[i] - previous >= mid:
            count+=1
            previous = arr[i]
    return count >= cows
        
def usinglinear(arr,cows):
    start = arr[0]
    last = arr[-1]
    for i in range(start,last):
        if not trueorfalse(arr,i,cows):
            print(i-1)
            break

# def agressivecows(arr,cows):
#     left = min(arr)
#     right = max(arr)
#     res = -1
#     while left <= right:
#         mid = left + ((right - left) >> 1)
#         if trueorfalse(arr,mid,cows):
#             res = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(res)
        
    
arr = [1, 2, 4, 8, 9] 
cows = 5
usinglinear(arr,cows)
# agressivecows(arr,cows)
