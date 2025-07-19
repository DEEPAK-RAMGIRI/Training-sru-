# Lexicographical Numbers
#Time Complexcity O(n) + O(n log n) + O(n)
#Space Complexciy O(1)
n = 13
ans = []
for i in range(1,n + 1):
    ans.append(str(i))
ans.sort()
print([int(i) for i in ans])


#Time Complexcity O(n)
#Space Complexcity O(1)
ans = [1]
def find(index):
    if index > n or len(ans) == n: return
    if index * 10 <= n:
        ans.append(index*10)
        find(index*10)
    if 1 <= (index + 1)%10 <= 9 and index + 1 <= n:
        ans.append(index + 1)
        find(index+1)
    return
find(1)
print(ans)



#Time Complexcity O(n)
#space Complexcit O(1)
nums = [1 ,2, 3, 4]
# nums = [1 ,2, 3, 4, 5]

nums.sort()
time = total = nums[0] + nums[1] 

for i in range(2,len(nums)):
    total += nums[i]
    time += total
# print(time)


#time Complexcity O(N)
#Space complexcity O(N)
n,k = 12,3
n,k = 30,9
ans = [1]


for i in range(2,n+1):
    if not n % i: 
        ans.append(i)
        if len(ans) == k+1: 
            break
if len(ans) < k:
    print(ans[0])
else: print(ans[-1])


#Time Complexcity O(root(n))
#Space Complexcity O( max(a,b)) 
# O(max(a,b)) < n
n,k = 12,3 
n,k = 30,9
temp1,temp2 = [],[]
for i in range(1,int(n ** 0.5)+ 1):
    if not n % i:
        temp1.append(i)
        if i != n// i: temp2.append(n//i)
temp1.extend(temp2[::-1])
# print(temp1[k] if len(temp1) >= k else temp1[0])
    
    
# House Problem

#Time Complexcity O(2 ^ n)
#SpaceComplexcity O(1) 
val = [6, 7, 1, 3, 8, 2, 5] 
def find(index):
    if index >= len(val):
        return 0
    left = find(index+2) + val[index]
    right = find(index+1)
    return max(left,right)

print(find(0))

#Time Complexcity O(n)
#Space Complexcity O(1)

val = [6, 7, 1, 3, 8, 2, 5]
dp = [-1] * len(val)
def find(index):
    if index >= len(val):
        return 0 
    elif dp[index] != -1: return dp[index]
    left = find(index + 2) + val[index]
    right = find(index + 1)
    dp[index] = max(left,right)
    return dp[index]
print(find(0))

#Time Complexcity O(n)
#space Complexcity O(1)
left = 0
right= 0
for i in range(len(val)):
    maxi = max(left,right + val[i])
    right = left
    left = maxi
print(maxi)


# Count the factors which are not  perfect squares

#Time Complexcity O(n) + O(sqrt(m))
#Space complexcity O(m)
n = 20
n = 72
factors = []
for i in range(2,n+1):
    if not n % i and ((i**0.5) ** 2) != i: 
        factors.append(i)
print(factors)
count = 0     
for i in factors:
    for j in range(2,int(i ** 0.5)+1):
        if not i % (j**2):
            break
    else: 
        count+=1
         
print(count)
    


