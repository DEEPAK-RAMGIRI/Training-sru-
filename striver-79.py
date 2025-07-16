# Arrays:


# Q1: ❓❓❓ Next permutations ❓❓❓

from itertools import permutations
nums = [1,2,3]
nums = [3,2,1]
nums = [1,1,5]

# Time Complexity: O(n! * n)
# Space Complexity: O(n! * n)

arr = list(permutations(nums))
for i in range(len(arr)):
    if arr[i] == tuple(nums): break
# print(arr[i+1] if i + 1 < len(arr) else arr[0])


#Time Complexcity O(n)
#Space Complexcity O(1)

nums = [1,2,3]
nums = [3,2,1]
# nums = [1,1,5]
#because we of dictionary methid  

i = len(nums) - 2
while i >= 0 and nums[i + 1] < nums[i]:
    i-=1
j = len(nums) - 1
if i >= 0:
    while nums[j] < nums[i]:
        j-=1
    nums[j],nums[i] = nums[i],nums[j]
    print("hi")
nums[i+1:] = reversed(nums[i+1:])
# print(nums)



# Q2: ❓❓❓ 3 sum problem  ❓❓❓
nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]

#Time Complexcity O(n ^ 3)
#Space Complexcity O(m)

ans = set()
for i in range(len(nums) - 2):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if not nums[i] + nums[j] + nums[k]:
                ans.add(tuple(sorted([nums[i],nums[j],nums[k]])))
print(list(ans))



# Time complexcity O(n ^ 2)
#Space Complexcity O(m)
nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]
nums.sort()
ans = set()
for i in range(len(nums)):
    left = i + 1
    right = len(nums) - 1
    while left < right:
        if not nums[i] + nums[left] + nums[right]:
            ans.add(tuple(sorted([nums[i],nums[left],nums[right]])))
            left+=1
            right-=1
        elif nums[i] + nums[left] + nums[right] > 0:
            right-=1
        else: left+=1
# print(list(ans))


#  Q3: ❓❓❓ Maximum Subarray ❓❓❓ 
nums = [-2,1,-3,4,-1,2,1,-5,4] #6
nums = [1]# 1
nums = [5,4,-1,7,8] # 23

#Time Complexcity O(n ^ 3)
#Spaace Complexcity O(1 )
total = nums[0]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        maxi = 0
        for k in range(i,j+1):
            maxi += nums[k]
            total = max(total,maxi)
print(total)
            
        
#Time Complexcity O(n ^ 2)
#Space Complexcity O(1)
total = nums[0]
for i in range(len(nums)):
    maxi = 0
    for j in range(i,len(nums)):
        maxi += nums[j]
        total = max(maxi,total)
print(total)
        
        
#Time Complexcity O(n)
#Space Complexcity O(1)

maxi = total = nums[0]
for i in range(1,len(nums)):
    maxi = max(maxi+nums[i],nums[i])
    total = max(total,maxi)
print(total)



# Q4: ❓❓❓ Majority of element  ❓❓❓ 
nums = [3,2,3]
nums = [1]
nums = [1,2]


#Time Complexcity O(2 ^ n)
#Space Complexcity O(n)
from itertools import combinations
ans = []
for i in range(1,len(nums)+1):
    for subset in combinations(nums,i):
        for j in set(subset):
            if subset.count(j) >= len(nums)//3:
                ans.append(j)
print(ans)

#Time Complexcity O(n^2)
#Space Complexcity O(1) # at max we have two integers in the arr do n//3
#comparing each element in the list
ans = set()
for i in range(len(nums)):
    count = 0
    for j in range(i,len(nums)):
        if nums[i] == nums[j]:count+=1
    if count > len(nums)//3:ans.add(nums[i])
print(list(ans))

    
#Time Complexcity O(n^2)
#space Complexcity O(1)
ans = []
for i in set(nums):
    if nums.count(i) > len(nums)//3: ans.append(i)
print(ans)


