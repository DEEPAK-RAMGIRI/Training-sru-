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

nums = [1,5,11,5]
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



# TimeComplexcity = O(n × T)  
# SpaceComplexcity = O(n × T)

def partition(nums):
    total = sum(nums)
    if total & 1 == 1:
        return False
    target = (total >> 1)
    dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums))] 
    def dfs(index,temp):
        if temp == 0: return True
        elif index < 0 or temp < 0: return False
        elif dp[index][temp] != -1: return dp[index][temp]
        dp[index][temp] =  dfs(index-1,temp-nums[index]) or dfs(index - 1,temp)
        return dp[index][temp]
    return dfs(len(nums)-1,target)
# print(partition(nums))


# tabilation 
# maybe not right now may be in future 😊👍        
nums = [1,5,11,5] 

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


# =================================================== House Robber ======================================================================
# Time complexcity O(2 ^n)
# space complexcity O(n)
nums = [1,2,3,1]
def house_robber(index):
    if index < 0: return 0 
    normal = house_robber(index - 1)
    cons = nums[index] + house_robber(index - 2)
    return max(normal,cons)
# print(house_robber(len(nums) - 1))


# Time complexcity O(n)
# space complexcity O(n)
dp = [-1] * (len(nums) + 1)
def house_robber(index):
    if index < 0: return 0
    elif dp[index] != -1: return dp[index]
    normal = house_robber(index - 1)
    cons = nums[index] + house_robber(index - 2)
    return max(normal,cons)
# print(house_robber(len(nums) -1))

dp = [nums[0],max(nums[0],nums[1])] + [-1] * (len(nums) - 2)
for i in range(2,len(nums)):
    dp[i] = max(dp[i-1],dp[i - 2 ] + nums[i])
# print(dp[-1])

# =================================================== House Robber II ====================================================================
# Recursion
# Time Complexcity O( 2 ^ n)
# Space Complexcity O(n)
nums = [1,2,3,1]
def houses(nums):
    def robberII(index):
        if index < 0:
            return 0
        return max(robberII(index - 1),robberII(index - 2) + nums[index])
    return robberII(len(nums) -1)
# print(max(houses(nums[1:],houses[:-1])))


# Memoization
# Time complexcity O(n)
# Space complexcity O(n)

dp = [-1] * (len(nums) + 1)
def  houses(nums):
    def robberII(index):
        if index < 0:
            return 0
        elif dp[index] != -1: return  dp[index]
        dp[index] = max(robberII(index - 1),robberII(index - 2) + nums[index])
        return dp[index]

    return (robberII(len(nums) - 1))   
# print(max(houses(nums[1:]),houses(nums[:-1])))


# Tabulation
# Time Complexcity O(n)
# Space Complexcity O(n)
def rob(self, nums):
    if len(nums) == 1: return nums[0]
    def houses(nums):
        if len(nums) == 1: return nums[0]
        dp = [nums[0],max(nums[0],nums[1])] + [-1] * (len(nums) - 1)
        for i in range(2,len(nums)):
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i])
        return dp[len(nums)-1]
    
    return max(houses(nums[1:]),houses(nums[:-1]))
        
# Space Optimization
def rob(nums):
    if len(nums) == 1: return nums[0]
    def houses(nums):
        if len(nums) == 1: return nums[0]
        prev,prev1 = nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            prev,prev1 = prev1,prev + nums[i] 
        # print(prev1,prev)
        return prev1
    
    return max(houses(nums[1:]),houses(nums[:-1]))
# print(rob(nums))
    


# =================================================== Longest Increasing Subsequence ===============================

nums = [10,9,2,5,3,7,101,18]


# Recursion
# Time Complexcity O(2 ^ m)
# Space Complexcity (n)
def lis(index,prev):
    if index == len(nums):
        return 0
    with_out = lis(index+1,prev)
    withvalue = 0
    if prev == -1 or nums[prev] < nums[index]:
        withvalue = 1 + lis(index+1,index)
    return max(withvalue,with_out)
# print(lis(0,-1))

# memoization
# Time Complexcity O(n ^ 2)
# Space Complexcity O(n ^ 2)
dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
def lis(index,prev):
    if index == len(nums):
        return 0
    elif dp[index][prev] != -1: return dp[index][prev]
    with_out = lis(index + 1,prev)
    withvalue = 0
    if prev == -1 or nums[prev] < nums[index]:
        withvalue = 1 + lis(index + 1,index)
    dp[index][prev] = max(withvalue,with_out)
    return dp[index][prev]
# print(lis(0,-1))

