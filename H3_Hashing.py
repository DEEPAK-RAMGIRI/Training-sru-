#Longest Consecutive Sequence
nums = [100,4,200,1,3,2]
# Time complexcity O(n)
# Space complexcity O(1)
nums.sort()
maxi = 1
count = 1
for i in range(len(nums)-1):
    count = count+1 if nums[i] + 1 == nums[i+1] else 1
    maxi = max(maxi, count)
# print(maxi)   

# Longest subarray with sum k 
arr = [10, 5, 2, 7, 1, -10]
k = 15
#Time Complexcity O(N^2)
maxi = 0
for i in range(len(arr)):
    sums = 0
    for j in range(i,len(arr)):
        sums += arr[j]
        if sums == k:
            maxi = max(maxi,j-i+1)
# print(maxi)

# Longest subarray with sum k using prefix sum and hashmap
# Time Complexcity O(N)
# Space Complexcity O(N)
arr = [10, 5, 2, 7, 1, -10]
k = 15
prefix_sum = 0
maxi = 0
prefix_map = {0: -1}

for i in range(len(arr)):
    prefix_sum += arr[i]
    if (prefix_sum - k) in prefix_map:
        maxi = max(maxi, i - prefix_map[prefix_sum - k])
    if prefix_sum not in prefix_map:
        prefix_map[prefix_sum] = i

print(maxi)
            
  