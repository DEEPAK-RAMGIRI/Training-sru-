# print frequency of element in array
def function(arr,i,k,count):
    if i == len(arr):
        return count
    if arr[i] == k:
        count+=1
    return function(arr,i+1,k,count)

arr=[2,4,6,3,2,6,1,2,3,6,6,5]
# print(function(arr,0,6,0))

arr =[2,3,3,4,4,4,5,6]

def function(arr,i,freq):
    if i == len(arr):
        for j in arr:
            if freq[j] == 2:
                return j
        return -1
    freq[arr[i]] = freq.get(arr[i],0)+1
    return function(arr,i+1,freq)
# print(function(arr,0,{},2))


def loop(arr,i):
    if i == len(arr):
        return -1
    if function1(arr,arr[i],0,0) == 2:
        return arr[i]
    return loop(arr,i+1)

def function1(arr,k,i,freq):
    if i == len(arr):
        return freq
    if arr[i] == k:
        freq+=1
    return function1(arr,k,i+1,freq)

print(loop(arr,0))
    
    
    
    
    
    