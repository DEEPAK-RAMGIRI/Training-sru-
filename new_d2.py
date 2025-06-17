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
# if left <= right and nums[left] == target  and nums[right] == target:
#     print([left,right])
    
# else:print([-1,-1])

#Search in Rotated Sorted Array
nums = [4,5,6,7,0,1,2]
target = 0

#Time  Complexcity O(n)
#Space Complexcity O(1)
for i in range(len(nums)):
    if target == nums[i]:
        # print(i)
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
        # print(mid)
        break
    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else: left  = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else: right = mid - 1
# else:print(-1)
    
#Capacity to ship packages within D days
#Time Complexcity O(max(weights),sum(weights)) * n)
#Space Complexcity O(1)
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
res =-1
for we in range(max(weights),sum(weights)+1):
    total = 0
    day = 1
    flag = True
    for i in weights:
        if total+i > we:
            total = i
            day+=1
        else:
            total+= i
    if day <= days:
        res = we
        break
# print(res)




#Optimal approach
#Time Complexcity O(n logn)
#Space Complexcity O(1)
        
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
weights = [3,2,2,4,1,4]
days = 3
weights = [1,2,3,1,1]
days = 4

def function1(mid,days):
    day = 1
    maxi = 0
    for i in weights:
        if i+maxi > mid:
            day+=1
            maxi = i
        else:
            maxi += i
    return day <= days
left = 0
right = sum (weights)
while left <= right:
    mid = left + ((right - left) >> 1)
    if function1(mid,days):
        right = mid -1
    else:
        left = mid +1
# print(left)



#Find the peak element
nums = [1,2,3,1]
maxi = nums[0]
for i in range(1,len(nums)-1):
    if nums[i-1] < nums[i] > nums[i+1]:    
        print(i)
        break
left = 0
right =len(nums) - 1
while left < right:
    mid = left + ((right - left) >> 1)
    if nums[mid] > nums[mid + 1]:
        right = mid
    else:
        left= mid + 1
        
print(left)
        


