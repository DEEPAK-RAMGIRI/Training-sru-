    # ================================================== 1. Two Sum   ==================================================
    nums = [2,7,11,15]
    target = 9
    # 2 for loops
    # Time Complexcity O(n^2)
    # Space Complexcity O(1)
    def two_sum():
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [-1,-1]
    
    # Binary 
    # Time Complexcity O(n log n)
    # Space Complexcity O(1) 
    nums.sort()
    def two_sum():
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left,right]
            elif nums[left] + nums[right] < target:
                left+=1
            else:
                right -= 1
    
    # Time Complexcity O(n)
    # Space Complexcity O(n)
    def two_sum():
        maps = dict()
        n = len(nums)
        for i in range(n):
            if  target - nums[i] in maps:
                return [maps[target - nums[i]],i]
            maps[nums[i]] = i
        return []
            
#======================================================== Best Time to Buy and Sell Stock ===============================================
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
#  for loops
#Time Complexcity O(n^2)
#Space Complexcity O(1)
def duplicates():
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return nums[i]
# using sort
# Time complexcity O(n log n)
# Space complexcity O(1)
def duplicates():
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
    return -1

# using set
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
# 2 loops
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

# using suffix and preffix
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
# using 3 for loop
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

# using 2 for loop
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

# Kadane's algorithm
# using 1 for loop
# Time Complexcity O(n)
# Space Complexcity O(1)

maxi = nums[0]
sums = nums[0]
for i in range(len(nums)):
    maxi = max(maxi + nums[i],nums[i])
    sums = max(sums,maxi)
# print(sums) 

# ================================================== 152. Maximum Product Subarray ==================================================
# using 3 loops
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

# using 2 loops
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
#linear search
# Time Complexcity O(n)
# Space Complexcity O(1)
def find_mini():
    if not nums: return 0
    mini = nums[0]
    for i in nums[1:]:
        mini = min(i,mini)
    return mini

# Binary search (modified)
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
#Linear search
# Time Complexcity O(n)
# Space Complexcity O(1)
def find_element():
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# bianry search (modified)
# Time Complexcity O(log n)
# Space Complexcity O(1)
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
# using 3 loops
# Time Complexcity O(n^3)
# Space Complexcity O(1)
nums = [-1,0,1,2,-1,-4]
def sum3(nums):
    ans = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if not nums[k] + nums[j] + nums[i]:
                    ans.add(tuple(sorted([nums[k], nums[j], nums[i]])))
    print(ans)
    
    
# binary search (modified)
# Time Complexcity O(n ^ 2)
# Space Complexcity O(1)
def sum3(nums):
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
    print(ans)

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
# ===== ========================================= Climbing Stairs ========================================================            
    
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
# ========================================================= Longest Increasing Subsequence ==============================================
nums = [10,9,2,5,3,7,101,18] 
count = [0]
#Recursion
# Time ComplexcityO(2 ^n)
# Space Complexcity O(h)
def lis(index,temp):
    if index == len(nums):
        return 0
    not_taken = lis(index+1,temp)
    taken = 0
    if temp == -1 or nums[index] > nums[temp]:
        taken = 1 + lis(index+1,index)
    count[0] = max(not_taken,taken)
    return count[0]

# Memoization
# Time Complexcity O(n^2)
# Space Complexcity O(n^2)
dp = [[-1 for _ in range(len(nums) + 1)]for _ in range(len(nums))]
def lis(index,temp):
    if index == len(nums):
        return 0
    if dp[index][temp] != -1: return dp[index][temp]
    not_taken = lis(index+1,temp)
    taken = 0 
    if temp == -1 or nums[index] > nums[temp]: # instead of taking number take index and compare future me
        taken = 1 + lis(index+1,index)
    dp[index][temp] = max(not_taken,taken)
    return dp[index][temp]

# Time Complexcity O(n^2)
# Space Complexcity O(n^2) #but efficent
dp = dict()
def lis(index,temp):
    if index == len(nums):
        return 0
    if (index,temp) in dp:
        return dp[index,temp]
    not_taken = lis(index+1,temp)
    taken = 0
    if temp == -1 or nums[temp] < nums[index]:
        taken = 1 + lis(index+1,index)
    dp[index,temp] =  max(taken,not_taken)
    return dp[index,temp]
# print(lis(0,-1))

# Tabulation
def lis():
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i],dp[j] + 1)
    return max(dp)

