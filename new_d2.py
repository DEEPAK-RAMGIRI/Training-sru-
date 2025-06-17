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
#Time Complexcity O(n)
#Space Complexcity O(1)
nums = [1,2,3,1]
maxi = nums[0]
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:    
        print(i)
        break
else: len(nums) -1

#Time Complexcity O(log n)
#Space Complexcity O(1)
nums = [1,2,3,1]
left = 0
right =len(nums) - 1
while left < right:
    mid = left + ((right - left) >> 1)
    if nums[mid] > nums[mid + 1]:
        right = mid
    else:
        left= mid + 1
        
# print(left)
    
#search element in rotated array 2

#Time Complexcity O(n)
#Space Complexcity O(1)
nums = [2,5,6,0,0,1,2]
target = 100

left = 0
right = len(nums) - 1
while left <= right:
    mid = left + ((right - left) >> 1) 
    if nums[mid] ==  target:
        # print(True) 
        break 
    while left < mid and nums[left] == nums[mid]: left += 1
    while mid < right and nums[right] == nums [mid]: right -= 1
    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:  left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else: right = mid - 1
# else:print("Not found")
    
#Time Complexcity O(n)
#Space Complexcity O(1)  
left = 0
right = len(nums) - 1
while left <= right:
    mid = left + ((right - left) >> 1)
    if nums[mid] == target: 
        # print(True)
        break
    elif nums[mid] == nums[left] and nums[mid] == nums[right]: 
        left +=1
        right -=1
    elif nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right=  mid - 1
        else:
                left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
# print(False)


#Search element in the 2d matrix
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

#Brute Force O(m *n)
# if m = n then O(n^2)
flag = True
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            # print("found")
            flag = False
            break
    if not flag: break
# else: print("not found") 


# using Binary search
#Time Complexcity O(m log n)
#Space Complexcity O(1)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
flag = True
for i in matrix:
    left = 0
    right = len(i) - 1
    if i[left] <= target <= i[right]: 
        while left <= right:
            mid = left + ((right - left) >> 1)
            if i[mid] == target: 
                # print("found")
                flag = False
                break
            elif i[mid] < target: left = mid + 1
            else: right = mid - 1
        if not flag: break
# else: print("not Found")

# Time Complexcity O(m+log n)
# Space Complexcity O(1)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
flag = True
for i in matrix:
    if i[0] <= target <= i[-1]: 
        arr = i
i =arr 
while left <= right:
    mid = left + ((right - left) >> 1)
    if i[mid] == target: 
        print("found")
        break
    elif i[mid] < target: left = mid + 1
    else: right = mid - 1
else: print("not Found")


#Time Complexcity O(log m + log n)
#Space Complexcity O(1)
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#Don't use below code
# left = 0
# right = len(matrix) - 1
# while left < right:
#     mid = left + ((right - left ) >> 1)
#     if matrix[mid][-1] < target: left = mid + 1
#     else: right = mid - 1
# arr = matrix[left]
# left = 0
# right = len(arr) - 1
# while left < right:
#     mid = left + ((right - left) >> 1)
#     if arr[mid] == target:
#         print("found")
#         break
#     elif arr[mid] < target: left = mid + 1
#     else: right = mid - 1
# else: print("not Found")



#Time Complexcity O(log(m * n))
#Space Complexcity O(1)
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
key = 3
n = len(matrix)
m = len(matrix[0])
left = 0
right = n * m - 1

found = False
while left <= right:
    mid = left + ((right - left) >> 1)
    row = mid // m
    col = mid % m
    if matrix[row][col] == key:
        # print("Found at position:", (row, col))
        found = True
        break
    elif key < matrix[row][col]:
        right = mid - 1
    else:
        left = mid + 1

if not found:
    print("Not found")


# Minimum Number of Days to Make m Bouquets
#Time Complexcity O(max(bloomDay) * n)
#Space Complexcity O(1)
bloomDay = [1,10,3,10,2]
m = 3
k = 1

def function1(mid,k,m,bloomday):
    count= 0 
    bou = 0
    for i in bloomDay:
        if i <= mid:
            count+=1
        else:
            bou += count//k
            count = 0
    bou += count//k
    return bou >= m 

left = min(bloomDay)
right = max(bloomDay)

for i in range(left,right + 1):
    
    if function1(i,k,m,bloomDay):
        res = i
        break
print(res)
    
#Time Complexcity O(n log n)
#Space Complexcity O(1)
def function1(mid,k,m,bloomday):
    count= 0 
    bou = 0
    for i in bloomDay:
        if i <= mid:
            count+=1
        else:
            bou += count//k
            count = 0
    bou += count//k
    return bou >= m 
    
    
bloomDay = [1,10,3,10,2]
m = 3
k = 1
left = min(bloomDay)
right = max(bloomDay)

if m * n < len(bloomDay):
    print(-1)
else:
    value = -1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if function1(mid,k,m,bloomDay):
            value = mid
            right = mid - 1
        else:
            left =  mid + 1
# print(mid)


print("Completed")
#Exam Question

# Q1
#reverse the linked list
## Q2
#print the linked list with values less than average of arr

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.size = 0
        self.sums = 0
        self.head = None
        
    def insert(self,data):
        self.sums += data
        node = Node(data)
        self.size+=1
        
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
    
    def reverse(self):
        temp,prev = self.head,None
        while temp:
            nextnode,temp.next = temp.next,prev
            prev,temp = temp,nextnode
        self.head = prev
        
    def printing(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            
            
    def linked_list_with_less_than_avg_values(self):
        avg = self.sums / self.size
        while self.head and self.head.data > avg:
            self.head = self.head.next
        curr = self.head
        while curr and curr.next:
            if curr.next.data > avg: curr.next = curr.next.next
            else:curr = curr.next
            
arr = [1,2,3,4,5,6,7,8,10,9] 
ll= Linkedlist()
for i in arr:
    ll.insert(i)
# ll.printing()
#Q1 ans
# ll.reverse()
# ll.printing()

#q2
ll.linked_list_with_less_than_avg_values()
ll.printing()