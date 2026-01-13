
# sum of first n elements where it look like this -1 + 2 - 3 + 4 -5...
# n = int(input())
# if n % 2 == 0:
#     print(n // 2)
# else:
#     print(-(n + 1) // 2)



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
# print(brackets_with_k_swaps(n, k))


# unbonded Knapsack
weights = [2, 3, 4]
values  = [4, 5, 7]
W = 7

# Time Complexcity O(2 ^ n)
# Space complexcity O(H)
def recursion(index,W):
    if index >= len(weights) or W == 0:
        return 0
    skip = recursion(index + 1,W)
    take = 0
    if W - weights[index] >= 0:
        take = values[index] + recursion(index,W - weights[index])
    return max(skip,take)
# print(recursion(0,W)) 

# Time Complexcity O(n * w)
# Space Complexcity O(n * w)
dp = [[-1 for _ in range(W + 1)]for _ in range(len(weights) + 1)]
def memoization(index,W):
    if index >= len(weights) or W == 0:
        return 0
    if dp[index][W] != -1:
        return dp[index][W]
    skip = memoization(index + 1, W)
    take = 0
    if W - weights[index] >= 0:
        take = values[index] + memoization(index,W - weights[index])
    dp[index][W] = max(skip,take)
    return dp[index][W]

# print(memoization(0,W))

# Time Complexcity O(n * w)
# Space Complexcity O(n * w)
def Tabulation():
    dp = [[0 for _ in range(W + 1)]for _ in range(len(weights) + 1)]
    for i in range(len(weights)-1,-1,-1):
        for j in range(W + 1):
            dp[i][j] = dp[i + 1][j]
            if j - weights[i] >= 0:
                dp[i][j] = max(dp[i][j] , values[i] + dp[i][j - weights[i]])
    # print(dp)
    return dp[0][W]
# print(Tabulation())

# Time Complexcity O(n * w)
# Space Complexcity O(w)
def memoryOptimization():
    prev = [0] * (W + 1)
    for i in range(len(weights)-1,-1,-1):
        temp = [0] * (W + 1)
        for j in range(W + 1):
            temp[j] = prev[j]
            if j - weights[i] >=0 :
                temp[j] = max(temp[j], values[i] + temp[j - weights[i]])
        prev= temp[:]
               
    return prev[W]
# print(memoryOptimization())


# Rod Cutting Problem

# Time Complexcity O(2 ^ n)
# Space Complexcity O(h)

length = [1,2,3,4]
profit = [5,6,8,8]
N = 4

def recursion(index,N):
    if N == 0 or index >= len(length):
        return 0
    skip = recursion(index + 1, N)
    take = 0
    if N - length[index] >= 0:
        take = profit[index] + recursion(index ,N - length[index])
    return max(skip,take)
# print(recursion(0,N))

# Time Complexcity O(n * m)
# Space Complexcity O(n * m)
dp = [[-1 for _ in range(N + 1)] for _ in range(len(length) + 1)]

def memoization(index , n):
    if n == 0 or index >= len(length):
        return 0
    if dp[index][n] != -1: return dp[index][n] 
    skip = memoization(index + 1,n )
    take = 0
    if n - length[index] >= 0:
        take = profit[index] + memoization(index, n - length[index])
    dp[index][n] = max(skip , take)
    return dp[index][n]
# print(memoization(0,N))


# Time Complexcity O(n * m)
# Space Complexcity O(n * m)
def Tabulation(n):
    dp = [[0 for _ in range(N + 1)] for _ in range(len(length) + 1)]
    for i in range(len(length)-1,-1,-1):
        for j in range(n + 1):
            dp[i][j] = dp[i + 1][j]
            if j - length[i] >= 0:
                dp[i][j] = max(dp[i][j] ,profit[i] + dp[i][j - length[i]])
    return dp[0][n]
# print(Tabulation(N))

length = [1,2,3,4]
profit = [5,6,8,8]
N = 4

# Time Complexcity O(n * m)
# Space Complexcity O(N)
def Space_Optimization():
    dp = [0] * (N + 1)
    for i in range(len(length)-1,-1,-1):
        temp = [0] * (N + 1)
        for j in range(N + 1):
            temp[j] = dp[j]
            if j - length[i] >= 0:
                temp[j] = max(temp[j], profit[i] + temp[j - length[i]])
        dp = temp[:]
    print(dp[N])
# Space_Optimization()

# Coin change problem

coins = [1,2,3,5]
money = 8