# ===================================================== Longest Common Subsequence ========================================================
text1 = 'abcde'
text2 = 'ace'

#Time Complexcity O(2^(m + n))
#Space Complexcity O(m+n) # stack space

def lcs(i,j):
    if i < 0 or j < 0: return 0
    if text1[i] == text2[j]: return 1 + lcs(i-1,j-1)
    else: return max(lcs(i-1,j),lcs(i,j-1))
    
# Time Complexcity O(n^2)
# Space Complexcity O(n^2)

dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
def lcs(i,j):
    if i< 0 or j < 0 : return 0
    if text1[i] == text2[j]: return 1 + lcs(i-1,j-1)
    elif dp[i][j] != -1: return dp[i][j]
    dp[i][j] = max(lcs(i-1,j),lcs(i,j-1))
    return dp[i][j]


# print(dp)
        
# Time Complexcity O(n ^ 2)
#Space Complexcity O( n ^ 2)    
dp = dict()
def lcs(i,j):
    if i< 0 or j < 0 : return 0
    if text1[i] == text2[j]: return 1 + lcs(i-1,j-1)
    elif (i,j) in dp: return dp[i,j]
    dp[i,j] = max(lcs(i-1,j),lcs(i,j-1))
    return dp[i,j]

#Tabulation
# Time Complexcity O(n ^ 2)
# Space Complexcity O( n ^ 2)
dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

for i in range(len(text1)):
    for j in range(len(text2)):
        if text1[i] == text2[j]:
            if i-1 >= 0 and j - 1 >= 0:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else: dp[i][j] = 1
        else:
            dp[i][j] = max(dp[i - 1][j] if i - 1 >= 0 else 0 , dp[i][j-1] if j-1 >= 0 else 0)

# Space Optimization
# Time Complexcity O(n^2)
#Space COmplexcity O(n)
dp = [-1] * len(text2)
for i in range(len(text1)):
    temp = [0] * len(text2)
    for j in range(len(text2)):
        if text1[i] == text2[j]:
            if i-1 >= 0 and j-1 >= 0:
                temp[j] = 1 + dp[j-1]
            else:
                temp[j] = 1
        else:
            temp[j] = max(dp[j] if i-1 >= 0 else 0 , temp[j-1] if j-1 >=0 else 0)
    dp = temp
# ================================================== word Break ==========================================================================

s = "leetcode"
wordDict = ["leet","code"]  

# Recursion
# Time Complexcity O(2^n)
# Space Complexcity O(n)
seen = set(wordDict)
def wordbreak(index):
    if len(s) == index:
        return True
    for i in range(index+1,len(s)+1):
        if s[index:i] in seen and wordbreak(i):
            return True
    return False
# print(wordbreak(0))
              
              
# Time Complexcity O()
# Space Complecity O(n)

dp = [-1 for _ in range(len(s)+1)]
def word_break(index):
    if len(s) == index: return True
    if dp[index] != -1: return dp[index]
    for i in range(index+1,len(s)+1):
        if s[index:i] in seen and word_break(i):
            dp[index] = True
            return dp[index]
    dp[index] = False
    return dp[index]
# print(word_break(0)) 

# Time Complexcity O(n^2)
# Space Complexcity O(n)
dp = dict()
def word_break(index):
    if len(s) == index: return True
    if index in dp: return dp[index]
    for i in range(index+1,len(s)+1):
        if s[index:i] in seen and word_break(i):
            dp[index] = True
            return True
    dp[index] = False
    return dp[index]
# print(word_break(0))



# Time Complexcity O(n^2)
# Space Complexcity O(n)

dp = [False for _ in range(len(s)+1)]
dp[len(s)] = True

for index in range(len(s),-1,-1):
    for i in range(index+1, len(s)+1):
        if s[index:i] in seen and dp[i]:
            dp[index] = True
            break
# print(dp[0])
# ============================================== Combination Sum =====================================


# Time Complexcity O(2 ^ n)
# Space Complexcity O(2^n)
candidates = [2,3,6,7]
target = 7        

res = []
def find_combinations(sums,temp,index):
    if sums == target:
        res.append(temp)
        return
    if index == len(candidates):
        return
    
    find_combinations(sums,temp,index + 1)
    if sums + candidates[index] <= target:
        find_combinations(sums + candidates[index], temp + [candidates[index]] , index )

# find_combinations(0,[],0)


# ============================================================ House Robber ================================================================

nums = [1,2,3,1]
maxi = [0]

