#Creation of Segment Tree
arr = [1,2,3,4]
queries = [(1,4),(2,3)]
ans = [-1] * (4 * len(arr))
def create_segment_tree(left,right,index):
    if left == right: 
        ans[index] = arr[left]
        return ans[index]
    mid = left + ((right - left) >> 1)
    ans[index] = create_segment_tree(left,mid,2 * index + 1) + create_segment_tree(mid+1,right,2*index+2)
    return ans[index]
# create_segment_tree(0,len(arr)-1,0)


def find_range_sum(left,right,index,start,end):
    mid = left + ((right - left) >> 1)
    if left > end or right < start:
        return 0
    elif left >= start and right <= end:
        return ans[index]
    else:
        return find_range_sum(left,mid,2 * index + 1,start,end) + find_range_sum(mid+1,right,2 * index + 2,start,end)
  
# for i,j in queries:
#     print(i-1,j-1)
#     print(find_range_sum(0,len(arr)-1,0,i-1,j-1))  
# print(ans)


arr = [1,2,3,4]
mini = [-1] * (4 * len(arr))
def min_segment_tree(left,right,index):
    if left == right:
        mini[index] = arr[left]
        return mini[index]
    mid = left + ((right - left) >> 1)
    mini[index] = min(min_segment_tree(left,mid,2 * index + 1),min_segment_tree(mid+1,right,2*index + 2))
    return mini[index]
min_segment_tree(0,len(arr)-1,0)


def find_min_in_range(left,right,start,end,index):
    mid = left + ((right - left) >> 1)
    if start > right or end < left:
        return float("inf") 
    elif start <= left and right <= end:
        return mini[index]
    else: return min(find_min_in_range(left,mid,start,end,2 * index + 1),find_min_in_range(mid + 1,right,start,end,2 * index + 2))  


queries = [(0,2),(2,3)]
for i,j in queries:
    print(find_min_in_range(0,len(arr)-1,i,j,0))
print(mini)



    