# Time Complexcity O(2 ^ n)
# Space Complexcity O(h)
def recursion(index,money):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0
    
    total = recursion(index + 1,money)
    
    if money - coins[index] >= 0:
        total += recursion(index,money - coins[index])
    
    return total

# print(recursion(0,money))

# Time Complexcity O(money * n)
# Space Complexcity O(money * n)

dp = [[-1 for _ in range(money + 1)] for _ in range(len(coins) + 1)]
def Memoization(index,money):
    if money == 0: return 1
    if index >= len(coins):return 0
    if dp[index][money] != -1: return dp[index][money]
    total = Memoization(index + 1,money)
    if money - coins[index] >= 0:
        total += Memoization(index,money - coins[index])
    dp[index][money] = total
    return dp[index][money]
# print(Memoization(0,money))
     

# Time Complexcity O(money * n)
# Space Complexcity O(money * n)

def Tabulation(money):
    dp = [[0 for _ in range(money + 1)] for _ in range(len(coins) + 1)] 
    for i in range(len(nums) + 1):
        dp[i][0] = 1
    for i in range(len(coins)-1,-1,-1):
        for j in range(money + 1):
            total = dp[i + 1][j]
            if j - coins[i] >= 0:
                total += dp[i][j - coins[i]]
            dp[i][j] = total
    return dp[0][money]

# print(Tabulation(money))


# Time Complexcity O(money * n)
# Space Complexcity O(money)
def Space_optimization(money):
    dp = [1] + [0] * money
    for i in range(len(coins)-1,-1,-1):
        temp = [0] * (money + 1)
        for j in range(money + 1):
            temp[j] = dp[j]
            if j - coins[i] >= 0:
                temp[j] += temp[j - coins[i]]
        dp = temp[:]
    return dp[money]
            
# print(Space_optimization(money))

# coin change 2 
# minimum count

money = 125
moneys = [ 1,5,10,20,100 ]
def recursion(index,money):
    if money == 0: return 0
    if index >= len(moneys):
        return float("inf")
    skip = recursion(index + 1,money)
    if money - moneys[index] >= 0:
        skip =min(skip,1 + recursion(index,money - moneys[index]))
    return skip

# print(recursion(0,money))

dp = [[-1 for _ in range(money + 1)] for _ in range(len(moneys) +  1)]
def memoization(index,money):
    if money == 0: return 0
    if index >= len(moneys):
        return float("inf")
    if dp[index][money] != -1:
        return dp[index][money]
    dp[index][money] = memoization(index + 1,money)
    if money - moneys[index] >= 0:
        dp[index][money] = min(dp[index][money],1 + memoization(index,money - moneys[index]))
    return dp[index][money]

# print(memoization(0,money))

def Tabulation(m):
    dp = [[float("inf") for _ in range(m + 1)] for _ in range(len(moneys) +  1)]
    for i in range(len(moneys) + 1):
        dp[i][0] = 0
    for index in range(len(moneys)-1,-1,-1):
        for money in range(1,m + 1): 
            dp[index][money] = dp[index + 1][money]
            if money - moneys[index] >= 0:
                dp[index][money] = min(dp[index][money],1 + dp[index][money - moneys[index]])
    print(dp[0][m])
    
# space optimiatio may be wrong
# best way to sort the coins and  do this
def another_method():
    money = int(input())
    coins = [100, 20, 10, 5, 1]

    count = 0
    for coin in coins:
        count += money // coin
        money %= coin

    print(count)
    
# longestCommonSubsequence LCS
string1 = 'abcdgh'
string2 = 'abedfhg'

# Time Complexcity O(2^ (m + n))
# Space Complexcity O(h) h= m* n
def recursion(i,j):
    if i >= len(string1) or j >= len(string2):
        return 0
    if string1[i] == string2[j]:
        return 1 + recursion(i + 1, j + 1)
    return max(recursion(i+1,j) , recursion(i,j + 1))
# print(recursion(0,0))

# Time Complexcity O(m * n)
# Space Comnplexcity O(m * n)
dp = [[-1 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
def memoization(i,j):
    if i >= len(string1) or j >= len(string2): return 0
    if dp[i][j] != -1: return dp[i][j]
    if string1[i] == string2[j]:
        dp[i][j] = 1 + memoization(i + 1,j +1)
    else:
        dp[i][j] = max(memoization(i + 1, j), memoization(i ,j + 1))
    return dp[i][j]
# print(memoization(0,0))


# Time Complexcity O(m * n)
# Space Comnplexcity O(m * n)
def Tabulation():
    dp = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1)-1,-1,-1):
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                dp[i][j] = 1 + dp[i + 1][j +1]
            else:
                dp[i][j] = max(dp[i + 1][j],dp[i][j + 1])
    return dp[0][0]