# Time Complexcity O(2 ^ n)
# Space Complexcity O(n) # Stack Space

def find(index):
    if index < 0: return 0
    skip = find(index-1)
    cons = nums[index] + find(index - 2)
    return max(cons, skip)


# Time Complexcity O(n)
# Space Complexcity O(n)
dp = [-1] * len(nums)
def find(index):
    if index < 0: return 0
    if dp[index] != -1: return dp[index] 
    skip = find(index-1)
    cons = nums[index] + find(index - 2)
    dp[index] = max(cons, skip)
    return dp[index]


# Time Complexcity O(n)
# Space Complexcity O(n) 

dp = dict()
def find(index):
    if index < 0: return 0
    if index in dp: return dp[index] 
    skip = find(index-1)
    cons = nums[index] + find(index - 2)
    dp[index] = max(cons, skip)
    return dp[index]


# Time Complexcity O(n)
# Space Complexcity O(n)
dp = dict()
def find():
    for i in range(len(nums)):
        skip = 0 if i - 1 < 0 else dp[i - 1] 
        cons = (0 if i - 2 < 0 else dp[i - 2]) + nums[i]
        dp[i] =  max(cons,skip)
    return dp[len(nums)-1]

# Time Complexcity O(n)
# Space Complexcity O(1)
def find():
    temp1,temp2 = 0, 0
    for i in range(len(nums)):
        temp1,temp2 = max(temp1,temp2 + nums[i]),temp1
    return (temp1)

# ========================================================== House Robber II =========================================================

nums = [2,3,2]
# Time Complexcity O(2^n)
# Space Complexcity O(n) 
def houseRobber(nums,index):
    if index < 0: return 0
    skip = find(index-1)
    cons = nums[index] + find(index - 2)
    return max(cons, skip)
# if nums.length == 1: print(nums[0])
# else: print(max(houseRobber(nums[1:],len(nums)-1),houseRobber(nums[:-1],len(nums)-1)))

# Time Complexcity O(2^n)
# Space Complexcity O(n) 
dp = [-1] * len(nums)
def houseRobber(nums,index):
    if index < 0: return 0
    skip = find(index - 1)
    cons = nums[index] +  find(index - 2)
    dp[index] = max(skip,cons)
    return dp[index]
 
# if nums.length == 1: print(nums[0])
# else: print(max(houseRobber(nums[1:],len(nums)-1),houseRobber(nums[:-1],len(nums)-1)))


# Time Complexcity O(n)
# Space Complexcity O(n)
dp = dict()
def find(nums):
    for i in range(len(nums)):
        skip = 0 if i - 1 < 0 else dp[i - 1] 
        cons = (0 if i - 2 < 0 else dp[i - 2]) + nums[i]
        dp[i] =  max(cons,skip)
    return dp[len(nums)-1]

# if nums.length == 1: print(nums[0])
# else: print(max(houseRobber(nums[1:]),houseRobber(nums[:-1]))

# Time Complexcity O(n)
# Space Complexcity O(1)
def find(nums):
    temp1,temp2 = 0, 0
    for i in range(len(nums)):
        temp1,temp2 = max(temp1,temp2 + nums[i]),temp1
    return (temp1)


# if nums.length == 1: print(nums[0])
# else: print(max(houseRobber(nums[1:]),houseRobber(nums[:-1])))

# ======================================== Decode Ways ================================================================================
s = "12"

# Time Complexcity O(2^n)
# Space Complexcity O(n) # Stack Space
def DecodeWays(index):
    if index == len(s): return 1
    if s[index] == '0': return 0
    total = DecodeWays(index + 1)
    if 10 <= int(s[index:index + 2] )<= 26:
        total += DecodeWays(index + 2)
    return total

# Time Complexcity O(n)
# Space Complexcity O(n)

dp = [-1] * len(s)
def DecodeWays(index):
    if index == len(s): return 1
    if s[index] == '0': return 0
    total = DecodeWays(index + 1)
    if 10 <= int(s[index:index + 2] )<= 26:
        total += DecodeWays(index + 2)
    return total

# Time Complexcity O(n)
# Space Complexcity O(n)

dp = dict()
def DecodeWays(index):
    if index == len(s): return 1
    if s[index] == '0': return 0
    if index in dp: return dp[index]
    dp[index] = DecodeWays(index + 1)
    if 10 <= int(s[index:index + 2] )<= 26:
        dp[index] += DecodeWays(index + 2)
    return dp[index]

