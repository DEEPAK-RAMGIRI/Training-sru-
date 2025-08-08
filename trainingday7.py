#=========================================== Climbing Stairs =======================================================
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

# Space Optimization
prev1,prev2 = 1,2
for i in range(n-1):
    prev1,prev2 = prev2,prev1+prev2
# print(prev1)

# ============================================ House Robber =========================================================
nums = [1,2,3,1]

# recursion
def rob_house(index):
    if index < 0: return 0
    consecutive = nums[index] + rob_house(index-2)
    no_consecutive = rob_house(index - 1)
    return max(consecutive,no_consecutive)
# print(rob_house(len(nums)-1))

# memoization
dp = [-1] * len(nums)
def rob_house(index):
    if index < 0: 
        return 0
    elif dp[index] != -1:
        return dp[index]
    consecutive = nums[index] + rob_house(index-2)
    no_consecutive = rob_house(index - 1)
    dp[index] = max(consecutive,no_consecutive)
    return  dp[index]
# print(rob_house(len(nums)-1))
    
    
# tabulation
dp = [-1] * (len(nums))
dp[0] = nums[0]
dp[1] = max(nums[0],nums[1])
for i in range(2,(len(nums))):
    dp[i] = max(dp[i -2] + nums[i],dp[i-1])
# print(dp)
# print(dp[len(nums)-1])

#============================================ Unique Paths =========================================================
n = 3
m = 7
# recursion
def no_of_unique_paths(i,j):
    if i == 0 and j == 0: return 1
    elif i<0 or j <0: return 0
    up =no_of_unique_paths(i-1,j)
    left = no_of_unique_paths(i,j-1)
    return up + left
# print(no_of_unique_paths(n-1,m-1))    

# memoization
dp = [ [-1 for _ in range(m)] for _ in range(n)]
def no_of_unique_paths(i,j):
    if i == 0 and j == 0:
        return 1
    elif i < 0 or j< 0:
        return 0
    elif dp[i][j] != -1: return dp[i][j] 
    up = no_of_unique_paths(i-1,j)
    left = no_of_unique_paths(i,j-1)
    dp[i][j] = up + left
    return dp[i][j]
# print(no_of_unique_paths(n-1,m-1))

#tabulation
dp = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = 1
        else:
            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j - 1] if j > 0 else 0
            dp[i][j] = left + up
        
# print(dp[n-1][m-1])
        
# ============================================ Minimum Path Sums =========================================================
grid = [[1,3,1],[1,5,1],[4,2,1]]

# recursion
def find_min_sum(i,j):
    if i == 0 and j == 0:
        return grid[i][j]
    elif i < 0 or j < 0:
        return float("inf")
    upside = find_min_sum(i - 1,j)
    leftside = find_min_sum(i,j - 1)
    return min(upside,leftside) + grid[i][j]
# print(find_min_sum(len(grid)-1,len(grid[0])-1))

# memoization
dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
def find_min_sum(i,j):
    if i == 0 and j == 0:
        return grid[i][j]
    elif i < 0 or j < 0:
        return float("inf")
    elif dp[i][j] != -1:
        return dp[i][j]
    upside = find_min_sum(i - 1,j)
    leftside = find_min_sum(i,j - 1)
    dp[i][j] = min(upside,leftside) + grid[i][j]
    return dp[i][j]
# print(find_min_sum(len(grid)-1,len(grid[0])-1))

# tabulation
dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        else:
            upside = dp[i-1][j] if i > 0 else float("inf") 
            leftside = dp[i][j-1] if j > 0 else float("inf")
            dp[i][j] = min(upside,leftside) + grid[i][j]
# print(dp[len(grid)-1][len(grid[0])-1])

# ============================================ Decode Ways ======================================================

# Recursion
string = '226' 
def decodeways(index):
    if index == len(string): return 1
    elif string[index] == "0":return 0
    total = decodeways(index + 1)
    if index + 1 < len(string) and 10 <= int(string[index:  index + 2]) <= 26:
        total += decodeways(index + 2)
    return total 
# print(decodeways(0))