#Time Complexcity O(n)
#Space Complexcity O(n)
dictionary = dict()
ans = set()
for i in nums:

    dictionary[i] = dictionary.get(i,0)+1
    if dictionary[i] > len(nums)//3: 
        ans.add(i)
# print(list(ans))
    
    
    
#Time Complexcity O(n)
#Space Complexcity O(1)
#so generally we have 2 candidiates so we are using two candidates

candidate1 = candidate2 = None
freq1 = freq2 = 0
for i in nums:
    if freq1 == 0 and i != candidate2:
        candidate1 = i
        freq1 = 1
    elif freq2 == 0 and i != candidate1:
        candidate2 = i
        freq2 = 1
    elif candidate1 == i:
        freq1+=1 
    elif candidate2 == i:
        freq2+=1
    else:
        freq1-=1
        freq2-=1
        
ans = []
freq1 = freq2 = 0 
for i in nums:
    if not candidate1 ^ i: freq1+=1 
    if candidate2 is not None and not candidate2 ^ i: freq2+=1  
if freq1 > len(nums)//3:ans.append(candidate1)
if freq2 > len(nums)//3:ans.append(candidate2)


# print(ans)


# ❓❓❓Count number of subarrays with given xor K❓❓❓
#Time Complexcity O(n^3)
#Space complexcity O(1)

k = 6
nums = [4,2,2,6,4]
count = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        maxi = 0
        for l in range(i,j+1):
            maxi ^= nums[l]
            if maxi == k: count+=1
# print(count)

#Time Complexcity O(n^2)
#space Complexcity O(1) 
count = 0
for i in range(len(nums)):
    maxi = 0
    for j in range(i,len(nums)):
        maxi ^= nums[j]
        if maxi == k:count+=1
# print(count)
            
            
#Time Complexcity O(n)
#Space Complexcity O(n) 
seen = {0:1}  
count = 0
total = 0     
for i in nums:
    total ^= i
    if total ^ k in seen:
        count+= seen[total ^ k]
    seen[total] = seen.get(total,0)+1
# print(count)


# ❓❓❓ Find the repeating and missing number❓❓❓
# Time Complexcity O(n^2)
# Space Complexcity O(1)

not_found = dup =  -1
nums= [4,3,6,2,1,1]


for i in range(1,len(nums)+1):
    n = nums.count(i)
    if n == 2: dup = i
    if n == 0:not_found = i
print(not_found,dup)


# Time Complexcity O(n) +O(n) ~ O(2n)
# Space Complexcity O(n)
nums= [4,3,6,2,1,1]
values = [0] * len(nums)
for i in nums:
    values[i-1]+=1
not_found = dup  = -1
for i in range(len(values)):
    if not values[i]: not_found =  i+1
    if values[i] == 2:dup = i + 1
if not_found == -1:
    not_found = len(nums)+1
print(dup,not_found)


# Time Complexcity O(n)
#Space Complexcity O(n)
nums= [4,3,6,2,1,1]
max_range = (len(nums) * (len(nums)+1)) >> 1
dup = 0
sets = set()
for i in nums:
    if i in sets:dup = i
    else: max_range -= i
    sets.add(i)
print(dup,max_range if max_range > 0 else len(nums)+1)
    
    
#Time Complexcity O(n)
#Space Complexcity O(1)

#idea is 
nums= [4,3,6,2,1,1]
Y = (len(nums) * (len(nums)+1)) >> 1 
Y_square = (len(nums) * (len(nums)+1) * (2*len(nums) + 1))//6
X = X_square = 0
for i in nums:
    X+=i
    X_square+=(i*i)
X_Y = X - Y
X2_Y2 = X_square - Y_square
XplusY= X2_Y2//X_Y
X = (XplusY + X_Y)//2
Y = X - X_Y 
# print(X,Y)
    
    
#Find the Xor
nums= [4,3,6,2,1,1]
xor = 0
for i in range(len(nums)):
    xor ^= nums[i]
    xor ^= i + 1
bit = 0
while True:
    if ((1 << bit) & xor) != 0: break
    bit+=1 