# Time Complexcity O(n)
# Space Complexcity O(n)
dp = dict()
dp[len(s)] = 1
def DecodeWays():
    for i in range(len(s)-1,-1,-1):
        if s[i] == '0': 
            dp[i] = 0 
        else:
            dp[i] = dp[i + 1]
            if 10 <= int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]
    return dp[0]

# Time Complexcity O(n)
# Space Complexcity O(1)
def DecodeWays():
    one,two = 1,0
    for i in range(len(s)-1,-1,-1):
        if s[i] == '0':
            curr = 0
        else: 
            curr = one
            if 10 <= int(s[i:i+2]) <= 26:
                curr += two
        two,one = one, curr
    return one
             
# print(DecodeWays())

# ========================================================== Unique Paths =================================================================
m = 3
n = 7

# Time Complexcity O(2^(m + n))
# Space Complecity O(n) # Stack Space
def unique_paths(i,j):
    if i == 0 and j == 0: return 1
    if i < 0 or j < 0: return 0
    return unique_paths(i-1,j) + unique_paths(i,j-1)

# Time Complexcity O(m* n)
# Space Complexcity O(m* n) 
dp = [[-1 for _ in range(n)] for _ in range(m)]
def unique_paths(i,j):
    if i == 0 and j == 0: return 1
    if i <0 or j < 0: return 0
    if dp[i][j] != -1: return dp[i][j]
    dp[i][j] = unique_paths(i-1,j) + unique_paths(i,j-1)
    return dp[i][j]

# Time Complexcity O(m * n)
# Space Complexcity O(m * n)
dp = dict()
def unique_paths(i,j):
    if i == 0 and j == 0: return 1
    if i < 0 or j < 0: return 0
    if (i,j)in dp: return dp[i,j]
    dp[i,j] = unique_paths(i - 1,j) + unique_paths(i,j-1)
    return dp[i,j]  

# Time Complexcity O(m * n)
# Space Complexcity O(m * n)
def unique_paths():
    dp = dict()
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0: dp[i,j] = 1     
            else: dp[i,j] = (dp[i-1,j] if i - 1 >= 0 else 0 )+ (dp[i,j-1] if j-1 >= 0 else 0)
    return dp[m - 1, n - 1]

# Space Optimzation
# Time Complexcity O(n * m)
# Space Complexcity O(n)

def unique_paths():
    dp = []
    for i in range(m):
        temp = [0] * n
        for j in range(n):
            if i==0 and j == 0: temp[j] = 1
            else:
                temp[j] = (dp[j] if i - 1 >= 0 else 0) + (temp[j-1] if j - 1 >= 0 else 0)
        dp = temp.copy()
    return  dp[-1] 

# Time Complexcity O(1)
# Space Complexcity O(1)
import math
def unique_paths(m, n):
    return math.comb(m + n - 2, m - 1)
# print(unique_paths(m,n)) 

# ========================================= Jump Game ============================================================================
nums = [2,3,1,1,4]

# Recursion
# Time Complexcity O(2 ^ n)
# Space Complexcity O(n) # Stack Space
def jumpGame(index):
    if index == len(nums) - 1: return True
    if index > len(nums) : return False
    for i in range(1,nums[index]+1):
        if jumpGame(index + i):
            return True
    return False


# Memoization
# Time Complexcity O(n)
# Space Complexcity O(n) 

dp = [-1] * len(nums)
def jumpGame(index):
    if index == len(nums) - 1: return True
    if index > len(nums) : return False
    if dp[index] != -1: return dp[index]
    for i in range(1,nums[index]+1):
        if jumpGame(index + i):
            dp[index] = True
            return dp[index] 
    dp[index] = False
    return dp[index]

# Memoization
# Time Complexcity O(n)
# Space Complexcity O(n) 

dp = dict()
def jumpGame(index):
    if index == len(nums) - 1: return True
    if index > len(nums) : return False
    if index in dp: return dp[index]
    for i in range(1,nums[index]+1):
        if jumpGame(index + i):
            dp[index] = True
            return dp[index] 
    dp[index] = False
    return dp[index]  



# Tabulation
# Time Complexcity O(n)
# Space Complexcity O(n) 

dp = [False] * len(nums)
dp[-1] = True
def jumpGame():
    for index in range(len(nums)-2,-1,-1):
        for i in range(1,nums[index]+1):
            if dp[i + index]:
                dp[index] = True
                break
        else:
            dp[index] = False
    return dp[0]
        
        