# memoization
dp = [-1] * len(string)
def decodeways(index):
    if index == len(string): return 1
    elif string[index] == '0':return 0
    elif dp[index] != -1:
        return dp[index]
    dp[index] = decodeways(index + 1)
    if index + 1 < len(string) and 10 <= int(string[index : index + 2]) <= 26:
        dp[index] += decodeways(index + 2)
    return dp[index]
# print(decodeways(0))

# tabulation
dp = [-1] * (len(string) + 1)
dp[-1] = 1
for i in range(len(string)-1,-1,-1):
    if string[i] == '0': dp[i] = 0
    else:
        dp[i] = dp[i+1]
        if i + 1 < len(string) and  10 <= int(string[i :i + 2]) <= 26:
            dp[i] += dp[i + 2]
# print(dp[0])

# =================================== Longest Common Subsequences =================================================
text1 = "abcde"
text2 = "ace" 

# Recursion
def longest_common_subsequence(i,j):
    
    if i < 0 or j < 0: return 0
    elif text1[i] == text2[j]: return 1 + longest_common_subsequence(i-1,j-1)
    else: return max(longest_common_subsequence(i-1,j),longest_common_subsequence(i,j-1))
    
# print(longest_common_subsequence(len(text1)-1,len(text2)-1))

# memoization
dp = [[-1 for _ in range(len(text1))] for _ in range(len(text2))]
def longest_common_subsequence(i,j):
    if i < 0 or j < 0: return 0
    elif dp[i][j] != -1: 
        return dp[i][j]
    elif text2[i] == text1[j]: return 1 + longest_common_subsequence(i-1,j-1)

    from_left_side = longest_common_subsequence(i,j-1)
    from_top_side = longest_common_subsequence(i-1,j)
    dp[i][j] = max(from_left_side,from_top_side)
    return dp[i][j]
# print(longest_common_subsequence(len(text2)-1,len(text1)-1))

#tabulation
dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
for i in range(len(text1)):
    for j in range(len(text2)):
        
        if text1[i] == text2[j]:
            if i > 0 and j > 0:
                dp[i][j] = 1 + dp[i - 1][j -1]
            else:
                dp[i][j] = 1 
        else:
            left_side = dp[i][j-1] if j > 0  else 0
            top_side = dp[i-1][j] if i > 0 else 0
            dp[i][j] = max(left_side,top_side) 
            
# print(dp[len(text1)-1][len(text2)-1])

# ========================================== Longest Increasing Subsequence ==========================================

# generate subsequence with the given array
arr = [10,9,2,5,3,7,101,18]
ans = []
def generate_subsequence(index,temp):
    if index  == len(arr):
        ans.append(temp[:])
        return
    
    generate_subsequence(index + 1,temp)
    
    if not temp or temp[-1] < arr[index]:
        temp.append(arr[index])
        generate_subsequence(index + 1,temp)
        temp.pop()
    
    
# generate_subsequence(0,[])
# print(ans)  

#  Longest Increasing Subsequence

# recursion   
def generate_subsequence(index,prev):
    if index == len(arr):
        return 0
    with_ = generate_subsequence(index+1,prev)
    with_out = 0
    if prev == -1 or arr[prev] < arr[index]:
        with_out  = 1  + generate_subsequence(index+1,index)
    return max(with_ ,  with_out)
print(generate_subsequence(0,-1))

# Memoization
dp = [[-1 for _ in range(len(arr) + 1)] for i in range(len(arr))]

def generate_subsequence(index,prev_index):
    if index == len(arr): return 0
    elif dp[index][prev_index + 1] != -1: return dp[index][prev_index + 1]
    with_ = generate_subsequence(index + 1,prev_index)
    with_out = 0
    if prev_index == -1 or arr[prev_index] < arr[index]:
        with_out  = 1 + generate_subsequence(index + 1,index)
    dp[index][prev_index] = max(with_,with_out)
    return dp[index][prev_index]
# print(generate_subsequence(0,-1))

dp = [1] * len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j] + 1)
# print(max(dp))  
        
        
        
    
        
      