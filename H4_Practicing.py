# # You are given an array A of n integers and q queries. Each query can be of one of the following two types:
# Update the array from index l to r (both inclusive) as follows:

# Copy
# Edit
# A[i] = (i - l + 1) * A[i]
# Where i ranges from l to r.

# 🔹 Type 2 Query: (2, l, r)
# Calculate the sum of elements from index l to r (both inclusive), and add it to the final answer.

# 🔸 Final Output
# After processing all queries, print the sum of results of all type 2 queries modulo (10^9 + 7).

# test case 01
# n = 7
# arr =[1, 4, 5, 1, 6, 7, 8]
# m = 5
# queries =[[1, 1, 6],
# [1, 1 ,5],
# [2, 5 ,5],
# [2, 3 ,4],
# [2, 3 ,3]]
sums = 0
#Test case 02
# n =7
# arr = [3,7,4,2,5,3,7]
# queries = [
#  [1, 0, 4],
#  [2, 0, 1],
#  [1, 3, 6],
#  [2, 3, 3],
#  [2, 0, 5]
# ]

#Test Case 03
n = 7
arr =[1,8,6,10,5,6,9]
queries =[
    [2, 0, 3],
    [1, 2, 3],
    [1, 0, 6],
    [2, 1, 4],
    [2, 6, 6]
    ]
#Time Complexcity is O(q,n)
for i in queries:
    Type,l,r = i
    if Type == 1:
        for j in range(l,r+1):
            arr[j] = (j - l + 1) * arr[l]
    else:
        sums += sum(arr[l:r+1])
# print(sums % (10**9+7))
    

#Question 02
#  find maximum subarray with k distinct elements in the array
#Test Case 01
# n = 11
# arr = [2,1,2,2,3,2,3,5,1,2,1]
# k = 2 
#Test  Case 02
# n = 3
# k =1
# arr = [-1,-2,-3]

# Test Case 03
n= 5
k = 5
arr = [-1, 1, 3, 2, -1]
seen = dict()

maxi = float("-inf")
lefty = 0
for righty in range(len(arr)):
        
    seen[arr[righty]] = seen.get(arr[righty],0)+1
    while len(seen) > k:
        seen[arr[lefty]] -=1
        if not seen[arr[lefty]]: 
            del  seen[arr[lefty]]
        lefty+=1
    maxi =max(maxi,sum(arr[lefty:righty + 1]))

print(maxi)
    
        