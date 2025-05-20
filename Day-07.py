# we have two sorted list which are [2,4,5,8,9] [3,5,6,9,11,12,13]
#merge it and form a sorted array
arr1 = [2,4,5,8,9] 
arr2 = [3,5,6,9,11,12,13]
left = 0
ans = []
right = 0
while left < len(arr1) and right < len(arr2):
    if arr1[left] < arr2[right]:
        ans.append(arr1[left])
        left+=1
    else:
        ans.append(arr2[right])
        right+=1
ans.extend(arr1[left:] if left < len(arr1) else arr2[right:])
# print(ans)


#merge sort algorithm
#time complexcity O(n log(n))
def conquer(arr,left,mid,right):
    ind1 = left
    ind2 = mid+1
    merged = []
    while ind1 <= mid and ind2 <= right:
        if arr[ind1] < arr[ind2]:
            merged.append(arr[ind1])
            ind1+=1
        else:
            merged.append(arr[ind2])
            ind2+=1
    merged.extend(arr[ind1:mid+1]) 
    merged.extend(arr[ind2:right+1])
    for i in range(len(merged)):
        arr[left+i] = merged[i]
            
arr = [11,2,5,7,8,11,12,12]
def divide(arr,left,right):
    if left < right:
        mid = left + (right - left) // 2
        divide(arr,left,mid)
        divide(arr,mid+1,right)
        conquer(arr,left,mid,right)
    return
divide(arr,0,len(arr)-1)
# print(arr)


#given an unsorted array which may have dup print kth largest element 
#optimised version(here iam using heapq)
    
import heapq

def findkth(arr,k):
    queue = []
    for i in set(arr):
        heapq.heappush(queue,i)
        if len(queue) > k:
            heapq.heappop(queue)
    return queue[0]

arr = [2,13,4,2,9,9,5,8,7,13,3]
k = 3
# print(findkth(arr, k))

#using bucket sort method (here i just used frequency of count to print kth largest element)
count = [0]* (max(arr) + 1)
for i in arr:
    count[i] = 1
# print(count)
for i in range(len(count)-1,-1,-1):
    if count[i] == 1:
        k-=1
        if k == 0:
            # print(i)
            break


#given array with duplicates with high freq

arr1 =[1,2,10,11,3,4,2,2,2,2,2,4,4,4,2,2,1,4,5,6,8,9,6,2,3]
count = [0] * (max(arr1) + 1)
max_frequency = [-1,-1]

for i in arr1:
    count[i] += 1
    if count[i] > max_frequency[-1]:
        max_frequency[0] = i
        max_frequency[-1] = count[i]
# print(max_frequency)
# print(count)
    
# kth largest freq
# finding the kth largest frequency
k = 2
kth_frequency = [0] * (max(count) + 1)
for i in count:
    kth_frequency[i] = 1
for i in range(len(kth_frequency)-1,-1,-1):
    if kth_frequency[i] == 1:
        k-=1
        if k == 0:
            # print(i)
            break
#method 2 printing max frequency in the array      
from collections import Counter     
arr1 =[1,2,10,11,3,4,2,2,2,2,2,4,4,4,2,2,1,4,5,6,8,9,6,2,3]
counter = Counter(arr1)
# print(max(counter.values()))
k=3
# printing kth frequency in array
counter = sorted(counter.items(),key = lambda x:(x[1],x[0]))
# print(counter)
# print(counter[-k])




# find the no whos is frequency is greater the n//2
#or majority of elements
#method 01
nums = [2,1,1,2,3,1,1]
for i in set(nums):
    if nums.count(i) >= len(nums)//2:
        # print(i)
        break
        
#method 02
n=len(nums)
freq=1
ans= nums[0]
nums.sort()
for i in range(n):
    if nums[i] == nums[i-1]:
        freq+=1
    else:
        freq=1
    ans = nums[i]
    # if n//2 < freq: 
        
        # print(ans)
        

    
#method 03
frequency = dict()
for i in nums:
    frequency[i] = frequency.get(i,0)+1
for i in set(nums):
    if frequency[i] > len(nums)//2:
        # print(i)
        break
    
#method 04 Moose voting algorithm
nums = [2,1,1,2,3,1,1]
nums = [3,3,3,2,2,4,4,3]
res = nums[0]
count = 1
for i in range(1,len(nums)):
    if count == 0:
        res = nums[i]
    if res == nums[i]:
        count+=1
    else:
        count-=1
# print(res)

#printing last occurence of value in the array:
#method 01
arr1 = [2,4,3,1,4,2,3,4,5]
first = last = -1
key = 4
for i in range(len(arr1)):
    if arr1[i] == key:
        if first == -1:
            first = last = i
        else:
            last = i
# print(first,last)

#method 2
last = -1
for i in range(len(arr1)):
    if key == arr1[i]: last = i
# print(last)

# #method 3
# last =-1
# for i in range(len(arr1)-1,-1,-1):
#     if arr1[i] ==key: 
#         # print(i)
#         break
 
 
 
 #code for binary search
key = 7
arr = [2,3,5,6,7,7,7,7,78,9,10,10,10,13,15] 
left = 0
right = len(arr) - 1

#method 01
# i have doubt in this one:)
while left < right:
    mid = left + ((right - left) >> 1)
    if arr[mid] == key:
        while arr[mid] == key:
            mid+=1
        break
    elif arr[mid] <= key:
        left = mid+1
    else:
        right = mid-1
# print(mid-1)

#method 02

last = -1
while left < right:
    mid = left + ((right - left) >> 1)
    if arr[mid] == key:
        last = mid
        left = mid+1
    elif arr[mid] < key:
        left = mid + 1
    else:
        right = mid - 1
# print(last)

# check element present in array if present return it's index else return its correct possition
#method 01
arr1 = [2,4,6,7,8,10,13,15]
key = 3
for i in range(len(arr1)):
    if key == arr1[i]:
        print("found at",i)
        break
    elif arr1[i] > key:
        print("Here it should be added: ",i)
        break
    
#method 02
left = 0
right = len(arr1) - 1
while left < right:
    mid  = left + ((right - left) >> 1)
    if arr[left] == arr[right]:
        break
    elif arr[mid] < key:
        left = mid+1
    else:
        right = mid -1
print(mid)
        
        
        
        
    
     
    

        
    
                


       
        

    
    
