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
        print(mid)
        break
    elif arr[left] < arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid -1
else:
    if arr[0] < arr[-1]:
        print(0)
    else:
        print(len(arr)-1)
        
#more optimised version use this
left = 0
right = len(arr) - 1
while left < right:
    mid = left + ((right - left) >> 1)
    if arr[mid] > arr[right]:
        left = mid + 1
    else:
        right = mid
print(left)
    
