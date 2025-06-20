#Stacks

# Asteroid Collision
#Time Complexcity O(n)
#Space Complexcity O(n)
asteroids = [5,10,-5]
stack = []
for i in asteroids:
    if i > 0:stack.append(i)
    else:
        while stack and 0 < stack[-1] < abs(i):
            stack.pop()
        if stack and stack[-1] == abs(i):
            stack.pop()
        elif not stack or stack[-1] < 0:
            stack.append(i)
        
# print(stack)     

# Minimum Remove to Make Valid Parentheses
#Time Complexcity O(4n) ~ O(n)
#Space Complexcity O(1)
s = "lee(t(c)o)de)"
par = 0 
s = list(s)
for i in range(len(s)):
    if s[i] == "(": par+=1
    elif s[i] == ')':
        if not par: s[i] = "*" 
        else: par-=1
for i in range(len(s)-1,-1,-1):
    if par > 0 and s[i] == '(':
        par-=1
        s[i] = "*"
# print(''.join([i for i in s if i !="*"]))

# Simplify Path
#Time complexcity O(n)
#Space Complexcity O(1)
path = "/home/"

stack = []
path = path.split('/')
for i in path:
    if i == '' or i == '.' : continue
    elif i == "..": 
        if stack: stack.pop()
    else:stack.append(i)
ans = '/'+ '/'.join(stack)
# print(ans)


#Minimum Bit Flips to Convert Number
#Time Complexcity O(1)
#Space Complexcity O(1)
start = 10
goal = 7
xor = start ^ goal
count = 0
while xor:
    xor &= xor-1
    count+=1
# print(count)

#Time Complexcity O(1)
#Space Complexcity O(1)
#left shift
start = 10
goal = 7
shift = 1
count = 0
for _ in range(32):
    if start & shift != goal & shift:
        count+=1
    shift = shift << 1
# print(count)


#Right shift
#Time Complexcity O(1)
#Space Complexcity O(1)
start = 10
goal = 7
count = 0
while start or goal:
    if start & 1 != goal & 1:
        count+=1
    start = start >> 1
    goal = goal >> 1
print(count)



#Generate subsets
#Time Complexcity O(n * 2 ^ n) ~ O(n)
#Space Complexcity O(n)
nums = [1,2,3]
subsets = 1 << len(nums)
ans = []
for i in range(subsets):
    arr = []
    for j in range(len(nums)):
        if i & (1 << j): arr.append(nums[j])
    ans.append(arr)
# print(ans)
    
# Pow(x, n)
x = 2.00000
n = 10
m = n
ans = 1
while m > 0:
    if m & 1:
        m -=1
        ans *=x
    else:
        m//=2
        x *= x
# print(ans)    
        
# Counting Bits
#Time COmplexcity O(n)
#Space Complexcuty O(1)
n = 2
ans = []
for i in range(n+1):
    count = 0
    while i:
        count+=1
        i = i& (i -1)
    ans.append(count)
# print(ans)

#Time Complexcity O(n)
#Space Complexcuty O(n)
n = 5
dp =[-1] * (n + 1)
dp[0],dp[1] = 0,1
for i in range(2,n+1):
    dp[i] = dp[i//2] + 1 if i & 1 else dp[i//2]
print(dp[n])
    

        
        
    
    
        
 

    
    