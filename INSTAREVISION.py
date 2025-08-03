# fibanacci 
# Time Complexcity O(2 ^ n)
# Space Complexcity + O(h)
n = 5
def fibancci(n):
    if n <= 1: return n
    else: return fibancci(n - 1) + fibancci(n - 2)
# print(fibancci(n))

#memozition
# Time Complexcity O(n)
# space complexcity O(h)
dp = [-1] * (n + 1)
def fibancci(n):
    if n <= 1: return n
    elif dp[n] != -1:
        return dp[n]
    dp[n] = fibancci(n - 1) + fibancci(n - 2)
    return dp[n]
# print(fibancci(n))


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



# Time Complexcity O( m * n)
# Space Complexcity O(m * n)
 
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
                
                
                
def mini_path_sum(m,n):
    for i in range(m):
        for j in range(n):
            pass
            
    
# CLIMBING STAIRS
# Time Complexcity O(2 ^ n)
# Space Complexcity O(n) (Stack Space)
n = 3
def climbing_stairs(n):
    if n == 0: return 1
    elif n < 0 :return 0
    else: return climbing_stairs(n - 1) + climbing_stairs(n - 2)
    
# print(climbing_stairs(n))


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


    
# PARTITION PROBLEMS 
# Coin change
    
    


    
    
    