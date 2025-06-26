# n = int(input())
#Dynamic Programming
#Recursion
#time Complexcity O(2 ^n)
#Space Complexcity O(n)
def fibancci(i):
    if not i: return 0
    if i == 1: return 1
    return fibancci(i - 1) + fibancci(i - 2)
# print(fibancci(n)) 


# memoization
# dp = [-1] * (n+1)
#time Complexcity O(n)
#Space Complexcity O(1)
def fibancci1(i):
    if not i: return 0
    elif i == 1: return 1
    elif dp[i] != -1: return dp[i]
    dp[i] = fibancci1(i-1) + fibancci1(i-2) 
    return dp[i]
# print(fibancci1(4))

#time Complexcity O(n)
#Space Complexcity O(1)
#Tabulation
# dp = [0,1] + [-1] * (n- 1)
# for i in range(2,n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])


#Space Optimization
#Time Complexcity O(n)
#Space Complexcity O(1)
n = 4
prev1,prev2 = 0,1
for i in range(2,n+1):
    prev1,prev2 = prev2,prev1 + prev2
# print(prev2)
# climbing stairs

n = 3
#Recursion
def function(i):
    if i <= 1:
        return 1
    return function(i - 1) + function(i - 2)
# print(function(n))

#Time Complexcity O(n)
#Space Complexcity O(n)
#memoization
dp = [1,2] + [-1] * (n - 1)
def function(i):
    if i <= 1: return 1
    elif dp[i] != -1: return dp[i]
    dp[i] = function(i - 1) + function(i - 2)
    return dp[i]
