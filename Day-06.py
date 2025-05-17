# make a bubble sort
#method 01
arr = [3,4,1,5,68,34,12,67767,3,1,2,3,4,0]
arr = [5,2,3,8,1,6,7,4]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr,"\n")

# method 02 optimised version
# using flag
arr = [2,5,8,6,3,1,9,4,7]
for i in range(len(arr)-1):
    flag = True
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            flag = False
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if flag:
        break
print(arr,"\n")
 
        
# here we are not going to sort first and last k digits       
k = 2
arr = [5,2,3,8,1,6,7]
for i in range(len(arr)-1):
    for j in range(k,len(arr)-i-1-k):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)

#print the kth largest element using bubble sort

k = 5
arr = [2,5,8,6,3,1,9,4,7]   
for i in range(len(arr)-1):
    if i == k-1:
        break
    flag = True
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            flag = False
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if flag:
        break
print(arr[-k])