# tabuation
dp = [1] * len(nums)
for i in range(len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[j] = max(dp[i],dp[j] + 1)
# print(max(dp))
    
# =================================================== Longest Common Subsequence ===================================
text1 = "abcde"
text2 = "ace" 

# recursion
# Time Complexcity O( 2^n)
# Space complexcity O(n)
def lcs(i,j):
    if i < 0 or j < 0: return 0
    if text1[i] == text2[j]:
        return 1 + lcs(i-1,j-1)
    return max(lcs(i-1,j) , lcs(i,j-1))
# print(lcs(len(text1)-1,len(text2) -1))

dp = [[-1 for _ in range(len(text1)+1) ] for _ in range(len(text2)+1)]

# Memoization
# Time Complexcity O(m*n)
# Space Complexcity O(m*n)
def lcs(i,j):
    if i < 0 or j < 0: return 0
    elif text1[i] == text2[j]:
        return 1 + lcs(i - 1,j - 1)
    elif dp[i][j] != -1: return dp[i][j]
    dp[i][j] = max(lcs(i-1,j), lcs(i,j-1))
    return dp[i][j]    
# print(lcs(len(text1)-1,len(text2) -1))


# Tabulation
# Time Complexcity O(m*n)
# Space Complexcity O(m*n)
dp = [[-1 for _ in range(len(text2))]for _ in range(len(text1))]

for i in range(len(text1)):
    for j in range(len(text2)):
            if text1[i] == text2[j]:
                if i > 0 and j > 0:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 
            else:
                 dp[i][j] = max(dp[i-1][j] if i > 0 else 0 , dp[i][j-1] if j > 0 else 0)
# print(dp[len(text1) - 1][len(text2) - 1])



text1 = "abcde"
text2 = "ace"   
# Space optimization
# Time Complexcity O(m *n)
# Space Complexcity O(m)
prev = [0] * len(text2)
for i in range(len(text1)):
    curr = [0] * len(text2)
    for j in range(len(text2)):
        if text1[i] == text2[j]:
            if j > 0:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = 1
        else:
            curr[j] = max(prev[j],curr[j - 1] if j > 0 else 0 ) 
    prev = curr
# print(curr[-1]) 

# ============================================ Cutting Rod ========================================================
# ❓❓❓ rod cutting problem ❓❓❓
# Time complexcity O(2 ^ n)
# Space Complexcity O(n)
prices  = [2,5,7,8,10]
def max_price(index,n):
    if index == 0: return prices[0] * n
    not_cut = max_price(index - 1,n)
    length = index + 1
    cut = float("-inf")
    if length <= n:
        cut = prices[index] + max_price(index,n - length)
    return max(cut,not_cut)
# print(max_price(len(prices)-1,len(prices)))

# Time complexcity O(m * n)
# Space complexcity O(m * n)

dp = [[-1 for _ in range(len(prices)+1)] for _ in range(len(prices))]
def max_prices(index,n):
    if index == 0: return prices[0] * n
    elif dp[index][n] != -1: return dp[index][n]
    not_cut = max_prices(index - 1,n)
    length = index + 1
    cut = float("-inf")
    if length <= n:
        cut = prices[index] + max_prices(index,n - length)
    dp[index][n] = max(cut,not_cut)
    return dp[index][n]
# print(max_prices(len(prices)-1,len(prices)))

    

# ============================================ Unbound KnapSack ===================================================
# ============================================ Edit distance ======================================================

# edit distance
# Time Complexcity O(3 ^ (m + n))
# Space Complexcity O( m + n)
word1 = "horse"
word2 = "ros"
def edit_distance(i,j):
    if i < 0: return j+1
    if j < 0: return i+1
    elif word1[i] == word2[j]:
        return edit_distance(i-1,j-1)
    else:
        return 1 + min(edit_distance(i,j-1), # insert
                       edit_distance(i-1,j-1), # replace
                       edit_distance(i-1,j) # delete
                       )
# print(edit_distance(len(word1)-1,len(word2)-1))

# Time Complexcity O(n * m)
# space complexcity O(n *  m)
dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
def edit_distance(i,j):
    if i < 0 : return j + 1
    if j < 0 : return i + 1
    elif dp[i][j] != -1: return dp[i][j]
    elif word1[i] == word2[j]:
        return 0 + edit_distance(i-1,j-1)
    dp[i][j] = 1 + min(edit_distance(i-1,j),edit_distance(i,j-1),edit_distance(i-1,j-1))
    return dp[i][j]
# print(edit_distance(len(word1)-1,len(word2)-1))

# Time Complexcity O(m * n)
# Space Complexcity O(m * n)

dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1)+1)]
def function(word1,word2):
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j

    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j - 1],dp[i-1][j-1])
    return dp[len(word1)][len(word2)]


# Time Complexcity O(m * n)
# Space Complexcity O(n)


# ============================================ vertex Cover =======================================================
# ============================================ matrix Multiplication ==============================================

arr = [1, 2, 3, 4, 3]
# Recursion
# Time Complexcity O(2 ^ n) * O(n)
# Space Complexcity O(2 ^ n)
def mcm(i,j):
    if i == j:
        return 0
    maxi = float("inf")
    for k in range(i,j):
        maxi = min(arr[i-1] * arr[j] * arr[k] + mcm(i,k)+mcm(k+1,j),maxi)
    return maxi
# print(mcm(1,len(arr)-1))


# using dp
# Memoization
# Time Complexcity O(n * n * n)
# Space ComplexcityO(n * n)
dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]

for i in range(len(arr)):
    dp[i][i] = 0
    
def mcm(i,j):
    if i == j:
        return 0
    elif dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = float("inf")
    for k in range(i,j):
        dp[i][j] = min(dp[i][j], arr[i - 1] * arr[k] * arr[j] + mcm(i,k) + mcm(k+1,j))
    return dp[i][j]
# print(mcm(1,len(arr) - 1))
# ============================================ Palindrome Partition ===============================================  
                
                
                
                 
                    
                    
            
    


