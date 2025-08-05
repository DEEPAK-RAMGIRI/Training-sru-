# ====================================================== fibanacci ================================================

# Time Complexcity O(2 ^ n)
# Space Complexcity  O(h)
n = 5
def fibancci(n):
    if n <= 1: return n
    else: return fibancci(n - 1) + fibancci(n - 2)
# print(fibancci(n))

# Memoization
# Time Complexcity O(n)
# space complexcity O(n)
dp = [-1] * (n + 1)
def fibancci(n):
    if n <= 1: return n
    elif dp[n] != -1:
        return dp[n]
    dp[n] = fibancci(n - 1) + fibancci(n - 2)
    return dp[n]
# print(fibancci(n))

# Tabulation
# Time Complexcity O(n)
# Space Complexcity O(n)
dp = [0,1] + [-1] * (n-1)
for i in range(2,n+1):
    dp[i] = dp[i - 1] + dp[i - 2]
# print(dp[n])
     
# Space optimization
# Time Complexcity O(n)
# Space Complexcity O(1)
prev,prev1 = 1,0
for i in range(n-1):
    prev,prev1 = prev1 + prev,prev
# print(prev)

#-------------------------------------------------------MIN/MAX SUM-----------------------------------------------
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

n = len(grid)
m = len(grid[0])

# Recursion
# Time complexcity O(2 ^ (m + n))
# Space Complexcity O(m + n)

def mini_path_sum(i,j):
    if i == 0 and j == 0: return grid[i][j]
    if i < 0 or j < 0 : return float("inf")
    up = mini_path_sum(i-1,j)
    right = mini_path_sum(i,j-1)
    return grid[i][j] + min(up,right)

# print(mini_path_sum(m-1,n-1))

# Memoization
# Time Complexcity O(m * n)
# space Complexcity O(m * n)
dp = [[-1 for _ in range(m)] for _ in range(n)]
def  mini_path_sum(i,j):
    if not i and not j: return grid[i][j]
    if i < 0 or j < 0: return float("inf")
    up = mini_path_sum(i-1,j)
    down = mini_path_sum(i,j - 1)
    dp[i][j] = grid[i][j] + min(up,down)
    return dp[i][j]
# print(mini_path_sum(m-1,n-1))


# Tabulation
# Time Complexcity O( m * n)
# Space Complexcity O(m * n) + O(h)
 
def mini_path_sum(m,n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not i and not j: dp[i][j] = grid[i][j]
            else:
                up = dp[i - 1][j] if i > 0 else float("inf")
                right= dp[i][j - 1] if j > 0 else float("inf")
                dp[i][j] = grid[i][j] + min(up,right)
    return dp[m - 1][n - 1]
# print(mini_path_sum(m,n))
                
                
# Space Optimization 
# Time  Complexcity O(m * n)
# Space Complexcity O(n) 
def mini_path_sum(m,n):
    up = [0] * n
    for i in range(m):
        left = [0] * n
        for j in range(n):
            if i == 0 and j == 0: left[0] = grid[i][j]
            else:
                up_side = up[j] if i > 0 else float("inf")
                left_side = left[j - 1] if j > 0 else float("inf")
                left[j] = grid[i][j] + min(up_side,left_side)
        up = left
    return left[n - 1]
# print(mini_path_sum(m,n))
            
#======================================= Maximum path sum ======================================================

grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]


# Recursion
# Time complexcity O(2 ^ (m + n))
# Space Complexcity O(m + n)
def maximum_path_sum(i,j):
    if i == 0 and j == 0: return grid[i][j]
    elif i < 0 or j < 0 : return float("-inf")
    up = maximum_path_sum(i-1,j)
    left = maximum_path_sum(i,j-1)
    return grid[i][j] + max(left,up)
# print(maximum_path_sum(m-1,n-1)) 


# Memoization 
# Time Complexcity O(m + n)
# Space complexcity O(m + n) 
dp = [[-1 for _ in range(m)] for _ in range(n)]
def maximum_path_sum(i,j):
    if i == 0 and j == 0: return grid[i][j]
    elif i < 0 or j < 0: return float("-inf")
    elif dp[i][j] != -1: return dp[i][j]
    up = maximum_path_sum(i - 1,j)
    left = maximum_path_sum(i,j-1)
    dp[i][j] = max(up,left) + grid[i][j]
    return dp[i][j]
