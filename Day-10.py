# Random problems
#given a list of integers 
arr = [2,3,1,4,2,3,1]
arr = [2,2,1,0,1,3,0]
arr = [2,3,1,0,1,3,0]
arr = [1,3,1,0,1,3,1]
arr = [3,2,1,0,4]
maxi = arr[0]
flag = True
for i in range(1,len(arr)):
    maxi-=1
    if maxi == -1:
        # print("not possible")
        break
    maxi = max(arr[i],maxi)
# else:
    # print("possible")
    
# Lemonshop problems
list1 = [5,5,5,20,10]
count_5 = 0
count_10 = 0
count_20 = 0
for i in list1:
    if i == 5:
        count_5+=1
    elif i == 10:
        if count_5 > 0:
            count_5-=1
        else:
            print("not possible")
            break
            
        count_10+=1
    else:
        if count_10 > 0 and count_5 > 0:
            count_5-=1
            count_10-=1
        elif count_5 > 3:
            count_5-=3
        else:
            # print("not_possible")
            break
        count_20+=1
# else:
#     print("possible")

# we have jobs we need 
# we need to find min average waiting time
# arr = [4,3,7,1,6,2]
arr = [4,3,7,1,6,2]
arr.sort()
waiting = 0
total_waiting = 0
for i in range(len(arr)-1):
    waiting+=arr[i]
    total_waiting += waiting 

# print(total_waiting//len(arr))
    
#greedy alogrithm   
def possible(g, s):
    g.sort()
    s.sort()
    i = j = count = 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1
    return count

# print(possible([1,6,2,3,4,5], [4,2,3,1,1,2]))

import math

def sqrt(n,precision):
    left = 0
    right = n
    while (right - left) > 1e-6:
        mid = (left + right) / 2
        if mid * mid < n:
            left = mid 
        else:
            right = mid 
    print(round(left,precision))
sqrt(10,3)
def sqrt(n,precision):
    left = 0
    right = n
    while (right - left) > 1e-6:
        mid = (left + (right - left) >> 1)
        if mid * mid < n:
            left = mid 
        else:
            right = mid 
    # print(round(left,precision))
# sqrt(10,3)
#method 01
arr1 = [1,4,5,7]
arr2 = [10,20,30,40]
x = 32
mini = float("inf")
for i in arr1:
    for j in arr2:
        if abs( i + j - x) > mini:
            flag = True
            break
        mini = min(mini,abs(i+j-x))
        a,b = i,j
    if flag: break
# print(a,b)
#Time Complexcity O( n * m)

#method 02
arr1 = [1,4,5,7]
arr2 = [10,20,30,40]
x = 32
left = 0
right = len(arr2) - 1
mini = float("inf")
while left < len(arr1) and right >= 0:
    total = arr1[left] + arr2[right]
    difference = abs(total-x)
    
    if difference < mini:
        a,b = left,right
        mini = difference
    if total > x:
        right -=1
    else:
        left+=1 
# print(a,b)

print("hello world")