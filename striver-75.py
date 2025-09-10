# 1. Two Sum
nums = [2,7,11,15]
target = 9

# Time Complexcity O(n^2)
# Space Complexcity O(1)
def two_sum():
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return [-1,-1]

# Time Complexcity O(n)
# Space Complexcity O(1) 
def two_sum():
    left = 0
    right = len(nums) - 1
    while left < right:
        if left + right == target:
            return [left,right]
        elif left + right < target:
            left+=1
        else:
            right -= 1
            
# Best Time to Buy and Sell Stock
# Time Complexcity O(n)
#Space Complexcity O(1)
prices = [7,1,5,3,6,4]
def buy_sell():
    if not prices: return 0
    maxi = prices[0]
    ans = 0
    for i in prices[1:]:
        maxi = min(maxi,i)
        ans = max(ans,i - maxi)
    return ans
        
        
# 217. Contains Duplicate
nums = [1,2,3,1]

#Time Complexcity O(n^2)
#Space Complexcity O(1)
def duplicates():
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return nums[i]

#Time Complexcity O(n)
#Space Complexcity O(n)
nums = [1,2,3,1]
def duplicates():
    seen = set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)
    return -1

# Time Complexcity O(n^2):
# Space Complexcity O(1)
# 238. Product of Array Except Self
nums = [1,2,3,4]
def product():
    ans = []
    for i in nums:
        temp = 1
        for j in nums:
            if i == j: continue 
            temp *= j
        ans.append(temp)
    return ans
# print(product())

# Time Complexcity O(n ^ 2)
# Space Complexcity O(n) 
def product():
    prefix = [1] * (len(nums))
    suffix = [1] * (len(nums))
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]
    
    for i in range(len(nums)-2,-1,-1):
        suffix[i] = suffix[i+1] * nums[i + 1]

    return [prefix[i] * suffix[i] for i in range(len(nums))]
        

# 53. Maximum Subarray
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Time Complexcity O(n^3)
# Space Complexcity O(1)
def max_subarray():
    maxi  = nums[0]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sums = 0
            for k in range(i,j+1):
                sums += nums[k]
            maxi = max(maxi,sums)
    return maxi
# print(max_subarray())


# Time Complexcity O(n^2)
# Space Complexcity O(1)
def max_subarray():
    maxi  = nums[0]
    for i in range(len(nums)):
        sums = 0
        for j in range(i,len(nums)):
            sums += nums[j]    
            maxi = max(maxi,sums)
    return maxi
# print(max_subarray())

  
# Time Complexcity O(n)
# Space Complexcity O(1)

maxi = nums[0]
sums = nums[0]
for i in range(len(nums)):
    maxi = max(maxi + nums[i],nums[i])
    sums = max(sums,maxi)
# print(sums) 