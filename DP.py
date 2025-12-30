# Recursion 
# dp = addvanced dp
# in dp we have choice and ask for optimal like minimum or maximum

# 0 1 knapsack problems
    # 3 types fractional (greedy) , 0 - 1 and bounded are dp
    
    
# knapsack dp

wt = [1,3,4,5]
pt = [1,4,5,7]
bag = 7

# Time Complexcity O(2 ^ n)
# Space Complexcity O(h)
def recursion(index,curr,sums):
    if index == len(wt):
        return sums
    total = recursion(index+1,curr,sums)
    if curr + wt[index] <= bag:
        total = max(total,recursion(index+1,curr + wt[index],sums + pt[index]))
    return total
    
# print(recursion(0,0,0))

def recursion(index,curr):
    if index >= len(wt):
        return 0
    total = recursion(index+1,curr)
    if curr + wt[index] <= bag:
        total = max(total,pt[index] + recursion(index+1,curr + wt[index]))
    return total
# print(recursion(0,0))

dp = [[-1 for _ in range(bag + 1)] for _ in range(len(wt))]

def memoization(index,curr):
    if index >= len(wt):
        return 0
    if dp[index][curr] != -1: return dp[index][curr]
    dp[index][curr] = memoization(index+1,curr)
    if curr + wt[index] <= bag:
        dp[index][curr] = max(dp[index][curr],pt[index] + memoization(index+1,curr + wt[index]))
    return dp[index][curr]
# print(memoization(0,0))


def tabulation():
    dp = [[0 for _ in range(bag + 1)] for _ in range(len(wt) + 1)]
    for i in range(len(wt)-1,-1,-1):
        for j in range(bag +1):
            dp[i][j] = dp[i + 1][j]
            if j + wt[i] <= bag:
                dp[i][j]  = max(dp[i][j],pt[i] + dp[i + 1][j + wt[i]])
    print(dp[0][0])        
# tabulation()  


def memory_optimization():
    dp = [0] * (bag + 1)

    for i in range(len(wt)):
        for j in range(bag, wt[i] - 1, -1):
            dp[j] = max(dp[j], pt[i] + dp[j - wt[i]])

    print(dp[bag])
    
    
# Subset Sum
nums = [2,3,7,8,10]
sums = 11

# Time Complexcit O(2 ^ n)
# Space Complexcity O(h)
def recursion(index,sums):
    if sums == 0:
        return True
    if index >= len(nums): return False
    skip = recursion(index + 1,sums)
    not_skip = False
    if sums - nums[index]>= 0:
        not_skip = recursion(index + 1,sums - nums[index])
    return skip or not_skip
# print(recursion(0,sums))

#Time Complexcity O(n * sums)
# space Complexcity O(n * sums)

dp = [[-1 for _ in range(sums + 1)] for _ in range(len(nums) + 1)]
def memoization(index,sums):
    if sums == 0: return True
    if index >= len(nums): return False
    if dp[index][sums] != -1 : return dp[index][sums]
    skip = memoization(index+ 1,sums)
    not_skip = False
    if sums - nums[index]>= 0:
        not_skip = memoization(index + 1,sums - nums[index])
    dp[index][sums] = skip or not_skip
    return dp[index][sums]
# print(memoization(0,sums))

#Time Complexcity O(n * sums)
# space Complexcity O(n * sums)
def tabulation(sums):
    dp = [[False for _ in range(sums + 1)] for _ in range(len(nums) + 1)]
    for i in range(len(nums)+1):
        dp[i][0] = True
    for i in range(len(nums)-1,-1,-1):
        for j in range(sums + 1):
            skip = dp[i + 1][j]
            not_skip = False
            if j - nums[i] >= 0:
                not_skip = dp[i + 1][j - nums[i]]
            dp[i][j] = skip or not_skip

    return dp[0][sums] 

# print(tabulation(sums))

# equal sum Partition problem
# Time Complexcity O(2^n)
# Space Complexcity O(h)
nums = [1,5,5,11]
total = sum(nums)
if total & 1: 
    print(False)
else:
    target = total >> 1
    def recursion(index,target):
        if target == 0:
            return True
        if index >= len(nums):
            return False
        skip = recursion(index+1,target)
        not_skip = False
        if target - nums[index] >= 0:
            not_skip = recursion(index + 1,target- nums[index])
        return skip or not_skip
            
            
# Time Complexcity O(n * target)
# Space Complexcity O(n * target)

nums = [1,5,5,11]
total = sum(nums)
if total & 1: 
    print(False)
else:
    target = total >> 1
    dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
    def memoization(index,target):
        if target == 0: return True
        if index >= len(nums): return False
        if dp[index][target] != -1: return dp[index][target]
        skip = memoization(index + 1,target)
        not_skip = False
        if target - nums[index] >= 0:
            not_skip = memoization(index + 1,target - nums[index])
        dp[index][target] = skip or not_skip
        return dp[index][target]
        
    # print(memoization(0,target))
    
