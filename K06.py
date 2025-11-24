m = n = 5
hurdles = {(3,1),(3,2)}

def find(i,j):
    if i == 1 and j == 1:
        return 1
    if i < 1  or j < 1 or (i,j) in hurdles:
        return 0
    return  find(i-1,j) + find(i,j - 1)
print(find(m,n))
        

dp = dict()

def find(i,j):
    if i == 1 and j == 1:
        return 1
    if i < 1  or j < 1 or (i,j) in hurdles:
        return 0
    if (i,j) in dp:
        return dp[i,j]
    dp[i,j] =  find(i-1,j) + find(i,j - 1)
    return dp[i,j]
print(find(m,n))

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = 1 
        elif (i-1,j - 1) in hurdles:
            continue
        else:
            left = dp[i - 1][j] if i - 1  >= 0 else 0
            right = dp[i][j - 1]  if j - 1 >= 0 else 0
            dp[i][j] = left + right 
print(dp)
print(dp[-1][-1])
        
        
        
temp = [0] * m
for i in range(m):  
    arr = [0] * n
    for j in range(n):
        if i == 0 and j == 0:
            arr[j] = 1
        elif (i - 1,j - 1) in hurdles:
            continue
        else:
            left = temp[j] if i - 1  >= 0 else 0
            right = arr[j - 1]  if j - 1 >= 0 else 0
            arr[j] = left + right
    temp = arr[:]
print(temp[-1])
        
    
m,n = 5,6
forest = [
    ['T','T','T','T','T','.'],
    ['T','.','T','.','.','.'],
    ['T','.','T','T','T','T'],
    ['.','.','T','.','.','.'],
    ['T','T','T','T','T','T']
]

count_tree = 0
for i in range(m):
    for j in range(n):
        if forest[i][j] == 'T':
            count_tree +=1

count =  [0]
def dfs(i,j,fire):
    if i < 0 or j < 0 or i >= m or j>=n or forest[i][j] == '.':
        return  0 
    forest[i][j] = '.'
    count[0] = max(count[0],fire)
    return  1 + dfs(i + 1,j,fire + 1) + dfs(i - 1,j,fire + 1) + dfs(i ,j - 1,fire + 1) + dfs(i ,j + 1,fire + 1)

print(count_tree - dfs(2,5,0))
print(count[0])
    
        