first_num = secound_num = 0 
for i in range(1,len(nums)+1):
    if not (i & (1 << bit)):
        first_num ^= i
    else:
        secound_num ^= i

for i in nums:
    if not (i & (1 << bit)): first_num ^= i
    else:secound_num ^= i
    
count = 0
for i in nums:
    if i == first_num: count+=1
if count == 2 :
    print(first_num,secound_num)
else:
    print(secound_num,first_num)
    


# ❓❓❓ count inversions❓❓❓


#Time Complexcity O(2 ^n)
#Space Complexcity O(n)
nums = [5,3,2,4,1]

def find(i,arr,count):
    if len(arr) == 2:
        return count+1
    if i == len(nums) :
        return count
    if not arr or  arr[-1] > nums[i]:
        count = find(i+1,arr + [nums[i]],count)
    count = find(i+1,arr,count)
    return count
print(find(0,[],0))


#Time Complexcity O(2^n)
#Space Complexcity O(1)

nums = [5,3,2,4,1]

def find(i,prev,length):
    count = 0
    if length == 2:
        return 1
    if len(nums) <= i:
        return count
    elif prev is None or prev > nums[i]:
        count += find(i+1,nums[i],length+1)
    count += find(i+1,prev,length)
    return count

print(find(0,None,0))
  
#Time Complexcity O(n^2)
#Space Complexcity O(1)
count = 0
arr = [5,3,2,4,1]
for i in range(len(arr) - 1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]: count+=1
# print(count)



#Time Complexcity O(n log n)
#Space Complexcity O(n)
#merge sort algorithm


nums = [5,3,2,4,1]

def conquer(nums,left,mid,right):
    count = 0
    output = []
    ind1 = left
    ind2 = mid + 1
    while ind1 <= mid and ind2 <= right:
        if nums[ind1] <= nums[ind2]:
            output.append(nums[ind1])
            ind1+=1
        else: 
            count += (mid - ind1 + 1)
            output.append(nums[ind2])
            ind2+=1
    if ind1 <= mid: output.extend(nums[ind1:mid+1]) 
    if ind2 <= right: output.extend(nums[ind2:right+1])
    for i in range(len(output)):
        nums[i+left] = output[i]
    return count
        
    

def divide(nums,left,right):
    count = 0
    if left < right:
        mid = left + ((right - left) >> 1)
        count += divide(nums,left,mid)
        count += divide(nums,mid+1,right)
        count += conquer(nums,left,mid,right)
    return count

print(divide(nums,0,len(nums)-1))

    
# ❓❓❓Maximum Product Subarray❓❓❓
#Time Complexcity O(n ^ 3)
#Space Complexcity O(1)
nums = [2,3,-2,4]
total = nums[0]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        maxi = 1
        for k in range(i,j+1):
            maxi *= nums[k]
            total = max(total,maxi)
print(total)
        
#Time Complexcity O(n ^2)
#Space Complexcty O(1)
nums = [2,3,-2,4]
total = nums[0]
for i in range(len(nums)):
    maxi = nums[i]
    for j in range(i+1,len(nums)):
        maxi = maxi*nums[j]
        total = max(total,maxi)
        
print(total)
 
# Time Complexcity O(n)
# Space Complexcity O(1)

nums = [2,3,-2,4]
 
preffix = suffix = 1
maxi = nums[0]  
for i in range(len(nums)):
    preffix *= nums[i]
    suffix *= nums[~i]
    if preffix == 0 : preffix = 1
    if suffix  == 0: suffix = 1
    maxi = max(maxi,preffix,suffix)
print(maxi)
 

# ❓❓❓  Search in Rotated Sorted Array II ❓❓❓

nums = [2,5,6,0,0,1,2] 
target = 0
# Time complexcity O(n)
#Space complexcity O(1)

for i in nums:
    if i == target: 
        print(True)
        break
    else: False
    
#Time Complexcity O(log n)
#Space Complexcity O(1)

left = 0 
right = len(nums) - 1

