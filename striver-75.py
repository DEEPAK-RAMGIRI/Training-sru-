# ================================================== 1. Two Sum   ==================================================
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
        
        
#  ================================================== 217. Contains Duplicate  ==================================================
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

#  ================================================== 238. Product of Array Except Self ==================================================
# Time Complexcity O(n^2):
# Space Complexcity O(1)
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
        
#  ================================================== 53. Maximum Subarray  ==================================================
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

# ================================================== 152. Maximum Product Subarray ==================================================
# Time Complexcity O(n^3)
# Space Complexcity O(1)
nums = [2,3,-2,4]
maxi = nums[0]
def max_prod_subarray():
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            prod = 1
            for k in range(i,j+1):
                prod *= nums[k]
            maxi = max(maxi,prod)
    return(maxi)

# Time Complexcity O(n^2)
# Space Complexcity O(1)
def max_prod_subarray():
    maxi = nums[0]
    for i in range(len(nums)):
        prod = nums[i]
        for j in range(i+1,len(nums)):
            prod *= nums[j]
            maxi = max(prod,maxi)
    # return(maxi)
    
    
# Time Complexcity O(n)
# Space Complexcity O(1)
def max_prod_subarray(nums):
    maxi = mini = ans = nums[0]
    for i in nums[1:]:
        if i < 0:
            maxi,mini = mini,maxi
        maxi = max(i,maxi*i)
        mini = min(i, mini * i)
        ans = max(maxi,ans)
        
    return ans  

# print(max_prod_subarray([2,3,-2,4]))  

# ================================================== Find Minimum in Rotated Sorted Array ================================================== 
nums = [3,4,5,1,2]

# Time Complexcity O(n)
# Space Complexcity O(1)
def find_mini():
    if not nums: return 0
    mini = nums[0]
    for i in nums[1:]:
        mini = min(i,mini)
    return mini

# Time Complexcity O(log n)
# Space Complexcity O(1)

def find_mini():
    if not nums: return 0
    left = 0
    right = len(nums)-1
    while left < right:
        mid = left + ((right - left) >> 1)
        if left+1 == right:
            return min(nums[left],nums[right])
        elif nums[left] < nums[mid] < nums[right]:
            right = mid
        else:
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
            
#================================================== Search in Rotated Sorted Array  ==================================================  
    
nums = [4,5,6,7,0,1,2]
target = 0
# Time Complexcity O(n)
# Space Complexcity O(1)
def find_element():
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def find_element():
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid +1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid +1
            else:
                right = mid - 1
# ============================================== 3Sum ====================================================
# Time Complexcity O(n^3)
# Space Complexcity O(1)

nums = [-1,0,1,2,-1,-4]
# ans = set()
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+1,len(nums)):
#             if not nums[k] + nums[j] + nums[i]:
#                 ans.add(tuple(sorted([nums[k], nums[j], nums[i]])))
# print(ans)

# Time Complexcity O(n ^ 2)
# Space Complexcity O(1)

nums = [-1,0,1,2,-1,-4]
nums.sort()
ans = set()
for i in range(len(nums)-2):
    left = i + 1          
    right = len(nums) -1
    while left < right:
        target = nums[left] + nums[right] + nums[i]
        if  target == 0:
             ans.add(tuple(sorted([nums[i], nums[left], nums[right]])))
             left+=1
             right-=1
        elif target < 0:
            left+=1
        else:
            right-=1
# print(ans)

# ====================================== Container With Most Water =======================================
nums = [1,8,6,2,5,4,8,3,7]

# Time complexcity O(n)
# Space complexcity O(21)

left = 0
water = 0
right = len(nums) - 1
while left < right:
    water = max(water,(min(nums[left] , nums[right])* (right - left)))
    if nums[left] < nums[right]:
        left+=1
    else:
        right -=1
# print(water)
# =================================    sum of two integers     =============================================
     
# Time Complexcity O(32)
# Space Complexcity O(1)
def add(a,b):
    mask = (1 << 32) - 1
    while b:
        carry = (a & b) & mask
        a = (a ^ b) & mask
        b = (carry << 1)
    return a if a < ((1 << 31)-1) else ~(a ^ mask)
      
# =============================== 191. Number of 1 Bits ================================================
# Time complexcity O(no_of_set_bits(no)) ~ O(32)
# Space complexcity O(1)
def no_of_one_bits(no):
    count = 0
    while no:
        no = (no & (no - 1))
        count+=1
    return count

