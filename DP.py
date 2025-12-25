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
        for j in range(bag):
            dp[i][j] = dp[i + 1][j]
            if j + wt[i] <= bag:
                dp[i][j]  = max(dp[i][j],pt[i] + dp[i + 1][j + wt[i]])
    print(dp[0][0])        
tabulation()  


def memory_optimization():
    dp = [0] * (bag + 1)

    for i in range(len(wt)):
        for j in range(bag, wt[i] - 1, -1):
            dp[j] = max(dp[j], pt[i] + dp[j - wt[i]])

    print(dp[bag])
    