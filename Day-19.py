#Dynamic Programming

#Even though you know about below just read once and visualise don't be over confident 
#its about problems :
#       --> Just try all possibe ways in recursion
#           just represent the problem in the index  terms
#           Do all the possible stuffs on it according to problem statement
#           sum all of stuff if problem says : count the no of ways
#           to find minimum of all stuff :take min of all stuffs
#fibanacci no
#method 01
n = 5 - 2
a = 0
b = 1
# print(a,b,end=" ")
while n > 0:
    c = a + b
    # print(c,end=" ")
    a,b = b,c
    n-=1
print()
#Method 02
n = 5    
a,b = 0,1
for _ in range(n):
    # print(a,end=" ")
    a,b = b,a + b
# print()

#method 03
def function(n):
    if n <= 1: return n
    return function(n-1)+function(n-2)
# for i in range(5):
#     print(function(i),end=" ")
    
#method 04:
#using dynamic programming Recursion top-bottom approach
n = 5
def function(n,dp):
    if n <= 1: return n
    if dp[n] != -1: return dp[n]
    dp[n] = function(n-1,dp) + function(n-2,dp)
    return dp[n]
dp = [-1]*(n + 1)
# for i in range(n):
#     print(function(i,dp),end=" ")
    
#method 05
#bottom - top approach
dp =[-1] * (n + 1)
dp[0],dp[1] = 0,1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
# print(*dp)

#climbing stairs:
# you can allowed to jump 1 or 2 steps
def  climbstairs(n):
    dp = [-1] * (n + 1)
    def function(n):
        if n <= 1: return 1
        elif dp[n] != -1: return dp[n]
        dp[n] = function(n -1) + function(n - 2)
        return dp[n]
    return function(n)
# print("The no of possible ways to climb stairs", climbstairs(5))

#Frog Jump
#Method 01
#min energy required to complete task
# Using recursion memoization top - bottom approach
arr = [30,10,60,10,60,50]
dp = [float("inf")] * (len(arr) + 1)
def frog_jump(n):
    if n == 0: return 0
    if dp[n] != float('inf'): return dp[n]
    left = frog_jump(n-1) + abs(arr[n-1] - arr[n])
    right = float("inf")
    if n > 1: right = frog_jump(n-2) + abs(arr[n-2] - arr[n])
    dp[n] = min(left,right)
    return dp[n]
# print(frog_jump(len(arr)-1))

#Method 02
#Tabulation
# bottom Up approach

dp = [0] * len(arr)
right = float("inf")
for i in range(1,len(arr)):
    left = dp[i-1] + abs(arr[i-1] - arr[i])
    if i > 1: right = dp[i-2] + abs(arr[i-2] - arr[i])
    dp[i] = min(left,right)
# print(dp[n])

# Method 03 without dp
first = secound = 0
for i in range(1,len(arr)):
     first = left + abs(arr[i-1] - arr[i])
     if i > 1: secound = right + abs(arr[i-2]-arr[i])
     left,right = left, min(first,secound)
# print(left)

# frog with k jumps:
# Method 01 Recursion sol 
# Time Complexcity O(N * K)
# Spac Complexcity O(1)
arr = [30,10,60,10,60,50]
k = 5
def function(n,k):
    if n == 0: return 0
    ministeps = float("inf") 
    for i in range(1,k+1):
        if n - i >= 0:
            ministeps = min(ministeps, (abs(arr[n - i]-arr[n]) + function(n-i,k)))
    return ministeps
# print(function(len(arr)-1,k))


#Method 02
#memoization
#Time Complexcity O(N * K)
#Space Complexcity O(N)

arr = [30,10,60,10,60,50]
k = 5
dp = [-1] * (len(arr) + 1)
dp[0] = 0
def function(n,k):
    if dp[n] != -1: return dp[n]
    minsteps = float("inf")
    for i in range(1,k+1):
        if n - i >= 0:
            minsteps = min(minsteps,abs(arr[n-i] - arr[n])+function(n-i,k))
    dp[n] = minsteps
    return dp[n]
# print(function(len(arr) - 1,k))




#House robber problem 
# Don't pick adjacent values  using recursion
# Time Complexcity O(2^n)
arr1 = [2,1,4,9]
arr1 = [1,2,3,1]
arr1 = [2,7,9,3,1]
n = len(arr1) - 1
if n == 0: print("array is empty")
def function(n):
    if n < 0: return 0
    right = arr1[n] + function(n - 2)
    left = function(n-1)
    return max(left,right)
# print(function(n))

arr1 = [2,1,4,9]
arr1 = [1,2,3,1]
arr1 = [2,7,9,3,1]

#TIME COMPLEXCITY O(N)
#Space Complexcity O(N)
dp =[-1] * (n + 1)
n = len(arr1)

def function(n):
    if  n < 0: return 0
    elif dp[n] != -1: return dp[n]
    left = arr1[n] + function(n - 2)
    right = function(n - 1)
    dp[n] = max(left,right)
    return dp[n]
# print(function(n - 1))

#Tabulation
def function(n):
    n = len(arr1)
    if n == 0: return 0 
    elif n == 1: return arr1[0]
    dp[0] = arr1[0]
    dp[1] = max(arr1[0],arr1[1])
    for i in range(2,len(arr1)):
        dp[i] = max(dp[i - 1],arr1[i] + dp[i - 2])
    print(dp[n - 1])
function(n)


# robber 02 problem
#Using Recursion
def Robber_02_recursion(n,arr):
    if n < 0: return 0
    return max(arr[n] + Robber_02_recursion(n - 2,arr) , Robber_02_recursion(n - 1,arr))

# using dp memo
def Robber_02_dp(n,arr,dp):
    if n < 0: return 0
    if dp[n] != -1: return dp[n]
    dp[n] = max(arr[n] + Robber_02_dp(n - 2,arr,dp) , Robber_02_dp(n - 1,arr,dp))
    return dp[n]

#Using Tabulation
def Robber_02_Tabulation(n,arr1):
    n = len(arr1)
    if n == 0: return 0 
    elif n == 1: return arr1[0]
    dp[0] = arr1[0]
    dp[1] = max(arr1[0],arr1[1])
    for i in range(2,len(arr1)):
        dp[i] = max(dp[i - 1],arr1[i] + dp[i - 2])
    return dp[n - 1]

    
arr =[2,3,2]
temp1 = arr[1:]
temp2 = arr[:-1]

print(max(Robber_02_recursion(len(temp1) - 1,temp1),Robber_02_recursion(len(temp2) - 1,temp2)))
print(max(Robber_02_dp(len(temp1) - 1,temp1,[-1] * (len(temp1)+1)),Robber_02_dp(len(temp2) - 1,temp2,[-1] * (len(temp1)+1))))
print(max(Robber_02_Tabulation(len(temp1)- 1,temp1),Robber_02_recursion(len(temp2)-1,temp2)))