# ============================== Counting Bits ========================================================
# Time Complexcity O(n*32)
# Space complexcity O(1)

def counting_bits(no):
    ans = []
    for i in range(no+1):
        ans.append(no_of_one_bits(i))
    return ans

# ============================= find missing number ==================================================

# Time Complexcity O(n ^ 2)
# Space complexcity O(1)
def find_missing_no(nums):
    if not nums: return 0
    for i in range(len(nums)+1):
        for j in nums:
            if i == j:
                break
        else: return i
        
# Time Complexcity O(n)
# Space Complexcity O(n)

def find_missing_no(nums):
    if not nums: return 0
    temp = [0] * len(nums)
    for i in nums:
        temp[i] = 1
    for i in range(len(nums)):
        if nums[i] == 0: return i
    return len(nums) + 1

# Time Complexcity O(n)
# Space Complexcity O(1)

def find_missing_no(nums):
    nos = (len(nums) * (len(nums) + 1) ) >> 1
    for i in nums:
        nos = i
    return nos if nos else len(nums) + 1
# ========================================= Reverse bits ============================================================
        
def reverse_bits(no):
    binary = ''
    while no:
        binary += str(no % 2)
        no >>= 1
    for _ in range(32 - len(binary)): binary += '0'
    power = ans = 0
    for i in binary[::-1]:
        ans += (2 ** power) * int(i)
        power+=1
    print(ans)
 
# ==================================================== DP =================================================================              
    
# Time Complexcity O(2^(n))
# Space Complexcity O(h) 
n = 2
def climbing_stairs(index):
    if index <= 0:
        return 1
    return climbing_stairs(index - 1) + climbing_stairs(index - 2) 

# Time Complexcity O(n)
# Space Complexcity O(h)

dp = [-1 for _ in range(n)]
def climbing_stairs(index):
    if index <= 0:
        return 1
    if dp[index] != -1:
        return dp[index]
    dp[index] = climbing_stairs(index - 1) + climbing_stairs(index - 2)
    return dp[index]


# Time Complexcity O(n)
# Space Complexcity O(h)

dp[0],dp[1] = 1,2
def climbing_stairs(n):
    for i in range(2,n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n-1]

# Time Complexcity O(n)
# Space Complexcity O(1)
def climbing_stairs(n):
    prev,prev1 = 0,1
    for i in range(n):
        prev,prev1 =prev1,prev1+prev 
    return prev1

# ============================================ coin change ===========================================================================
coins = [1,2,5]
amount = 11
# Time Complexcity O(2 ^n )
# Space Complexcity O(h)
def coin_change(index,amount):
    if amount == 0: return 0
    if index < 0 or amount < 0: return float("inf")
    return min(1 + coin_change(index,amount-coins[index]) , coin_change(index - 1,amount))


# Time complexcity O(n^2)
# Space Complexcity O(n^2)
dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
def coin_change(index,amount):
    if amount == 0: return 0
    if index < 0 or amount < 0 : return float("inf")
    if dp[index][amount] != -1:
        return dp[index][amount]
    dp[index][amount]=  min ( 1 + coin_change(index,amount - coins[index]),coin_change(index -1 ,amount))
    return dp[index][amount]

# Time Complexcity O(n^2)
# Space Complexcity O(n ^ 2)
def coin_change():
    for index in range(len(coins)):
        for amt in range(amount + 1):
            if amt == 0:
                dp[index][amt] = 0
            else:
                taken = not_taken = float("inf")
                if amt - coins[index] >= 0: taken = 1 + dp[index][amt - coins[index]]
                if index-1 >= 0: not_taken = dp[index - 1][amt]
                dp[index][amt] = min(taken,not_taken)

    return dp[len(coins)-1][amount]
            
            
# Time Complexcity O(n^ 2)
# Space complexcity O(n)       
def coin_change():
    prev = []
    for index in range(len(coins)):
        temp = [0] * (amount + 1)
        for amt in range(amount + 1):
            if amt != 0:
                taken = not_taken = float("inf")
                if amt - coins[index] >= 0: taken = 1 + temp[amt - coins[index]]
                if index-1 >= 0: not_taken = prev[amt]
                temp[amt] = min(taken,not_taken)
        prev = temp

    return temp[-1]
  