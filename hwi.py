# • Type 1 Query: (1, l, r) - Replace A[i]  = (i-l+1)*A[l] 
#  • Type 2 Query: (2, l, r) - Calculate the sum of the 
# arr = [1,4,5,1,6,7,8]
# queries = [
#     (1, 1, 6),
#  (1, 1, 5),
#  (2, 5, 5),
#  (2, 3, 4),
#  (2, 3, 3)
# ]



# arr = [3, 7, 4, 2, 5, 3, 7]
# queries = [[1, 0, 4], [2, 0, 1], [1, 3, 6], [2, 3, 3], [2, 0, 5]]

#Time Complexcity O(n)
#Space complexcirty o(n)
arr = [1, 8, 6, 10, 5, 6, 9]
queries = [[2, 0, 3], [1, 2, 3], [1, 0, 6], [2, 1, 4], [2, 6, 6]]
ans = [-1] * (4 * len(arr))
def create_segment_tree(left,right,index):
    mid = left + ((right - left) >> 1)
    if left == right:
        ans[index] = arr[left]
    else:
        ans[index] = create_segment_tree(left,mid,2*index+1) + create_segment_tree(mid+1,right,2*index+2)    
    return ans[index]


def update_tree(arr,left,right):
    for i in range(left,right+1):
        arr[i] = (i - left + 1)*arr[left]
        
    create_segment_tree(0,len(arr)-1,0)
   
def find_sum_range(left,right,start,end,index):
    mid = left + ((right - left) >> 1)
    if left > end or right < start:
        return 0
    elif left >= start and right <= end:
        return ans[index]
    else:
        return find_sum_range(left,mid,start,end,2*index+1)+ find_sum_range(mid+1,right,start,end,2*index+2)
          
print(arr)     
create_segment_tree(0,len(arr)-1,0)
total = 0
for i,j,k in queries:
    if i == 1:
        update_tree(arr,j,k)
    else:
        total+=find_sum_range(0,len(arr)-1,j,k,0)
print(arr)
print(ans)
print(total)


A = [1, 2, 2, 3, 2, 3, 5, 1, 2, 1, 1] #12
k = 2

# k = 1
# A = [-1, -2, -3] # 0

k = 5
A = [-1, 1, 3, 2, -1] # 6



#Time Complexcity O(2n)
#Space complexcityO(n)
from collections import defaultdict

seen = defaultdict(int)
left = total = max_sum = 0

for right in range(len(A)):
    seen[A[right]] += 1
    total += A[right]

    while len(seen) > k:
        seen[A[left]] -= 1
        total -= A[left]
        if seen[A[left]] == 0:
            del seen[A[left]]
        left += 1

    max_sum = max(max_sum, total)

# print(max_sum)



#3 question
A = [-1, 1, 1]
# A = [1, 1, 1, 1]
A = [-1, -1, 1] 

mini = float("inf")
total = 0
for i in A:
    mini = min(mini,total)
    total += i
# print(mini) 


