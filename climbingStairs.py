# Recursion
n = 3
def climb_stairs(n):
    if n == 0 : return 1 
    elif n < 0 : return 0
    else: return climb_stairs(n - 1) + climb_stairs(n -  2)
# print(climb_stairs(n))

# memoization
dp = [-1] * (n + 1)
def climb_stairs(n):
    if n == 0 : return 1 
    elif n < 0 : return 0
    elif dp[n] != -1: return dp[n]
    else: return climb_stairs(n - 1) + climb_stairs(n -  2)
# print(climb_stairs(n))

# Tabulation
dp = [1 ,2] + [-1] * (n)
for i in range(2,n+1):
    dp[i] = dp[i - 1] + dp[i -2]
# print(dp[n-1])
