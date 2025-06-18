# Maximum Points You Can Obtain from Cards

# Method 01
#Time Complexcity O(k)
#Space Complexcity O(1)
cardPoints = [1,2,3,4,5,6,1]
k = 3
total = maxi = sum(cardPoints[:k])
j = len(cardPoints) - 1
for i in range(k-1,-1,-1):
    maxi += cardPoints[j] - cardPoints[i]
    j-=1
    total = max(total,maxi)
# print(total)
 
#Method 02   
#Time Complexcity O(k)
#Space Complexcity O(1)
cardPoints = [1,2,3,4,5,6,1]
k = 3
total = maxi = sum(cardPoints[:k])
for i in range(k):
    maxi += cardPoints[~i] - cardPoints[k-i-1] 
    total = max(total,maxi)
# print(total)

#Time Complexcity O(n^2)
#Space Complexcity O(1)
s = "abciiidef"
k = 3
maxi = 0
vowels = {'a','e','i','o','u'}
for i in range(len(s)-k+1):
    count = 0
    for j in range(i,k+i):
        if s[j] in vowels:
            count+=1
    maxi = max(maxi,count)
# print(maxi)

# Time Complexcity O(n)
#Space Complexcity O(1)
s = "abciiidef"
k = 3
left = count = maxi = 0
vowels = {'a','e','i','o','u'}
for right in range(len(s)):
    if s[right] in vowels:
        count+=1
    if right - left + 1 > k:
        if s[left]in vowels:
            count-=1
        left+=1
    maxi = max(maxi,count)
# print(maxi)

# Max Consecutive Ones III
# Time Complexcity O(n^2)
#Space Complexcity O(1) 
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
maxi = 0
for i in range(len(nums)):
    count = 0 
    zeros = 0
    for j in range(i,len(nums)):
        if nums[j] == 1:
            count+=1
        else:
            if zeros < k:
                zeros+=1
                count+=1
            else:
                break
    maxi =max(maxi,count)
# print(maxi)
                    
#Time Complexcity O(n)
#Space Complexcity O(1)
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
left = maxi = 0
for right in range(len(nums)):
    if nums[right] == 0:
        k-=1
    while k < 0:
        if nums[left] == 0:
            k+=1
        left+=1
    maxi = max(maxi,right - left+1)
# print(maxi)

# Longest Substring Without Repeating Characters
#Time Complexcity O(2n) ~ O(n)
#Space Complexcity O(1) 
left = maxi = 0
nums = [1,1,0,1]
k = 1
for right in range(len(nums)):
    if nums[right] == 0:
        k-=1
    while k <0:
        if nums[left] == 0:
            k+=1
        left+=1
    maxi = max(maxi,right - left)
print(maxi - 1 if maxi == len(nums) else maxi)


#Time Complexcity O(n)
#Space Complexcity O(1)

nums = [1,1,0,1]
nums = [0,1,1,1,0,1,1,0,1]
right = count = maxi = curr = 0
flag = True
while right< len(nums):
    if nums[right] == 1:count+=1
    else:
        if flag:
            flag = False
        else:
            maxi = max(count,maxi)
            left = curr + 1
            count = right - left
        curr = right
    right+=1
if flag: print(len(nums)-1)
# else:print( max(count,maxi))


nums = [1,0,1,0,1]

goal = 2
#Time Complexcity O(n^2)
#Space Complexcity O(1)
count = 0
nums = [0,0,0,0,0]
goal = 0

for i in range(len(nums)):
    sums = 0
    for j in range(i,len(nums)):
        sums += nums[j]
        if sums == goal: count+=1
# print(count)

#Time Complexcity O(n)
#Space Complexcity O(n)
nums = [1,0,1,0,1]
goal = 2
nums = [0,0,0,0,0]
goal = 0

dictionary = {0:1}
sums =ans = 0
for i in nums:
    sums += i
    if sums in dictionary:
        ans += dictionary[sums - goal]
    dictionary[sums] = dictionary.get(sums,0)+1
# print(ans)
        
    
        
nums = [1,0,1,0,1]
goal = 2
def find(k):
    if k < 0 : return 0
    left = maxi = sums = 0
    for right in range(len(nums)):
        sums += nums[right]
        while sums > k:
            sums -= nums[left]
            left+=1
        maxi += right - left + 1
    return maxi
# print(find(goal) - find(goal - 1))


#Count Number of Nice Subarrays
# Time Complexcity O(n^2)
# Space Complexcity O(1)
nums = [1,1,2,1,1]
k = 3
count = 0
for i in range(len(nums)):
    value = 0
    for j in range(i,len(nums)):
        if nums[j] & 1:
            value+=1
        if value == k:
            count+=1
        if value > k:
            break
print(count)

            
        
                      
        
