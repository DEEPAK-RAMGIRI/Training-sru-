#search insert position
#Time Complexcity O(n)
#Space Complexcity O(1)
nums = [1,3,5,6]
target = 5
for i in range(len(nums)):
    if nums[i] >= target:
        # print(i)
        break
    
#using binary search
#Time Complexcity O(log n)
#Space Complexcity O(1)
nums = [1,3,5,6]
target = 5
left = 0
right = len(nums) - 1
while left < right:
    mid = left + ((right - left) >> 1)
    if nums[mid] == target: 
        # print(mid)    
        break
    elif nums[mid] < target:
        left = mid + 1
    else: right = mid - 1
else:   
    print(left)
        
        
#printing first and last occurence
nums = [5,7,7,8,8,10]
target = 8
#Brute Force Approach
#Time Complexcity O(n)
#Space Complexcity O(1)
index1 = index2 = -1
for i in range(len(nums)):
    if target == nums[i]:
        index1 = index2 = i
        break
    
for i in range(index1+1,len(nums)):
    if target == nums[i]:
        index2 = i
# print(f'first occurenece {index1} and last occurenece {index2}')


#Time Complexcity O(n)
#Space Complexcity O(1)
nums = [5,7,7,8,8,10]
target = 8
first =  last = -1
for i in range(len(nums)):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
# print(first,last)


#Time Complexcity O(log n + log n) ~ O(log n)
#Space Complexcity O(1)
nums = [5,7,7,8,8,10]
target = 8
left = 0
right = len(nums) - 1
first = last = -1
def find_first_and_last_occurenece(nums,i,j):
    left = i
    right = j
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] < target: left = mid + 1
        else: right = mid - 1
    lefty = left
        
    left = i
    right = j
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] <= target: left = mid + 1
        else: right = mid - 1
    righty = right
    
    return lefty,righty

left,right = find_first_and_last_occurenece(nums,0,len(nums) - 1)
if left <= right and nums[left] == target  and nums[right] == target:
    print([left,right])
else:[-1,-1]

#Search in Rotated Sorted Array
nums = [4,5,6,7,0,1,2]
target = 0

#Time  Complexcity O(n)
#Space Complexcity O(1)
for i in range(len(nums)):
    if target == nums[i]:
        print(i)
        break
    
# Time Complexcity O(n)
#Space Complexcity O(1)
nums = [4,5,6,7,0,1,2]
target = 0 
# print("using builtin",nums.index(target))
    
#Time Complexcity O(log n)
#Space Complexcity O(1)

nums = [4,5,6,7,0,1,2]
target = 0

left = 0
right = len(nums) - 1

while left <= right:
    mid = left + ((right - left) >> 1)
    if nums[mid] == target:
        print(mid)
        break
    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[right]:
            right = mid - 1
        else: left  = mid + 1
    else:
        if nums[left] < target <= nums[right]:
            left = mid + 1
        else: right = mid - 1
else:print(-1)
    