while left <= right:
    mid = left + ((right - left) >> 1)
    if nums[mid] == target: 
        print(True)
        break
    elif nums[left] == nums[mid] and nums[mid] == nums[right]:
        left+=1
        right-=1
    elif nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]: right = mid - 1
        else: left = mid + 1
    else:
        if nums[mid] < target <= nums[right]: left = mid + 1
        else: right=  mid - 1 
         
else: print(False)

# ❓❓❓ Find Minimum in Rotated Sorted Array❓❓❓

#Time Complexcity O(n log n)
#Space Complexcity O(1)
nums = [3,4,5,1,2]
nums.sort()
print(nums[0])
    
    
#Time Complexcity O(n)
#Space Complexcity O(1)

nums = [3,4,5,1,2]
print(min(nums))

# Time Complexcity O(n)
#Space Complexcity O(1)

nums = [3,4,5,1,2]
mini = float("inf")
for i in nums:
    if mini > i: mini = i
print(mini)

    
# Time Complexcity O(log n)
#Space complexcity O(1)

nums = [3,4,5,1,2]

left = 0
right = len(nums) - 1
while left <= right:
    mid = left + ((right - left) >> 1)
    if left + 1 == right:
        print(min(nums[left],nums[right]))
        break
    elif nums[left] < nums[mid] < nums[right]:
        left = mid
    else:
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid
else: print(nums[0])
 
 
 
#❓❓❓ Find Peak Element ❓❓❓
# Time COmplexcity O(n log n)
# Space Complexcity O(1)
nums = [1,2,3,1]
nums.sort()
print(nums[-1])

#Time Complexcity O(n)
# Space Complexcity O(1)

print(max(nums))

#Time Complexcity O(n)
#Space Complexcity O(1)

maxi = float("-inf")

for i in nums:
    maxi = max(maxi,i)
print(maxi)


#Time Complexcity O(log n)
#Soace Complexcity O(1) 

left = 0
right = len(nums) - 1
while left < right:
    mid = left + ((right - left) >> 1)
    if nums[mid] < nums[mid + 1]:
        left = mid + 1
    else: 
        right = mid
print(left)


#❓❓❓ koko Eating Banana ❓❓❓

#Time Complexcity O(n * m)
#Space Complexcity O(1)
piles = [3,6,7,11]
h = 8

maxi = sum(piles)
mini = 1
for i in range(mini,maxi+1):
    hours = 0
    for banana in piles:
        hours += banana// i if banana % i == 0 else (banana // i )+1
        if hours > h:
            break
    else: 
        print(i,"enough")
        break
    
    
#Time COmplexcity O(logn *m)
#space Complexcity O(1)

nums = [3,6,7,11]
ans = left = 1
right = sum(nums)
h = 8
def okay(hours):
    count = 0
    for i in nums:
        count += i//hours if not i%hours else (i//hours) + 1
    return count <= h

while left <= right:
    mid = left + ((right - left) >> 1)
    if okay(mid):
        ans = mid
        right=  mid - 1
    else:
        left = mid + 1
print(ans)
 
 
#❓❓❓ Aggressive Cows  ❓❓❓

#Time Complexcity O(n * max(nums))
#Space Comlexcity O(1)
arr = [0,3,4,7,10,9]
cows = 4

start = 1
end = arr[-1] - arr[0]
arr.sort()
for i in range(end,start-1,-1):
    prev = arr[0]
    count = 1
    for j in range(1,len(arr)):
        if arr[j] - prev >= i:
            prev = arr[j] 
            count+=1
    if count >= cows:
        print(i)
        break
    
    
# Time Complexcity O(n log max(nums))
#Space Complrxcity O(1)
nums = [0,3,4,7,10,9]
cows = 4

def count_cows(capacity):
    prev = arr[0]
    count = 1
    for i in range(1,len(nums)):
        if nums[i] - prev >= capacity:
            count+=1
            prev = nums[i]
    return count >= cows
        