# print(Tabulation())

# Time Complexcity O(m * n)
# Space Comnplexcity O(n)
def SpaceOptimization():
    dp = [0] * (len(string2) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp = [0] * (len(string2) + 1)
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                temp[j] = 1 + dp[j +1]
            else:
                temp[j] = max(dp[j],temp[j + 1])
        dp = temp[:]
    return dp[0]
# print(SpaceOptimization())
        
# Longest Common Substring
# Time Complexcity O(n * m)
# Space Complexcity O(n)

string1 = 'abcde'
string2 = 'abfce'

def Tabulation():
    ans = 0
    dp = [0] * (len(string2) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp = [0] * (len(string2) + 1)
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                temp[j] = 1 + dp[j +1]
                ans = max(ans,temp[j])
        dp = temp[:]
    return ans
# print(Tabulation())

# printing Longest CommonSubsequence in string

string1 = 'abcde'
string2 = 'abfce'

def recursion(i,j):
    if i >= len(string1) or j >= len(string2):
        return ''
    if string1[i] == string2[j]:
        return string1[i] + recursion(i+1,j + 1)
    else:
        return max(recursion(i + 1,j) , recursion(i, j + 1) ,key = len)
# print(recursion(0,0))

dp = [[-1 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
def Memoization(i,j):
    if i>= len(string1) or j >= len(string2):
        return ''
    if dp[i][j] != -1: return dp[i][j]
    if string1[i] == string2[j]:
        dp[i][j] =  string1[i] + Memoization(i + 1,j +1)
    else:
        dp[i][j] = max(Memoization(i+1,j),Memoization(i,j + 1),key = len) 
    return dp[i][j]
# print(Memoization(0,0))

def Tabulation():
    dp = [['' for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1)-1,-1,-1):
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                dp[i][j] =  string1[i] + dp[i + 1][j +1]
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j + 1],key = len) 
    return dp[0][0]
# print(Tabulation())

def spaceOptimization():
    dp = [''] * (len(string2) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp  = [''] * (len(string2) + 1)
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                temp[j] =  string1[i] + dp[j +1]
            else:
                temp[j] = max(dp[j],temp[j + 1],key = len) 
        dp = temp[:]
    return dp[0]

# print(spaceOptimization())

# length of SuperSequence
# we need to find the length of the super seqence 
# so max to max the answer would be the size of m + n where m,n are string 1 and string2 respectively
# we need to remove common values and we get the total remaining size of the answer string

# code is similar to the longest common subsequence  

string1 = "acbcf"
string2 = "abcdaf"

def Tabulation():
    dp = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1)-1,-1,-1):
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                dp[i][j] = 1 + dp[i + 1][j +1]
            else:
                dp[i][j] = max(dp[i + 1][j],dp[i][j + 1])
    return dp[0][0]

# print(len(string1) + len(string2) - Tabulation())

def spaceOptimization():

    dp = [0] * (len(string2) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp = [0] * (len(string2) + 1)
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                temp[j] = 1 + dp[j +1]
            else:
                temp[j] = max(dp[j],temp[j + 1])
        dp = temp[:]
    
    print((len(string1) + len(string2)) - dp[0])
    
# spaceOptimization()

# printing  shortest subsequence or printing that super sequence
# same code as lcs but we are printing the sequence here
string1 = "acbcf"
string2 = "abcdaf"

def Tabulation():
    dp = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1)-1,-1,-1):
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                dp[i][j] = 1 + dp[i + 1][j +1]
            else:
                dp[i][j] = max(dp[i + 1][j],dp[i][j + 1])
    
    i = 0
    j = 0
    ans = ''
    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            ans += string1[i]
            i+=1
            j+=1
        elif dp[i + 1][j] > dp[i][j + 1]:
            ans += string1[i]
            i+=1
        else:
            ans += string2[j]
            j+=1
            
    while i < len(string1):
        ans += string1[i]
        i+=1
        
    while j < len(string2):
        ans += string2[j]
        j+=1
        
    print(ans)            
                
# Tabulation()


# printing minimum insertion and deletion


