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
# print(arr[-k])


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
#Time Complexcity O(n)
#Space Complexcity O(n)

count = 0
ans = []
nums = [0,1,0,3,12]
for i in nums:
    if i: ans.append(i)
    else: count+=1
ans.extend([0 for _ in range(count)])
# print(ans)
     
     
#Time Complexcity O(n)
#Space Complexcity O(1)
nums = [0,1,0,3,12]
left = 0 
for right in range(1,len(nums)):
    if nums[left]!= 0:
        left = right
    if nums[right]:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        
# Remove duplicates from the array
arr = [0,0,1,1,1,2,2,3,3,4]
sets = set()
for i in arr:
    sets.add(i)


#Missing number nos start from [0,n]
nums = [3,0,1]
maxi = max(nums)
total = (maxi * (maxi + 1)) >> 1
print(total - sum(nums)) 


#Union of two sorted arrays
arr1=[1,2,3,4,5,6,7,78]
arr2=[2,3,6,10,13,23,45]
ans = []

i = j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        ans.append(arr1[i])
        i+=1
        j+=1
    elif arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i+=1
    else:
        
        ans.append(arr2[j])
        j+=1
# print(ans)
    
    
#Leaders in array
arr = [16, 17, 4, 3, 5, 2]
stack = [arr[-1]]
for i in arr[::-1]:
    if i > stack[-1]:
        stack.append(i)
# print(stack)

#print spiral matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rowend = len(matrix)
colend = len(matrix[0])
rowstart = colstart = 0
while rowstart < rowend and colstart < colend:
    for col in range(colstart,colend):
        print(matrix[rowstart][col],end=" ")
    rowstart+=1
    for row in range(rowstart,rowend):
        print(matrix[row][colend-1],end=" ")
    colend-=1
    if rowstart < rowend:
        for col in range(colend-1,colstart-1,-1):
            print(matrix[rowend-1][col],end=" ")
        rowend-=1
    
    if colstart < colend:
        for row in range(rowend-1,rowstart-1,-1):
            print(matrix[row][colstart],end=" ")
        colstart+=1
print()
#pascal's triangle
n  = 4
final = []
for i in range(n):
    temp = []
    for j in range(i+1):
        if j == 0 or i == j: temp.append(1)
        else: temp.append(final[i-1][j-1] + final[i-1][j])
    final.append(temp)
# print(final)


    
# TIME COMPLEXCITY O(n^3)bcoz we are  running loop n(n,3) time sincwe n is 7 for this question
# but overally it is O(n^3)
#Space Complexcity O(n) for fina;    
       
arr = [1, 2, 2, 3, 3, 4, 5]
arr = [1, 2, 3, 4, 5, 6, 7]
arr = [1, 2, 4, 5, 6, 7, 16]


def find_ans(arr): 
    final = [] 
    def check(ans):

        c = arr.copy()
        c.remove(ans[0])
        c.remove(ans[1])
        c.remove(ans[2])
        if ans[0] + ans[1] == c[0]:
            if ans[0] + ans[2] == c[1]:
                if ans[1] + ans[2] == c[2]:
                    if ans[0] + ans[1] + ans[2]: 
                        final.extend(ans)
                        return True
        return False 
    def subsequence(i,ans):
        if len(ans) == 3: 
            return check(ans)
        if i >= len(arr):
            return False
        
        return subsequence(i+1,ans+[arr[i]]) or subsequence(i+1,ans)
    if subsequence(0,[]):
        print("YES")
        print(final)
    else:
        print("NO")
# find_ans(arr)
            

#Rotate 90 degrees 
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]
       ]

for i in range(len(arr)):
    for j in range(i+1,len(arr[0])):
        arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
for i in arr:
    i.reverse()
print(arr)
            
        