def Tabulation():
    
    if total & 1: 
        print(False)
    else:
        target = total >> 1
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(len(nums)-1,-1,-1):
            for j in range(target + 1):
                skip = dp[i + 1][j]
                not_skip = False
                if j - nums[i] >= 0:
                    not_skip = dp[i + 1][j - nums[i]]
            dp[i][j] = skip or not_skip
        print(dp[0][target])
        
# Tabulation()

# Count of subset sum
arr = [1,2,3,5,6,8,10]
sums = 10

# Time complexcity O(2 ^ n)
# Space complexcity O(h)
def recursion(index,sums):
    if sums == 0: return 1
    if index >= len(arr): return 0
    skip = recursion(index + 1,sums)
    not_skip = 0
    if sums - arr[index] >= 0:
        not_skip = recursion(index + 1,sums - arr[index])
    return skip + not_skip
# print(recursion(0,sums))

# Time complexcity O(n * sums)
# Space COmplexcity O(n * sums)
arr = [1,2,3,5,6,8,10]
sums = 10
dp = [[-1 for _ in range(sums + 1)] for _ in range(len(arr) + 1)]
def memoization(index,sums):
    if sums == 0: return 1
    if index >= len(arr): return 0
    if dp[index][sums] != -1: return dp[index][sums]
    skip = memoization(index + 1,sums)
    not_skip = 0
    if sums - arr[index] >= 0:
        not_skip = memoization(index + 1,sums - arr[index])
    dp[index][sums] = skip + not_skip
    return dp[index][sums]
# print(memoization(0,sums))


# Time complexcity O(n * sums)
# Space COmplexcity O(n * sums)
arr = [1,2,3,5,6,8,10]
sums = 10
def Tabulation():
    dp = [[0 for _ in range(sums + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        dp[i][0] = 1
    for i in range(len(arr)-1,-1,-1):
        for j in range(sums + 1):
            skip = dp[i + 1][j]
            not_skip = 0
            if j - arr[i] >= 0:
               not_skip = dp[i + 1][j - arr[i]]
            dp[i][j] = not_skip + skip
    # for i in range(len(arr)):
    #     print(dp[i])
    return dp[0][sums]

# print(Tabulation())  

# Partition A Set Into Two Subsets With Minimum Absolute Sum Difference
        
    
arr  = [2,3,7]
sums =sum(arr)  # because this is the maximum number we get from the nums
def tabulation():
    dp = [[False for _ in range(sums + 1)] for _ in range(len(arr) + 1)]
    
    for i in range(len(arr) + 1):
        dp[i][0] = True
    for i in range(len(arr) - 1,-1,-1):
        for j in range(sums + 1): 
            skip = dp[i + 1][j]
            take = False
            if j - arr[i] >= 0:
                take = dp[i + 1][j - arr[i]]
            dp[i][j] = skip or take
    return dp[0]
                
def find_min_diff():
    dp = tabulation() # taking the elements in which i can find the all sums are possibles
    min_diff = float("inf") 
    for s1 in range(len(dp)):
        if dp[s1]:
            s2 = sums - s1 # finding secound subset value
            # min_diff = min(min_diff,abs(s2 - s1)) # (sums -s1)-s1 = sums - (2 * s1)
            min_diff = min(min_diff, abs(sums - (2 * s1)))
    print(min_diff)
# find_min_diff()
    
# Count the number of subset with a given difference 
# Target Sum is also similar to this 

# The Idea is to find the count for that 
# diff = s2 - s1
# sums = s2 + s1
# we have 2s2 = diff + sums ~ s2 = (diff + sums) // 2
# in question we have diff and we can find the sums with help sum(array)
    
# so we need to find the count of the subsets where target is s2

arr = [1,2,1,3]
diff = 1
def Tabulation(sums):
    dp = [[0 for _ in range(sums + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        dp[i][0] = 1
    for i in range(len(arr)-1,-1,-1):
        for j in range(1,sums + 1):
            skip = dp[i + 1][j]
            take = 0
            if j - arr[i] >= 0:
                take = dp[i + 1][j - arr[i]]
            dp[i][j] = skip + take
    return dp[0][sums]

# print(Tabulation((sum(arr) + diff)//2))



  
# Random Question
from collections import deque

def is_valid(s):
    bal = 0
    for ch in s:
        if ch == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
    return bal == 0


def brackets_with_k_swaps(n, k):
    start = "()" * n
    q = deque([(start, 0)])
    visited = set([(start, 0)])
    result = set()

    while q:
        s, swaps = q.popleft()

        if swaps == k:
            if is_valid(s):
                result.add(s)
            continue

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                new_s = s[:i] + s[i + 1] + s[i] + s[i + 2:]
                state = (new_s, swaps + 1)
                if state not in visited:
                    visited.add(state)
                    q.append(state)

    return result


# Example
n = 3
k = 2
print(brackets_with_k_swaps(n, k))
        
    
        
            
    