# print(maximum_path_sum(m-1,n-1))

# Tabulation
dp = [[-1 for _ in range(m)] for _ in range(n)]
def maximum_path_sum(m,n):
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0: dp[i][j] = grid[i][j]
            else:
                up = dp[i - 1][j] if i > 0 else float("-inf")
                left = dp[i][j - 1] if j > 0 else float("-inf")
                dp[i][j] = max(left,up) + grid[i][j]
    return dp[m - 1][n - 1]
# print(maximum_path_sum(m,n))

# Space Optimization
# Time Complexcity O(m+n)
# Space complexcity O(n)

def maximum_path_sum(m,n):
    upside = []
    for i in range(m):
        leftside = [0] * n
        for j in range(n):
            if i == 0 and j == 0: 
                leftside[j] = grid[i][j]
            else:
                up = upside[j] if i > 0 else float("-inf")
                left = leftside[j - 1] if j > 0 else float("-inf")
                leftside[j] = max(left,up) + grid[i][j]
        upside = leftside
            
    return leftside[m - 1]
# print(maximum_path_sum(m,n))
                
#======================================== CLIMBING STAIRS ========================================================
# Recursion
# Time Complexcity O(2 ^ n)
# Space Complexcity O(n) (Stack Space)
n = 3
def climbing_stairs(n):
    if n == 0: return 1
    elif n < 0 :return 0
    else: return climbing_stairs(n - 1) + climbing_stairs(n - 2)
# print(climbing_stairs(n))


# Memoization
# Time Complexcity O(n)
# Space Complexcity O(n)
n = 5
dp = [-1] * n
def Climbing_Stairs(n):
    if n == 0: return 1
    elif n < 0: return 0
    elif dp[i] != -1: return dp[i]
    dp[i] = climbing_stairs(n -1 ) + climbing_stairs(n - 2)
    return dp[i]
# print(Climbing_Stairs(n))


# Tabulation
# Time Complexcity O(n)
# Space Complexcity O(n)
def Climbing_Stairs(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Space Optimization    
# Time Complexcity O(n)
# Space Complexcity O(1)
prev,prev1 = 1,0
for i in range(n-1):
    prev,prev1 = prev1 + prev,prev
# print(prev)

#=================================================== PARTITION PROBLEMS  ==========================================
# Recursion 
# Time Complexcity O(2 ^ (n))
# Space Complexcity O(n)

def partion(nums):
    total = sum(nums)
    if total & 1: return False
    target = total >> 1
    def dfs(index,temp):
        if temp == 0: return True  
        elif temp < 0 or index < 0: return False
        else: return dfs(index-1,temp-nums[index]) or dfs(index-1,temp)
    return dfs(len(nums)-1,target)
    
# print(partion([1,5,11,5]))
#=================================================== Coin change ==================================================

# Recursion
# Time Complexcity O(2 ^ n)
# Space Complexcity O(n)
coins = [2,5]
amount = 11
def coin_change(amount,index):
    if amount == 0: return 0
    if index < 0 or amount  < 0:
        return float("inf")
    include =  1 + coin_change(amount-coins[index],index)
    dont_include = coin_change(amount,index - 1)
    return min(include,dont_include)
# print(coin_change(amount,len(coins)- 1))

# Memoization
# Time Complexcity O(n)
# Space Complexcity O(n)
dp = [[-1 for _ in range(amount + 1)]for _ in range(len(coins))]
def coin_change(amount,index):
    if amount == 0:return 0 
    elif amount < 0 or index < 0:return float("inf")
    elif dp[index][amount] != -1: return dp[index][amount]
    include = 1+ coin_change(amount-coins[index],index)
    dont_include = coin_change(amount,index-1)
    dp[index][amount] = min(include,dont_include)
    return dp[index][amount]
# print(coin_change(amount,len(coins)-1))




    
    