# idea is to find longest common subsequence from a and b
# then a - lcs we get the no of deletion
# then b - lcs we get the no of insertion  

string1 = 'heap'
string2 = 'pea' 
# ans  = 3
def Spaceoptimization():
    dp = [0] * (len(string2) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp = [0] * (len(string2) + 1)
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                temp[j] = 1 + dp[j +1]
            else:
                temp[j] = max(dp[j],temp[j + 1])
        dp = temp[:]
    
    deletion = len(string1) - dp[0]
    insertion = len(string2) - dp[0]
    print(deletion + insertion)
    
# Spaceoptimization()


# Longest Palindrome subsequence
# idea is to reverse the string and do lcs we will get common sbseqence and that to palindromez
string1 = "bbbab"
string2 = string1[::-1]
def LPS():
    
    dp = [0] * (len(string2) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp = [0] * (len(string2) + 1)
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                temp[j] = 1 + dp[j +1]
            else:
                temp[j] = max(dp[j],temp[j + 1])
        dp = temp[:]
    print(dp[0])
    
# LPS()

# minum deletion to make the lonest palindrom subsequence
# simple length - longest palindrome subsequencce 

string1 = "bbbab"
string2 = string1[::-1]
def LPS():
    
    dp = [0] * (len(string2) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp = [0] * (len(string2) + 1)
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                temp[j] = 1 + dp[j +1]
            else:
                temp[j] = max(dp[j],temp[j + 1])
        dp = temp[:]
    print(len(string1) - dp[0])
    
# LPS()


# minimum deletion to make srting palindome
# Time Complexcity O(2 ^ (m + n))
# Space Complexcity O(h)
string1 = 'agbcba'
def recursion(i,j):
    if i > j:
        return 0
    if string1[i] == string1[j]:
        return recursion(i + 1, j - 1)
    else:
        return 1 + min(recursion(i + 1,j) , recursion(i,j - 1))
# print(recursion(0,len(string1) - 1))

# Time Complexcity O(n ^ 2)
# space Complexcity O(n ^ 2)
dp = [[-1 for _ in range(len(string1) + 1)] for _ in range(len(string1) + 1)]
def memoization(i,j):
    if i > j: return 0
    if dp[i][j] != -1: return dp[i][j]
    if string1[i] == string1[j]: 
        dp[i][j] = memoization(i + 1,j - 1)
    else:
        dp[i][j] = 1 + min(memoization(i + 1,j) , memoization(i,j - 1))
    return dp[i][j]
# print(memoization(0,len(string1) - 1))


def Tabulation():
    dp = [[0 for _ in range(len(string1) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1) -1,-1,-1):
        for j in range(len(string1)):
            if i > j: continue
            elif string1[i] == string1[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j],dp[i][j - 1])
    # print(dp)
    return dp[0][len(string1)-1]
# print(Tabulation())

def SpaceOptimization():
    dp = [0] * (len(string1) + 1)
    for i in range(len(string1)-1,-1,-1):
        temp = [0] * (len(string1) + 1)
        for j in range(len(string1)):
            if  i > j : continue
            elif string1[i] == string1[j]:
                temp[j] = dp[j - 1]
            else:
                temp[j] = 1 + min(dp[j],temp[j - 1])
        dp = temp[:]
    return dp[len(string1) - 1]

# print(SpaceOptimization())
     
# longest_repeating_subsequence
           
string1 = "AABEBCDD"
string2 = string1
def Tabulation():
    dp = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1)-1,-1,-1):
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j] and i != j:
                dp[i][j] = 1 + dp[i + 1][j +1]
            else:
                dp[i][j] = max(dp[i + 1][j],dp[i][j + 1])
    return dp[0][0]

# print(Tabulation())

# Sequence Pattern matching
# here we want to find that string1 present in the string2
# if so we return True else False

string1  = 'axy'
string2 = 'advxcpy'

