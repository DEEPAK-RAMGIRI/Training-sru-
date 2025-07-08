    #segment trees
# arr = [2,1,0,4,3,7]
arr = [1,3,2,0,4,5]
# arr = [3,1,2,7]
arr =[3,1,2,7,2,1,2,3]


ans = [-1] * ((4* len(arr)))

def segmant_tree(index,left,right):
    if left == right:
        ans[index] = arr[left]
        return ans[index]
    mid = left + ((right - left) >> 1)
    ans[index] = (segmant_tree(2*index+1,left,mid) +segmant_tree(2*index+2,mid+1,right))
    return ans[index]


def update_tree(index,value,i,left,right):
    if left == right:
        ans[i] = value
    else:
        mid = left + ((right - left) >> 1)
        if index <= mid:
            update_tree(index,value,2*i+1,left,mid)
        else:
            update_tree(index,value,2*i+2,mid+1,right)
        ans[i] = ans[2*i+1] + ans[2*i+2]
        
        
def find_range_sums(start,end,index,left,right):
    mid = left + ((right - left) >> 1)
    if start > right or end < left:
        return 0
    elif start <= left and end >= right:
        return ans[index]
    else:
        return find_range_sums(start,end,2 * index + 1,left,mid) + find_range_sums(start,end,2 * index + 2,mid+1,right)
    
        
        
        
def find_mini_segement_tree(index,left,right):
    if left == right:
        return ans
segmant_tree(0,0,len(arr) - 1)
queries =  [(2,6)]
for i,j in queries:
    print(find_range_sums(i,j,0,0,len(arr)-1))
    
# update_tree(1,2,0,0,len(arr)-1)
print(ans)
    
    
    
            
        
    
        