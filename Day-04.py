# print frequency of element in array
#method 01
def function01(arr,i,k,count):
    if i == len(arr):
        return count
    if arr[i] == k:
        count+=1
    return function01(arr,i+1,k,count)

#method 02
def function02(arr,k,i):
    if i == len(arr):
        return 0
    if arr[i] == k:
        return 1 + function02(arr,k,i+1)
    return function02(arr,k,i+1)    

arr=[2,4,6,3,2,6,1,2,3,6,6,5]
# print(function01(arr,0,6,0))
# print(function02(arr,6,0))


#Method 01 using dictionary
# print the value which will occurs exactly 2 times

def function03(arr,i,freq):
    if i == len(arr):
        for j in arr:
            if freq[j] == 2:
                return j
        return -1
    freq[arr[i]] =  freq.get(arr[i],0)+1
    return function03(arr,i+1,freq)

#Method 2 using  two recursive functions
def loop(arr,i):
    if i == len(arr):
        return -1
    if function04(arr,arr[i],0,0) == 2:
        return arr[i]
    return loop(arr,i+1)

def function04(arr,k,i):
    if i == len(arr):
        return 0
    if arr[i] == k:
        return 1 + function04(arr,k,i+1)
    return function04(arr,k,i+1)

arr =[2,3,3,4,4,4,5,6]
# print(function01(arr,0,{},2))
# print(loop(arr,0))


# printing the subsets  of the arr using recursion
# Method 01

res =[]
arr =[1,2,3]
def function05(arr,ans,i):
    if i == len(arr):
        res.append(ans)
        return
    function05(arr,ans+[arr[i]],i+1)
    function05(arr,ans,i+1)
function05(arr,[],0)
# print(res)

# printing subsubets where sum of array is target
#method 01
res =[]
arr =[1,2,3,4,5,6,7,8,9,10]
def function06(arr,ans,i,target):
    if i == len(arr):
        if sum(ans) == target:
            res.append(ans)
        return
    function06(arr,ans+[arr[i]],i+1,target)
    function06(arr,ans,i+1,target)
function06(arr,[],0,10)
print(res)

#method 02
#returning true or false
arr =[1,2,3,4,5,6,7,8,9,10]
def function07(arr,i,target,sums):
    if sums == target:
        return True
    if i == len(arr) or sums > target:
        return False
    return function07(arr,i+1,target,sums+arr[i]) or function07(arr,i+1,target,sums)
# print(function07(arr,0,55,0))

#method 03
arr =[1,2,3,4,5,6,7,8,9,10]
def function07(arr,i,target):
    if target == 0:
        return True
    if i == len(arr) or target < 0:
        return False
    return function07(arr,i+1,target-arr[i]) or function07(arr,i+1,target)
# print(function07(arr,0,55))

#method 04
#same code as shown above but here we are coming from back side
arr =[1,2,3,4,5,6,7,8,9,10]
arr=[2,4,6,8]
def function07(arr,i,target):
    if target == 0:
        return True
    if i == -1 or target < 0:
        return False
    return function07(arr,i-1,target-arr[i]) or function07(arr,i-1,target)
# print(function07(arr,len(arr)-1,13))

#print  minimum no of values to get the target value
#method 01  using recursion
arr = [2,4,6,8]
def function08(arr,i,target,count):
    if target == 0:
        return count
    if i == -1 or target < 0:
        return float("inf")
    return min(function08(arr,i-1,target-arr[i],count + 1),function08(arr,i-1,target,count))
ans = function08(arr,len(arr)-1,1,0)
    
# print( ans if ans != float("inf") else -1)

#using bitmanipulation method
#method 02
arr = [2,4,6,8]
res = []
def function09(arr,target):
    n = len(arr)
    subsets = 1 << n
    for i in range(subsets):
        temp = []
        for j in range(len(arr)):
            if i  & (1 << j):
                temp.append(arr[j])
        res.append(temp)
    for i in res:
        if sum(i) == target:
            print(i,end=" ")   
# function09(arr,10)


#take list ele from user and find largest even and smallest odd no
#inputs = 2 7 211 45 78 90 1 8 34 123 77 42

list1 = [] #list(map(int,input().split()))
mini = float("inf")
maxi = float("-inf")

for i in list1:
    if i > maxi and not i & 1:
        maxi = i
    if i < mini and i & 1:
        mini = i
# print(maxi,mini)





#secound largest no in the list
list1 =[2 ,10 ,211, 45, 78, 90, 1, 8, 34, 123, 77, 42]
secound = -1
maxi = float("-inf")
for i in list1:
    if maxi < i:
        secound = maxi
        maxi = i
    elif i > secound and i < maxi:  # imp condition
        secound = i
# print(secound)
        

    
     

    

    
    
    
    
    