# brute force approach
# Single Number
nums = [4,1,2,1,2]
n = len(nums)
# Time Complexity O(n^2)
#Space Complexcity O(1)
for i in range(n):
    count = 0
    for j in range(i+1,n):
        if nums[i] == nums[j]:
            count += 1
    if count == 0: 
    #    print(nums[i])
       break
   
   
#Time Complexcity O(n log n)
#Space Complexcity O(1)
nums = [2,2,1]
# nums = [2,2,3,3,4,4,5]
nums.sort()
for i in range(0,len(nums)-1,2):
    if nums[i] != nums[i+1]:
        # print(nums[i])
        break
# else: print(nums[-1]) 
   
# Time Complexcity O(n)
#Space Complexcity O(n)
#using hash map
maps = dict()
for i in nums:
    maps[i] = maps.get(i,0)+1
    
for i in maps:
    if maps[i] == 1:
        # print(i)
        break
# print(i for i in maps if maps[i] == 1)


#Time Complexcity O(n)
#Space Complexcity O(1)
xors = 0
for i in nums:
    xors ^= i
# print(xors)


#Sort Color
#Time Complexcity O(n)
#Space Complezxcity O(1)
nums = [2,0,2,1,1,0]
ans = [0] * 3
for i in nums: 
    ans[i]+=1
    
j = 0
for i in range(3):
    while ans[i] != 0:
        nums[j] = i
        ans[i]-=1
        j+=1
# print(nums)


#Time ComplexcityO(n)
#Space Complexcity O(1)
nums = [2,0,2,1,1,0]
count_0 = 0
count_1 = 0
count_2 = 0
for i in nums: 
    if not i: count_0+=1
    elif i == 1: count_1 +=1
    else:count_2+=1    
j = 0
for _ in range(count_0):
    nums[j] = 0
    j+=1
for _ in range(count_1):
    nums[j] = 1
    j+=1
for _ in range(count_2):
    nums[j] = 2
    j+=1
# print(nums)


#Dutch national flag algo
#Time Complexcity O(n)
#Space Complexcity O(1)

nums = [2,0,2,1,1,0]
low = mid = 0
high =len(nums)-1
while mid <= high:
    if nums[mid] == 0:
        nums[low],nums[mid] = nums[mid],nums[low]
        low+=1
        mid+=1
    elif nums[mid] == 2:
        nums[high],nums[mid] = nums[mid],nums[high]
        high-=1
        mid+=1
    else:
        mid+=1
# print(nums)
        
         
# Majority Element
#Brute Force  Time Complexcity O(n^2)
#Space Complexcity O(1)
nums = [3,2,3]
n = len(nums)//2
for i in range(len(nums)):
    count = 1
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]: 
            count+=1
    if count > n:
        print(nums[i])
        break
else:print(-1)
        
 
#Time Complexcity O(n^2)
#Space Complexcity O(1)
for i in set(nums):
    if nums.count(i) > n:
        print(i)
        break
    
    
#Use hashmap
#Time Complexcity O(n)
#Space Complexcity O(1)
freq = dict()
for i in nums:
    freq[i] = freq.get(i,0)+1
    if freq[i] > n:
        print(i)
        break
else: print(-1)

#Sortit and find the element
#Time Complexcity O(n log n)
#Space Complexcity O(1)
nums.sort()
print(nums[n+1])
    
 
# Moore's algorithm
freq = 0
for i in nums:
    if not freq: ans = i
    elif ans == i: freq+=1
    else: freq-=1
print(ans)
    