# Space optimzation
# Time Complexcity O(n)
# Space Complexcity O(1)

def jumpGame():
    last = len(nums) - 1
    for i in range(len(nums) - 2,-1,-1):
        if last <= nums[i] + i:
            last = i
    return last == 0  
# print(jumpGame())

# =========================================================== Graphs =======================================================================
# ======================================================= Clone Graph ====================================================================


class Node:
    def __init__(self,node,neighbors = None):
        self.val = node
        self.neighbors = neighbors if neighbors is not None else []
        
# DFS
# Time Complexcity O(V + E)
# Space Complexcity O(V)
def clone(node):
    graph = dict()
    def dfs(node):
        if not node: 
            return None
        
        if node in graph:
            return graph[node]
        
        copy = Node(node.val)
        graph[node] = copy

        for i in node.neighbors:
            copy.neighbors.append(dfs(i))

        return copy
    return dfs(node)

# BFS
# Time complexcity (V + E)
# Space Complexcity O(V)
from collections import deque
def bfs(node):
    if not node: return None
    graph = {node: Node(node.val)}  
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for nei in curr.neighbors:
            if nei not in graph:
                graph[nei] = Node(nei.val)
                queue.append(nei)
            graph[curr].neighbors.append(graph[nei])

    return graph[node]

# ===================================================== Course Schedule ============================================================

from collections import defaultdict,deque
# BFS
# Time Complexcity O(V + E)
# Space Complexcity O(V)
def courseSchedule(numCourses,prerequisites):
       
        graph = defaultdict(list)
        indeg = [0] * numCourses 
        for i,j in prerequisites:
            graph[j].append(i)
            indeg[i]+=1
        
        queue = deque([])

        for i,value in enumerate(indeg):
            if value == 0:
                queue.append(i)
        
        ans = []
        while queue:
            index = queue.popleft()
            for i in graph[index]:
                indeg[i]-=1
                if indeg[i] == 0:
                    queue.append(i)
            ans.append(index)
        return len(ans) == numCourses

# DFS
# Time Complexcity O( V + E)
# Space Complexcity O(V)

def find(numCourse,course):
    graph = defaultdict(list)
    for i, j in course:
        graph[j].append(i)
        
    visit = [0] * numCourse
    
    def dfs(index):
        if visit[index] == 1:
            return False
        if visit[index] == 2:
            return True
        
        visit[index] = 1
        for i in graph[i]:
            if not dfs(i):
                return False
        visit[index] = 2
        return True
    
    for i in range(numCourse):
        if not dfs(i): return False
    return True

# ======================================================= Pacific Atlantic Water Flow ==================================================
# DFS
# Time Complexcity O(m * n) * O(m * n)
#Space Complexcity O(m * n)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
m = len(heights) - 1
n = len(heights[0]) - 1

def pacificoratlantic(i,j,visit):
    visit.add((i,j))
    for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= x + i <= m and 0 <= y + j <= n and heights[i+x][j + y] >= heights[i][j] and (i+x,j+y) not in visit:
            pacificoratlantic(i+x,j+y,visit)
              
pacific = set()
atlantic = set()

for i in range(m + 1):
    pacificoratlantic(i,0,pacific)
    pacificoratlantic(i,n,atlantic)
    
for i in range(n + 1):
    pacificoratlantic(0,i,pacific)
    pacificoratlantic(n-1,i,atlantic)
    
# BFS
# Time Complexcity O(m * n) * (m * n)
# Space Complexcity O(m * n)

from collections import deque
def pacificoratlantic(i,j,visit):
    queue = deque([(i,j)])
    while queue:
        i,j = queue.popleft()
        visit.add((i,j))
        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0<= x + i <= m and 0<= y + j <=  n and heights[i+x][j+y] >= heights[i][j] and (i+x,j+y) not in visit:
                queue.append((i+x,j + y))
    
pacific = set()
atlantic = set()

# for i in range(m + 1):
#     pacificoratlantic(i,0,pacific)
#     pacificoratlantic(i,m-1,atlantic)

    
# for i in range(n + 1):
#     pacificoratlantic(0,i,pacific)
#     pacificoratlantic((n-1),i,atlantic)
    
# print(pacific & atlantic)

# ======================================= Number Of Islands =====================================================================

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]

]