# print(function(n))
    
    
#tabulization
#Time Complexcity O(n)
#Space Complexcity O(n)
dp = [1,2]  + [-1] * (n - 1)
for i in range(2,n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
# print(dp[n - 1])

#Space Optimization
#Time Complexcity O(n)
#Space Coplexcity O(1)
n = 3
prev1,prev2 = 1,2
for i in range(2,n):
    prev1,prev2 = prev2,prev1+prev2
# print(prev2) 



#House robber
#Recursion
#Time Complexcity O(n ^ 2)
#Space Complexcity O(1)
nums = [1,2,3,1]
nums = [2,7,9,3,1]
def function(i):
    if i < 0: return 0
    first_cons = nums[i] + function(i - 2)
    secound_cons = function(i - 1)
    return max(first_cons,secound_cons)
    
# print(function(len(nums) - 1))


#Memoization
#Time Complexcity O(n)
#Space Complexcity O(n)
nums = [1,2,3,1]
nums = [2,7,9,3,1]
dp = [-1] * (len(nums)+1)
def function(i):
    if i < 0: return 0
    first_cons = nums[i] + function(i - 2)
    seecound_cons = function(i - 1)
    dp[i] = max(first_cons,seecound_cons)
    return dp[i]
# print(function(len(nums) - 1))

#Tabulation
#Time Complexcity O(n)
#Space Complexcity O(1)

nums = [1,2,3,1]
nums = [2,7,9,3,1]
if len(nums) <= 2: print(max(nums))
dp = [nums[0],max(nums[0],nums[1])] + [-1] * (len(nums) - 1)
for i in range(2,len(nums)):
    dp[i] = max(dp[i-1],dp[i-2] + nums[i])
# print(dp[len(nums) - 1])

#Space Optimization
#Time Complexcity O(n)
#Space Complexcity O(1)
nums = [1,2,3,1]
nums = [2,7,9,3,1]
if len(nums) <= 2: print(max(nums))
prev1,prev2 = nums[0],max(nums[0],nums[1])
for i in range(2,len(nums)):
    prev1,prev2 = prev2,max(prev1 + nums[i],prev2)
# print(prev2)


# Unique Paths
#time Complexcity O(2^n)
#Space Complexcity O(1)
m = 3
n = 7
def find(i,j):
    if i >= m or j >= n:  return 0
    elif i == m - 1 and j == n -1 : return 1
    return find(i+1,j) + find(i,j+1)
# print(find(0,0))

#memoization
#Time Complexcity O(n * m)
#Space Complexcity o(n *m)

dp = [[-1 for _ in range(n)]  for _ in range(m)]
def find(i,j):
    if i >= m or j >= n: return 0
    elif i == m - 1 and j == n - 1: return 1 
    elif dp[i][j] != -1: return dp[i][j]
    dp[i][j] = find(i+1,j) + find(i ,j +1)
    return dp[i][j]
# print(find(0,0))

#Tabulation
#Time Complexcity O(n * m)
#Space Complexcity o(n *m)
dp = [[0 for _ in range(n)]  for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not i or not j: dp[i][j] =  1
        else: dp[i][j] = dp[i-1][j] + dp[i][j - 1]
# print(dp[m-1][n-1])

#Time Complexcity O(2 ^ (m +n))
#Space Complexcity O(m+n)
text1 = "abcde"
text2 = "ace" 
def find(i,j):
    if i < 0 or j < 0: return 0
    if text1[i] == text2[j]: return 1 + find(i -1, j-1)
    else: return max(find(i - 1,j) , find(i,j - 1))
# print(find(len(text1) - 1,len(text2) - 1))

#memoization
#Time Complexcity O(n *m)
#Space Complexcity O(n * m)
dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
def find(i,j):
    if i < 0 or j < 0: return 0
    if text1[i] == text2[j]: return 1 + find(i -1, j-1)
    elif dp[i][j] != -1: return dp[i][j]
    else: dp[i][j] = max(find(i - 1,j) , find(i,j - 1))
    return dp[i][j]
# print(find(len(text1) - 1,len(text2) - 1))
# print(dp)


#tabulation
#time Complexcity O(n*m)
#Space Complexcity O(m*n)
text1 = "abcde"
text2 = "ace" 
dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
for i in range(1,len(text1)+1):
    for j in range(1,len(text2)+1):
        if text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1] 
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print("text",dp[len(text1)][len(text2)])

#Best Time to Buy and Sell Stock II
#Time Complexcity O(2 ^n)
#space Complexcity O(1)
prices = [7,1,5,3,6,4]
def recur(i, holding):
    if i == len(prices):return 0
    if holding: return max(prices[i] + recur(i + 1, False),recur(i + 1, True))
    else: return max(-prices[i] + recur(i + 1, True),recur(i + 1, False))
# print(recur(0, False))



# 279. Perfect Squares
# Time Complexcity o(2^n)
# Space Complexcity O(n) 
arr = [i ** 2 for i in range(1,int(n** 0.5) +1)] 
def find(n):
    if n == 0: return 0
    elif n < 0: return float("inf")
    count = float("inf")
    for i in arr:
        count = min(count,1 + find(n - i))
    return count
# print(find(n))

#memoization
# TIme Complexcity O(n)
# Space Complexcity O(n)
arr = [i ** 2 for i in range(1,int(n** 0.5) +1)] 
dp = [-1] * (n + 1)
def find(n):
    if not n: return 0
    elif n < 0: return float("inf")
    elif dp[n] != -1: return dp[n]
    count = float("inf")
    for i in arr:
        count = min(count,1 + find(n - i))
    dp[n] = count
    return dp[n]
# print(find(n))

# Minimum Insertion Steps to Make a String Palindrome
#Time Complexcity O(2 ^n)
#Space Complexcity O(1)
s = "mbadm"
def find(i,j):
    if i >= j: return 0
    elif s[i] == s[j]: return find(i + 1, j - 1)
    return min(1 + find(i+1,j) , 1 +find(i,j-1))
# print(find(0,len(s)-1))

#Time Complexcity O(n)
#Space Complexcity O(n)
dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
def find(i,j):
    if i >= j: return 0
    elif s[i] == s[j]: return find(i + 1, j - 1)
    elif dp[i][j] !=  -1: return dp[i][j]
    dp[i][j] =  min(1 + find(i+1,j) , 1 +find(i,j-1))
    return dp[i][j]
# print(find(0,len(s)-1))


