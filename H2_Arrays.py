#Linear search
#Time Complexcity o(n)
#Space Complexcity O(1)
key = 10
arr = [1,2,3,4,5,6,7,8,9,10,12,1,2,11]
for i in arr:
    if i == key:
        # print("found")
        break
# else: print("not found")

#largest elements
#Time Complexcity O(n)
#Space Complexcity O(1)
maxi = float('-inf')
for i in arr:
    if i > maxi: maxi = i
# print(maxi)

# print(max(arr))


#Secound largest element
# using bubble sort
#Time Complexcity O(n)
#Space Complexcity O(1)
k = 2
for i in range(k):
    flag = False
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr[-k])


arr = [1,2,3,4,5,6,7,8,9,10,12,1,2,11]
first = secound = -1
for i in arr:
    if first < i:
       secound = first
       first = i
    elif i < first and secound < i:
        secound = i

# print(secound)

#maximum number of consecutive 1's in the array.
nums = [1,1,0,1,1,1]
count= 0 
maxi  = 0
for i in nums:
    count = count+1 if i else 0
    maxi = max(count,maxi)
# print(maxi)
    
    

# Left Rotate Array by One
nums = [1,2,3,4,5,6,7]
nums.append(nums.pop(0))
print(nums)


# Left Rotate Array by k
#Time Complexcity O(1)
#Space Complexcity O(n)
from collections import deque
nums = [1,2,3,4,6,7]
k = 2
queue = deque(nums)

for _ in range(k):
    queue.append(queue.popleft())
# print(queue)


#Move zeros to end
count = 0
ans = []
nums = [0,1,0,3,12]
for i in nums:
    if i: ans.append(i)
    else: count+=1
ans.extend([0 for _ in range(count)])
print(ans)
     
    
             
        