# DFS
# Time Complexcity O(m * n)
# Space Complexcity O(m * n) 

m = len(grid)
n = len(grid[0])

visited = [[False] * n for _ in range(m)]
    
def no_of_islands(i,j):
    if  i < 0 or i >= m or j >= n or grid[i][j] == '0' or visited[i][j]: 
        return 0
    visited[i][j] = True
    for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
        no_of_islands(i+x,j+y)
    return 1

land = 0    
# for i in range(m):
#     for j in range(n):
#         if grid[i][j] == '1':
#             land += no_of_islands(i,j)
# print(land)
    
    
# BFS
# Time Complexcity O(m * n)
# Space Complexcity O(m * n)

from collections import deque

m = len(grid)
n = len(grid[0])

visited = [[False] * n for _ in range(m)]

def no_of_islands(i,j):
    queue = deque([(i,j)])
    while queue:
        i,j = queue.popleft()
        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= i + x < m and 0 <= j + y < n and not visited[i+x][j+y] and grid[i +x][j + y] == '1':
                queue.append((i+x,j+y)) 
                visited[i+x][j+y] = True
    return 1

count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '1' and not visited[i][j]:
            count += no_of_islands(i,j)
# print(count)

#===================================================== Longest Consecutive Sequence =====================================================

# Time Complexcity O(n ^ 2)
# Space Complexcity O(1)
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

def lcs():
    maxi = 0
    for i in range(len(nums)):
        temp = nums[i]
        count = 1
        while temp + 1 in nums:
            temp = temp+1
            count+=1
        maxi = max(maxi,count)
    return (maxi)

# print(lcs())         

# Time Complexcity O(n log n)
# Space Complexcity O(1)
def lcs():
    nums.sort()   
    maxi = 0
    count = 1
    prev = nums[0]
    for i in range(1,len(nums)):
        if prev + 1 == nums[i]:
            count+=1
            prev = nums[i]
        else:
            count = 1
        maxi = max(maxi,count)
    print(maxi)

# Time Complexcity O(n)
# Space Complexcity O(n)
def lcs():
    maxi = 0
    count = 0
    num_set = set(nums)
    for i in nums:
        if i-1 not in num_set:
            count = 1
            temp = i + 1
            while temp in num_set:
                temp+=1
                count+=1
        maxi = max(maxi,count)
    return maxi
            
# lcs()
# =========================== Alien Dictionary ========================================================

# it is hard while implementing but method easy u had done this ur self future me
dictionary = ['baa','abcd','abca','cab','cad']

from collections import defaultdict,deque

graph = defaultdict(list)
indeg = [0] * 26
exist = [False] * 26

def create(string1,string2):
    i = 0
    j = 0
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            graph[ord(string1[i]) - ord('a')].append(string2[j])
            indeg[ord(string2[j]) - ord('a')]+=1
            break
        i+=1
        j+=1
for i in range(1,len(dictionary)):
      create(dictionary[i-1],dictionary[i])

for i in dictionary:
    for j in i:
        exist[ord(j) - ord('a')] = True
      
# BFS
# Time Complexcity O(V + E)
# Space Complexcity O(V)

# print(indeg)
queue = deque([])
for i in range(26):
    if exist[i] and indeg[i] == 0:
        queue.append(i)
        
# print(graph)
ans = []
while queue:
    index = queue.popleft()
    ans.append(chr(index + ord('a')))
    for i in graph[index]:
        indeg[ord(i) - ord('a')]-=1
        if indeg[ord(i) - ord('a')] == 0:
            queue.append(ord(i) - ord('a'))
# print(ans)     

# ======================================= valid graph Tree ========================================================
nums = [[0,1],[0,2],[0,3],[1,4]]

graph = defaultdict(list)
maxi = 0
for i,j in nums:
   graph[i].append(j)
   graph[j].append(i)
   maxi = max(i,j,maxi)
   
print(graph)
start = 0
# BFS
# Time Complexcity O(V + E)
# Space Complexcity O(V)

visited = [False] * (maxi + 1)
visited[start] = True

def bfs():
    queue = deque([(start , -1)])
    while queue:
        node,parent = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,node))
            elif parent != i:
                return False
    return True        

# DFS
# Time Complexcity O( V + E)
# Space Complexcity O(V)
visited = [False] * (maxi + 1)
def dfs(parent,node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            if not dfs(node,i):
                return False
        elif parent != i:
            return False
    return True

print(dfs(-1,0))
    