nums.sort()
left = 1
right = nums[-1] - nums[0] 
while left <= right:
    mid = left + ((right - left) >> 1)
    if count_cows(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1 
print(ans)
        
    
# ❓❓❓ Allocate Books or Book Allocation❓❓❓
arr = [25,46,28,49,24]
students = 4

#Time Complexcity O( n * (sum(arr) - max(arr))) ~ O(n*m)
#Space Complexcity O(1)
start = max(arr)
end = sum(arr)
for i in range(start,end+1):
    count = 1
    bag = arr[0]
    for j in range(1,len(arr)):
        if bag + arr[j] > i:
            count+=1
            bag = arr[j]
        else: bag += arr[j]
    if count <= students:
        print(i)
        break
    
#Time Complexcity O(log n * (sum(arr) - max(arr))) ~ O(log n * m)
#Space Complexcity O(1)

nums = [25,46,28,49,24]
students = 4
left = max(nums)
right = sum(nums)
ans = -1

def find_all(capacity):
    count =1
    bag = nums[0]
    for i in range(1,len(nums)):
        if nums[i] + bag > capacity:
            count+=1
            bag = nums[i]
        else: bag += nums[i]
    return count <= students
    
while left < right:
    mid = left + (( right - left) >> 1)
    if find_all(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
    
# ❓❓❓ Median of Two Sorted Arrays ❓❓❓
#Time Complexcity O(m + n)
#Space Complexcity O(n + m)
nums1 = [1,3]
nums2 = [2]
i = 0 
j = 0
output = []
while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]: 
        output.append(nums1[i])
        i+=1
    else: 
        output.append(nums2[j])
        j+=1
        
if i < len(nums1):output.extend(nums1[i:])
if j < len(nums2):output.extend(nums2[j:])
median = (len(output)) >> 1

if len(output) & 1:
    print(output[median])
else:
    print((output[median] + output[median - 1])// 2)
        
        
# Linked lists

print("--------------------------------------- Linked lists ---------------------------------------")

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

def traveral(head):
    temp = head 
    while temp:
        print(temp.data,end=" ")
        temp = temp.next

def insert(head,arr):
    dummy = Node(arr[0])
    head = dummy
    for i in arr[1:]:
        dummy.next = Node(i)
        dummy = dummy.next  
    return head      
    
    
    
# ❓❓❓ Middle of the Linked List ❓❓❓

# Time Complexcity O(n) + O(n//2) ~ O(3n//2) ~ O(n)
# Space Complexcity O(1)

def find_middle1(head):
    count = 0
    temp = head
    while temp:
        count+=1
        temp = temp.next
    count = (count >> 1)
    
    temp = head
    while count:
        temp = temp.next
        count-=1
    return temp 


#Time Complexcity O(n) 
#Space Complexcity O(n)
def find_middle2(head):
    arr = []
    temp = head
    while temp:
        arr.append(temp.data)
        temp = temp.next
    mid = len(arr) >> 1
    print(arr[mid])
    
# Time Complexcity O(n) 
#Space Complexcity O(1)

def find_middle_optimal(head):
    fast,slow = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

arr = [1,2,3,4,5]
arr = [1,2,3,4,5,6]
head = None
# head = insert(head,arr)
# head = find_middle1(head)
# find_middle2(head)
# head = find_middle_optimal(head)
# traveral(head)

# ❓❓❓ Linked List Cycle ❓❓❓

# Time Complexcity O(n)
# Space Complexcity O(n)
 
def find_cycle(head):
    sets = set()
    while head:
        if head in sets:
            return True
        sets.add(head)
        head = head.next
    return False
     
     
# Time Complexcity O(n)
# Space Complexcity O(1)

def find_cycle_optimal(head):
    fast,slow = head,head
    while fast and fast.next:
        if fast == slow: return True
        fast = fast.next.next
        slow = slow.next
    return False


arr = [3,2,0,-4]
head = None
# head = insert(head,arr)
# print(find_cycle(head))


#❓❓❓ Remove Nth Node From End of List ❓❓❓


# Time Complexcity = O(n) + O(count - k)~ O(n) = O(2n) ~ O(n)
# Space Complexcity = O(1)  

def delete_k_node(head,k):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count+=1
    temp = head
    if count < k: return -1
    elif count-k == 0: return head.next
    else:
        count -= k+1
        while count:
            temp = temp.next
            count-=1
            
        temp.next = temp.next.next if temp.next else None
    return head
        
# Time Complexcity O(n)
#Space Complexcity O(1) 
def delete_k_node_optimal(head,k):
    fast = head
    for _ in range(k):
        fast = fast.next
    if not fast: return head.next 
    slow = head
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
        
    
    
        
        
arr = [1,2,3,4,5]
n = 2
head = None
# head = insert(head,arr)
# delete_k_node(head)


# ❓❓❓ Intersection of Two Linked Lists❓❓❓

# Time Complexcity O(m + n)
# Space Complexcity O(m) 
def intersection_point(headA,headB):
    seen =set()
    while headA:
        seen.add(headA)
        headA = headA.next
    while headB:
        if headB in seen:
            return headB
        seen.add(headB)
        headB = headB.next
        
        
#Time Complexcity O(m + n)
#Space Complexcity O(1)
    
def insertion_point_optimal(headA,headB):
    tempA,tempB = headA,headB
    while tempA !=  tempB:
        tempA =  headB if not tempA else tempA.next
        tempB = headA if not tempB else  tempB.next
    return tempA
        
        
        
# ❓❓❓ Sort LL ❓❓❓
#Time Complexcity O(n log n) + O(n) + O(n) ~ o(2n) + O(n log n) ~ O(n log n)
#Space Complexcity O(n) + O(n) ~ O(2n) ~ O(n)
head = [4,2,1,3]
def sort_linked_list(head):
    temp = head
    arr = []
    while temp:
        arr.append(temp.data)
        temp = temp.next
    arr.sort()
    dummy = Node(arr[0])
    head = dummy
    for i in arr[1:]:
        dummy.next = Node(i)
        dummy = dummy.next
    return head


#Time Complexcity O( n log n)
#Space complexcity O(1)
def sort_optimal_ll(left,right):
    temp = Node(0)
    dummy = temp
    while left and right:
        if left.data <= right.data:
            dummy.next = left
            left = left.next
        else:
            dummy.next = right
            right = right.next
        dummy = dummy.next 
        
    dummy.next = left if left else right
    return temp.next
        
    
def sort_linked_list_optimal(head):
    
    if  head and head.next:
        mid  = find_middle_optimal(head)
        fast = mid.next
        mid.next = None
        left = sort_linked_list_optimal(head)
        right = sort_linked_list_optimal(fast)
        return sort_optimal_ll(left,right)
    return head
        
      
# ❓❓❓ Odd Even Linked List ❓❓❓
        
        
#Time Complexcity O(n) + O(n) ~O(2n) ~O(n)
#Space Complexcity O(n) +O(n) ~ O(2n) ~ O(n)
def odd_even_ll(head):
    temp = head
    odd = []
    even = []
    count = 1
    while temp:
        if count & 1: odd.append(temp.data)
        else: even.append(temp.data)
        temp = temp.next
        count+=1
    
    odd.extend(even)
    dummy = Node(odd[0])
    temp = dummy
    for i in odd[1:]:
        temp.next = Node(i)
        temp = temp.next
    return dummy


# Time Complexcity O(n)
#Space Complexcity O(1)

def odd_even_ll_optimal(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    start = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = start
    
    return head

#❓❓❓ Backtracking && Recursion ❓❓❓ 
print('--------------------------------------- Backtracking && Recursion ---------------------------------------')
# Time Complexcity O(2^n * n) 
# Space complexcity O(2^n * n)

nums = [1,2,3]
ans = []

def find_subsets(index,arr):
    if len(nums) == index:
        ans.append(arr)
        return
    find_subsets(index+1,arr + [nums[index]]) 
    find_subsets(index+1,arr)
    
# find_subsets(0,[])
# print(ans)

#Time Complexcity O(2 ^n *n)
#Space Complexcity O(n)
nums = [1,2,3]
ans = []
for i in range(1<<len(nums)):
    arr = []
    for j in range(len(nums)):
        if i & (1 << j):
            arr.append(nums[j])
    ans.append(arr)
# print(ans)


# ❓❓❓ Combination Sum ❓❓❓ 

#Time Complexcity O(k^target * target log target)
#space complexcity O(K^target * target)

candidates = [2,3,6,7]
target = 7
ans = set()
from itertools import product
for i in range(1,target+1):
    for j in product(candidates,repeat=i):
        if sum(j) == target:
            ans.add(tuple(sorted(j)))
# print(ans)
            
            


# Time Complexcity O(2^n * n)
#Space Complexcity O(2^n * n)

candidates = [2,3,6,7]
target = 7
ans = []
def find_combinations(index,arr,sums):
    if sums < 0: return 
    if index == len(candidates):
        if sums == 0:
            ans.append(arr)
        return
    find_combinations(index,arr + [candidates[index]],sums - candidates[index])
    find_combinations(index+1,arr,sums)
# find_combinations(0,[],target)
# print(ans)

    
    
# ❓❓❓ N QUEENS❓❓❓
n = 4

#Time Complexcity O(n * n!)
#Space Complexcity O(n ^ 2)
def backtrack(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    ans = []
    
    def is_safe(row,col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        i,j = row-1,col-1
        while i >=0 and j >=0:
            if board[i][j] == 'Q':
                return False
            i-=1
            j-=1
        i,j = row-1,col+1
        while j < n and i >= 0:
            if board[i][j] == 'Q':
                return False
            i-=1
            j+=1
        return True
    
    def build(row):
        if row == n:
            ans.append([''.join(i) for i in board])
            return
        for col in range(n):
            if is_safe(row,col):
                board[row][col] = 'Q'
                build(row + 1)
                board[row][col] ='.'
            
    build(0)
    return ans


# print(backtrack(n))

n = 4
board = [ ['.' for _ in range(n)] for _ in range(n)]
ans = []
columns = set()
diag1 = set()
diag2 = set()
def backtrack(row):
    if row == n:
        ans.append([''.join(i) for i in board])
        return
    for cols in range(n):
        if cols in columns or row-cols in diag1 or row+cols in diag2:
            continue
        
        board[row][cols] = 'Q'
        columns.add(cols)
        diag1.add(row-cols)
        diag2.add(row+cols)
        backtrack(row+1)
        board[row][cols] = '.'
        columns.remove(cols)
        diag1.remove(row - cols)
        diag2.remove(row + cols)
backtrack(0)
print(ans)



#Time Complexcity O(9 ^ m)
#Space complexcity O(m)
from collections import defaultdict
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]



def find_value(row,col,value):
    for k in range(0,9):
        if board[row][k] == str(value):
            return False
        if board[k][col] == str(value):
            return False
        if board[3 *(row // 3) + k // 3][3 * (col // 3) + k % 3] == str(value):
            return False
    return True
            
        
def backtrack(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                for value in range(1,10):
                    if find_value(i,j,value):
                        board[i][j] = str(value)

                        if backtrack(board): return True
                        else: board[i][j] = '.'
                return False
    return True

# backtrack(board)


# Optimised Version
from collections import defaultdict

rows = defaultdict(set)
cols = defaultdict(set)
boxs = defaultdict(set)

for i in range(9):
    for j in range(9):
        if board[i][j] != '.':
            value = str(board[i][j])
            rows[i].add(value)
            cols[j].add(value)
            boxs[(i // 3 ,j//3)].add(value)
            
            
def backtrack():
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for value in range(1,10):
                    value = str(value)
                    if value not in rows[i] and value not in cols[j] and value not in boxs[(i//3,j//3)]:
                        board[i][j] = value
                        rows[i].add(value)
                        cols[j].add(value)
                        boxs[(i//3,j//3)].add(value)
                        
                        if backtrack(): return True
                        
                        board[i][j] = '.'
                        rows[i].remove(value)
                        cols[j].remove(value)
                        boxs[(i//3,j//3)].remove(value)
                return False
    return True
backtrack()
print(board)
                        
                    


    
               



    


