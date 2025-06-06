# Sorting algo
#Bubble sorting
arr = [23,1,9,45,43,23,89,6,7,46,67,12]
for i in range(len(arr)):
    flag = True
    for j in range(len(arr)- i - 1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = False
    if flag: break
# print(arr)

# Selection sort
arr = [23,1,9,45,43,23,89,6,7,46,67,12]
for i in range(len(arr)):
    mini = i
    for j in range(i+1,len(arr)):
        if arr[mini] > arr[j]: 
            mini = j  
    if mini != i:
        arr[mini],arr[i] = arr[i],arr[mini]
# print(arr)   

#insertion sort
arr = [23,1,9,45,43,23,89,6,7,46,67,12]
for i in range(1,len(arr)):
    j = i - 1
    while j>=0 and arr[j] > arr[i]:
        j-=1
    j+=1
    arr[j] = arr[i]
# print(arr)

# merge Sort
arr = [23,1,9,45,43,23,89,6,7,46,67,12]
def conquer(arr,left,mid,right):
    ind1 = left
    ind2 = mid + 1
    output = []
    while ind1 <= mid and ind2 <= right:
        if arr[ind1] < arr[ind2]:
            output.append(arr[ind1])
            ind1+=1
        else:
            output.append(arr[ind2])
            ind2+=1
            
    while ind1<= mid:
        output.append(arr[ind1])
        ind1+=1
    
    while ind2 <= right:
        output.append(arr[ind2])
        ind2+=1
    
    for i in range(len(output)):
        arr[i+left] = output[i] 
    
def merge(arr,left,right):
    if left < right:
        mid = left + ((right - left) >> 1)
        merge(arr,left,mid)
        merge(arr,mid+1,right)
        conquer(arr,left,mid,right)
# merge(arr,0,len(arr)-1)
# print(arr)


# Lomuto Partition pivot 
def find_pivot(arr,left,right):
    pivot = arr[right]
    i = left - 1
    for j in range(left,right):
        if arr[j] < pivot:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    i+=1
    arr[i],arr[right] = arr[right],arr[i]
    return i
        
def quicksort(arr,left,right):
    if left <= right:
        pivot = find_pivot(arr,left,right)
        quicksort(arr,left,pivot-1)
        quicksort(arr,pivot+1,right)

arr = [23,1,9,45,43,23,89,6,7,46,67,12]
# quicksort(arr,0,len(arr)-1)
# print(arr)

# Permute two arrays such that sum of every pair is greater or equal to K
# sort and sorted use timsort which is developed by tim in 2002 didn't take extra space
#time complexcity is O(logn) for .sort()
#Time Comnplexcity is O(n) for sorted()

#Brute Force Using permutaion
#Time Complexcity O(n!^2 * n)
# n! for all permutaion for a and b so n!^2
# using all here which checks time Complexcity is O(n)
from itertools import permutations
a = [2, 1, 3]
b = [ 7, 8, 9 ] 
k = 10
flag = False
for i in permutations(a):
    for j in permutations(b):
        if all(x + y >= k for x, y in zip(i,j)):
            flag = True
            # print(True)
    if flag: break
# print(False)
        
#Time Cmoplexcity O(n log n)
#Space Complexcity O(1)
a = [2, 1, 3]
b = [ 7, 8, 9 ] 
k = 10
a.sort(reverse = True)
b.sort()
for i in range(len(a)):
    if a[i] + b[i] < k:
        # print(False)
        break
# else: print(True)

#count sort
arr = [4, 3, 12, 1, 5, 5, 3, 9]

count = [0] * (max(arr)+1)
for i in arr:
    count[i]+=1

# for i in range(len(count)):
#     while count[i] > 0:
#         print(i,end=" ")
#         count[i]-=1

# Find common elements in three sorted arrays
arr1 = [1, 5, 10, 20, 30]
arr2 = [5, 13, 15, 20]
arr3 = [5, 20] 

#Brute Force O(n^3)
# for i in arr1:
#     for j in arr2:
#         for k in arr3:
#             if i == j == k:
#                 # print(i,end=" ")
                
# Optimised version 🔥🔥🔥
i = j = k = 0
while i < len(arr1)  and j < len(arr2) and k <  len(arr3):
    if arr1[i] == arr2[j] == arr3[k]:
        print(arr1[i])
        i+=1
        j+=1
        k+=1
    else:
        mini = min(arr1[i],arr2[j],arr3[k])
        if arr1[i] == mini: i+=1
        elif arr2[j] == mini:j+=1
        else:k+=1
        