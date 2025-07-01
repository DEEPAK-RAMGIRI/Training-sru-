#Assign Cookies
g = [1,2,3]
s = [1,1]
def findContentChildren(g, s):
    j = i = 0
    g.sort()
    s.sort()
    count = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count+=1
            i+=1
        j+=1
    return count
# print(findContentChildren(g,s))


#Time Complexcity O(n log n)
# Space Complexcity O(n)
# Fractional knapsack
arr = [(100,20),(60,10),(100,50),(200,50)]
w = 90


arr.sort (key = lambda x:x[0]/x[1], reverse = True)
total = profit = 0
for i,j in arr:
    if j + total <= w:
        total += j
        profit += i
    else:
        profit += (i / j) * (w - total)
        total += (w - total)
        break
# print(profit)

# Using recursion
# Time Complexcity O(n)
#Space Complexcity O(n)
arr = [(100,20),(60,10),(100,50),(200,50)]
w = 90
arr.sort(key = lambda x: x[0]/x[1],reverse=True)
def find(i,total,maxi):
    if i == len(arr) or total >= w:
        return maxi
    if total + arr[i][1] <= w:
        return find(i+1,total + arr[i][1],maxi + arr[i][0])
    else:
        maxi += ((arr[i][0]/arr[i][1])*(w- total))
        total += (w - total)
        return maxi
        
# print(find(0,0,0))
    
    
    
#  Greddy algo to find minimum no of coins
nums = [1,2,5,10,20,50,100,500,1000]
v = 70
#Time Complexcity O(2^n)
#Space Complexcity O(k) where k is the no of combinations of arr and ans 
# here we require minimum no of coins to get 70 is 2 like we have 50 and 20 notes which is 70
ans = []
def find(i,arr,total):
    global ans
    if i == len(nums) or total > v:
        return 
    elif total == v:
        if not ans or len(ans) > len(arr):
            ans = arr
        return
    find(i,arr+[nums[i]],total + nums[i])
    find(i+1,arr,total)
# find(0,[],0)
# print(ans)

nums = [1,2,5,10,20,50,100,500,1000]
v = 489
j = len(nums) - 1
ans = []
#Time Complexcity O(n)
#Space COmplexcity O(k) where k is the values required to reach the v
while j >= 0 and v:
    count = v // nums[j]
    if count > 0:
       ans.extend([nums[j] for  _ in range(count)])
       v%=nums[j]
    j-=1
# print(ans)


#Time complexcityO(n)
#Space Complexcity O(1)
def lemonadeChange(bills):
    c5= 0
    c10 =0
    for i in bills:
        if i == 5:
            c5+=1
        elif i == 10:
            if not c5: return False
            c10+=1
            c5-=1
        else:
            if c10 >= 1 and c5 >= 1:
                c5-=1
                c10-=1
            elif c5 >= 3:
                c5-=3
            else: return False
    return True 
# print(lemonadeChange([5,5,5,10,20]))


# Time Complexcity O(3 ^n)
#Space Complexcity O(1)
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
# s = "()"
s = list(s)

def reursion(j,temp,count):
    if count < 0: return False 
    if j == len(s): return not count
    elif s[j] == "(": return reursion(j+1,temp+s[j],count+1)
    elif s[j] ==  ")": return reursion(j+1,temp+s[j],count-1)
    elif s[j] == "*": return reursion(j + 1,temp + "(",count + 1) or reursion(j + 1,temp +")",count-1) or reursion(j + 1,temp,count)
    return False
    
# print(reursion(0,'',0))


#Time Complexcity O(n)
#Space Complexcity O(1)
#Maintain range

s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
mini = maxi = 0
for i in s:
    if i == "(":
        mini +=1
        maxi +=1
    elif i == ")":
        mini -= 1 if mini else 0 
        maxi -= 1  
    else:
        mini -= 1 if mini else 0
        maxi += 1
# print(mini <=0)
        
#N meeting in a room

#Time Complexcity O(n  log n)
#Space Complexcity O(n)
start = [0,3,1,5,5,8]
end = [5,4,2,9,7,9]
time = []
count = 1
for i in zip(start,end): time.append(i)
time.sort(key = lambda x:(x[1],x[0]))
end = time[0][-1]
for i in range(1,len(time)):
    if end <= time[i][0]:
        print(time[i])
        end = time[i][-1]
        count+=1
# print(count)


# Jump Game
nums = [2,3,1,1,4]  
# nums = [3,2,1,0,4]
 
def find(path):
    if path == len(nums) - 1:
        return True
    elif not nums[path]: return False
    for i in range(1,nums[path] + 1):
        if find(i + path): return True
    return False       
# print(find(0))


#Time complexcity O(n)
#Space Complexcity O(1)
nums = [2,3,1,1,4]  
nums = [3,2,1,0,4]
maxi = 0

for i in range(len(nums)):
    if i > maxi:
        # print(False)
        break
    maxi= max(maxi,i + nums[i])
# print(True)
    






      
    