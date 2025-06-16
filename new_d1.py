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
        # print(nums[i])
        break
# else:print(-1)
        
 
#Time Complexcity O(n^2)
#Space Complexcity O(1)
for i in set(nums):
    if nums.count(i) > n:
        # print(i)
        break
    
    
#Use hashmap
#Time Complexcity O(n)
#Space Complexcity O(n)
freq = dict()
for i in nums:
    freq[i] = freq.get(i,0)+1
    if freq[i] > n:
        # print(i)
        break
# else: print(-1)

#Sortit and find the element
#Time Complexcity O(n log n)
#Space Complexcity O(1)
nums.sort()
# print(nums[n+1])
    
 
# Boyer's Moore algorithm
# Time Complexcity O(n)
# Space Complexcity O(1)
freq = 0
for i in nums:
    if not freq: ans = i
    elif ans == i: freq+=1
    else: freq-=1
# print(ans)
    
    
#maximum subarray

#Time Complexcity O(n^3)
#Space Complexcity O(1)
maxi = 0
nums = [-2,1,-3,4,-1,2,1,-5,4]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        count = 0
        for k in range(i,j+1):
            count+=nums[k]
        maxi = max(maxi,count)
# print(maxi)

# ---- or ----

maxi = 0
nums = [-2,1,-3,4,-1,2,1,-5,4]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        count = sum(nums[i:j])
        maxi = max(maxi,count)
print(maxi)

#Time Complexcty O(n^2)
#Space Complexcity O(1)
maxi = 0
nums = [-2,1,-3,4,-1,2,1,-5,4]
for i in range(len(nums)):
    sums = 0
    for j in range(i,len(nums)):
        sums += nums[j]
        maxi = max(maxi,sums)
# print(maxi)
   
#Kadane algorithm
#Time Complexcity O(n)
#Space Complexcity O(1)
ans = maxi = nums[0]
nums = [-2,1,-3,4,-1,2,1,-5,4]
for i in range(len(nums)):
    maxi = max(nums[i],maxi+nums[i])
    ans = max(ans,maxi)
# print(ans)



#printing the maximum subarray
nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = maxi = nums[0]
for i in range(i+1,len(nums)):
    if maxi + nums[i] < nums[i]:
        ind1 = i 
    if ans > maxi:
        pass
        

# print(ans)


#Rotate matrix by 90 deg

mat = [[1,2,3],[4,5,6],[7,8,9]]

temp = [ [0 for  _ in range(len(mat[0]))] for _ in range(len(mat))]


new_mat = [[0 for _ in range(len(mat))] for _ in range(len(mat))]
n = len(mat)
for i in range(len(mat)):
    for j in range(len(mat)):
        new_mat[i][j] = mat[j][i]

for i in range(len(new_mat)):
    for j in range(len(new_mat)):
        mat[i][n-j-1] = new_mat[i][j]
        
# print(mat)
        

#Time Complexcity O(n*m)
#Space Complexcity O(1) 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(i,len(matrix[0])):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for i in matrix:
    i.reverse()      
# print(matrix)
    
    
#find the duplicate in array
#Time Complexcity O(n^2)
#Space Complexcity O(1)
nums = [4,3,2,7,8,2,3,1]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            # print("ans",nums[i])
            break
        
# Time Complexcity O(n)
#Space Complexcity O(n) 
count = [0]* (max(nums) + 1)
for i in range(len(nums)):
    if count[nums[i]]+1 == 2:
        # print(count[nums[i]])
        break
    count[nums[i]]+=1   

nums = [4,3,2,7,8,2,3,1]

#Time Complexcity O(n log n)
#Space Complexcity O(1)
nums.sort()
for i in range(len(nums)-1):
    if nums[i] ==nums[i+1]:
        # print(nums[i])
        break
  

#Bouns
nums = [1,2,3,4,5,6,6]
def function(mid):
    count = 0
    for i in nums:
        if i <= mid:
            count+=1
    return count <= mid

left = min(nums)
right = max(nums)
while left < right:
    mid = left + ((right - left) >> 1)
    if function(mid):
        left = mid +1
    else:
        right = mid-1   
print(right)


#merge sort
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
i = j = 0
temp = []
while i < len(nums1) and j < len(nums2):
    
    if nums1[i] < nums2[j]:
        temp.append(nums1[i])
        i+=1
    else:
        temp.append(nums2[j])
        j+=1
    while i < len(nums1) and not nums1[i]:i+=1
    while  j < len(nums2) and not nums2[j]:j+=1 
temp.extend(nums1[i:] if i < len(nums1) else nums2[j:])
print(temp)
    
        
    
    
    
        

    
    
    



        

        