def Tabulation():
    dp = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1)-1,-1,-1):
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                dp[i][j] = 1 + dp[i +1][j +1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    if len(string1) == dp[0][0]:
        return True
    return False

# print(Tabulation())               


# minimum insertion to make the string palindrome

string1 = "acbcbda"

# Time Complexcity O (2 ^ n)
# Space Complexcity O(2 ^ n)
def recursion(i,j):
    if i >= j: return 0
    if string1[i] == string1[j]: return recursion(i + 1,j -1)
    else: return 1 + min(recursion(i+1,j),recursion(i,j - 1))

# print(recursion(0,len(string1)-1))

# Time Complexcity O(n ^ 2)
# Space Complexcity O(n ^ 2)
dp = [[-1 for _ in range(len(string1) + 1)] for _ in range(len(string1) + 1)]
def memoization(i,j):
    if i >= j: return 0
    if dp[i][j] != -1: return dp[i][j]
    if string1[i] == string1[j]: return memoization(i + 1,j - 1)
    else: return 1 + min(memoization(i + 1,j) ,memoization( i, j - 1))

# print(memoization(0,len(string1)-1))

# Time Complexcity O(n ^ 2)
# Space Complexcity O(n ^ 2)
def Tabulation():
    dp = [[0 for _ in range(len(string1) + 1)] for _ in range(len(string1) + 1)]
    for i in range(len(string1) -1,-1,-1):
        for j in range(len(string1)-1,-1,-1):
            if i >= j: continue
            if string1[i] == string1[j]: dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j],dp[i][j +1 ])
    return dp[0][len(string1) -1]
# print(Tabulation())

# Time Complexcity O(n^ 2)
# Space Complexcity O(n)
def SpaceOptimiztion():
    dp = [0] * (len(string1) + 1)
    for i in range(len(string1) -1,-1,-1):
        temp = [0] * (len(string1) + 1)
        for j in range(len(string1)-1,-1,-1):
            if i >= j: continue
            if string1[i] == string1[j]: temp[j] = dp[j - 1]
            else:
                temp[j] = 1 + min(dp[j],temp[j +1 ])
        dp = temp[:]
    return dp[len(string1) -1]
# print(SpaceOptimiztion())


# MATRIX CHAIN MULTIPLICATION
# time Complexcity O(2 ^ n)
#Space Complexcity O(h)
arr = [10,30,5,60]
def recursion(i,j):
    if i >= j: return 0
    mini = float("inf")
    for k in range(i , j):
        temp = recursion(i,k) + recursion(k + 1,j) + arr[i - 1] * arr[j] * arr[k]
        mini = min(mini,temp)
    return mini
# print(recursion(1,len(arr) - 1))

# Time Complexcity O(n ^ 3)
# Space Complexcity O(n ^ 2)
dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
def memoization(i,j):
    if i >= j:
        return 0
    if dp[i][j] != -1: return dp[i][j]
    dp[i][j] = float("inf")
    for k in range(i,j):
        temp = memoization(i ,k )+memoization(k + 1,j) + arr[i - 1] * arr[k] * arr[j]
        dp[i][j] = min(temp,dp[i][j])
    return dp[i][j]
# print(memoization(1,len(arr) - 1))

# Time Complexcity O(n ^ 3)
# Space Complexcity O(n ^ 2)
def Tabulation():
    dp = [[float("inf") for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr) -1,0,-1):
        for j in range(len(arr)):
            if i >= j: 
                dp[i][j] = 0
            else:
                for k in range(i,j):
                    temp = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j],temp)
    return dp[1][len(arr) - 1]
                
# print(Tabulation())

# palindrome parition

string1 = 'itin'

def palindrome(i,j):
    return string1[i : j + 1] == string1[i:j + 1][:: -1]

# def recursion(i,j):
#     if i >= j or palindrome(i,j): return 0
#     mini = float("inf")
#     for k in range(i,j):
#         temp = recursion(i,k) + recursion(k + 1,j) + 1
#         mini = min(mini,temp)
#     return mini 
# print(recursion(0,len(string1) - 1))

dp = [[ -1 for _ in range(len(string1))] for _ in range(len(string1))]
def memoization(i,j):
    if i >= j or palindrome(i,j): return 0
    if dp[i][j] != -1: return dp[i][j]
    mini = float("inf")
    for k in range(i,j):
        temp = memoization(i,k) + memoization(k + 1,j)  + 1
        mini = min(mini,temp)
    dp[i][j] = mini
    return dp[i][j]
# print(memoization(0,len(string1)-1))

def Tabulation():
    dp = [[ 0 for _ in range(len(string1))] for _ in range(len(string1))]
    for i in range(len(string1) - 1,-1,-1):
        for j in range(len(string1) - 1,-1,-1):
            if i >= j or palindrome(i,j):
                continue
            
            mini = float("inf")
            for k in range(i,j):
                temp = dp[i][k] + dp[k + 1][j]  + 1
                mini = min(mini,temp)
            dp[i][j] = mini
    return dp[0][len(string1) -1 ]
print(Tabulation())