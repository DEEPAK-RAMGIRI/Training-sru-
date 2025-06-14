# prime no
#Time Complexcity O(root(n))
#Space Complexcity O(1)
n = 10
for i in range(2,int(n ** 0.5)+1):
    if not n % i:
        print("not prime")
        break
else:print("prime no")

#Time Complexcity O(n^2)
#Space Complexcity O(n)

prime = [True] * (n + 1)
prime[0] = prime[1] = False
for i in range(2,len(prime)):
    if prime[i]:
        for j in range(2*i,len(prime),i):
            prime[j] = False
print(prime[n])



#prime factors
#Time Complexcity O(root(n))
#Space Complexcity O(1)
ans=[]
for i in range(2,int(n**0.5)+1):
    while not n % i:
        ans.append(i)
        n//=i
if n > 1: ans.append(n)
print("prime factors", ans)

#Time Complexcity O(n^0.5)
#Space Complexcity O(1)
arr = [8,2,3,4,3,3,4,5,6,7,9,2,4]
sets = set()
for i in arr:
    if i not in sets:
        sets.add(i)
print(sets)


# find Xor of first n values
n=10
xor = 0
for i in range(n+1):
    xor ^= i
print(xor)
#Time Complexcity O(n)
#Space Complexcity O(1)

#xor values 


def function(n):
    if n % 4  == 1: return 1
    elif n % 4 == 2: return n + 1
    elif n % 4 == 3: return 0
    else: return n
print(function(10))
    
    
    
# To find xor betweeen 5^.....^10

print(function(10) ^ function(4))



#count no occurenece of string
#Time Complexcity O(n)
#Space Complexcity O(1)
string = "aaabbaaaacccddeff"
string="abbacbababc"
j = 0
for i in range(1,len(string)):
    if string[i] != string[i-1]:
        print(string[i - 1],i - j,end=" ")
        j = i
print(string[i],len(string)- j)



#print even number
#Time Complexcity O(n)
a = [2,5,6,7,2,1,4,3,6]
def function(i,ans):
    if i >= len(a):
        return ans
    return function(i+1,ans+a[i] if not a[i] & 1 else ans)
print("answer",function(0,0))  

#counting min no of count to get 1 aif we subtract 3 or 5 iteratively


# Time Complexcity O(n ^ 2) bcoz we iterating  for n - 3 and n -5
#Space Complexcity O(n) #because of stack size
def trueorfalse(n):
    if n == 1: return 0
    elif n <= 0: return float("inf")
    else: return min(1+trueorfalse(n - 3), 1+trueorfalse(n - 5))

print("True or False",trueorfalse(10))


#using Dp 
#memoization
# Time Complexcity O(n)
# Space Complexcity O(n)
n = 10
dp = [-1] * (n+1)
def trueorfalse(n):
    if n == 1: return 0
    elif n <= 0: return float("inf")
    elif dp[n] != -1: return dp[n]
    else: dp[n] = min(1 + trueorfalse(n - 3) , 1 + trueorfalse(n - 5))
    return dp[n]
# print(trueorfalse(n))


#tabulation
n = 10
dp = [float("inf")] * (n + 1)
dp[1] = 0
for i in range(2,n+1):
    if i - 3 >= 1: dp[i] =min(dp[i],1 + dp[i-3])
    if i - 5 >= 1: dp[i] = min(dp[i],dp[i - 5] + 1)
# print(dp[n])


#now print the values of above question to reach the 1
ans = []
def function(n,arr = []):
    if n == 1: 
        arr.append(n)
        ans.append(arr)
    elif n < 1: return
    function(n-3,arr+[n])
    function(n-5,arr+[n])
print(function(10))
print(ans)

        
        
list1 = [
    [1,0,0,1,1],
    [1,0,0,0,1],
    [0,1,0,0,0],
    [1,0,0,1,0],
    [1,0,0,0,1]
]

def island(i,j):
    if i < 0 or i>= len(list1) or j < 0 or j >= len(list1[0]) or list1[i][j] == 0:
        return 0
    list1[i][j] = 0
    island(i+1,j)
    island(i,j+1)
    island(i-1,j)
    island(i,j-1)
    island(i+1,j+1)
    island(i-1,j-1)
    island(i+1,j-1)
    island(i-1,j+1)
    return 1
count = 0
for i in range(len(list1)):
    for j in range(len(list1[0])):
        if list1[i][j]: count += island(i,j)
        
print(count)
    
     



        
    




     