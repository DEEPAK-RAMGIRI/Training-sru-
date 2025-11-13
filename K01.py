string = '()()()(())(())'
# string ='))))))))))))))()('
# string = '))(('

# Time Complexcity O(n ^ 2)
# Space complexcity O(1)

def find():
    left = 0
    right = len(string) - 1
    ans = 0
    open = 0
    for i in range(len(string)):
        if string[i] == "(":
            open+=1
        close = 0
        for j in range(i+1,len(string)):
            if string[j] == ")":
                close+=1
        if open == close:
            ans+=i+1
            
    # print(ans)

# Time Complexcity O(n)
# Space Complexcity O(1)

def find():
    cc = string.count(")")

    new_op = 0
    new_cc = 0

    for i in range(len(string)):
        if new_op == cc-new_cc:
            print(i)
            return
        
        if string[i] == "(":
            new_op += 1
            
        elif string[i] == ")":
            new_cc += 1
            
         
# Time Complexcity O(n* len(queries)) 
# Space Complexcity O(1) 

arr = [4,6,2,3,7,1,3]
queries = [[2,5],[0,3],[3,5],[4,6],[1,5]]
def find_sum():

    for i in queries:
        start,end = i
        ans = 0
        for j in range(start,end+1):
            ans += arr[j]
            
# Time complexcity O(n)
# Space Complexcity O(n) 

def find():
    sums = [arr[0]]

    for i in range(1,len(arr)):
        sums.append(sums[-1] + arr[i])
        
    for i,j in queries:
        print(abs(sums[j] - sums[i-1]))
    
# find max from queries
# Time complexcity O(n)
# Space Complexcity O(n) 

def find():
    sums = [arr[0]]
    print(arr)
    for i in range(1,len(arr)):
        sums.append(max(sums[-1],arr[i]))
    print(sums)
    for i,j in queries:
        print(sums[j])


arr = [4,6,2,3,7,1,3]
queries = [[1,2,5],[2,2,4],[1,1,5],[1,2,5],[2,4,1],[1,0,3]]

def prefix_sum(arr):
    sums = [arr[0]]

    for i in range(1,len(arr)):
        sums.append(sums[-1] + arr[i])
        
    return sums
    
def find_sum():
    sums = prefix_sum(arr)
    for i,j,k in queries:
        
        if i == 1:

            print(abs(sums[k] - sums[j-1] ) if j != 0 else sums[k])
        if i == 2:
            arr[j] += k
            sums = prefix_sum(arr)
            

# segment Tree

arr = [3,2,4,7,6,5,8,9]
# queries = [[1,2,5],[2,2,4],[1,1,5],[1,2,5],[2,4,1],[1,0,3]]
queries = [[2,5],[0,3],[3,5],[4,6],[1,5],[0,1],[0,6]]
ans = [0] * 16
def Create_max(left,right,index):
    if left == right:
        ans[index] = arr[left]
        return ans[index]
    mid = left + ((right - left) >> 1)
    ans[index] = max(Create_max(left,mid,2 * index) , Create_max(mid+1,right,2 * index + 1))
    return ans[index]
Create_max(0,len(arr)-1,1)

def max_range(left,right,start,end,index):
    if left > end or right < start:
        return float("-inf")
    if left >= start and right <= end:
        return ans[index]
    mid = left + ((right - left) >> 1)
    return max(max_range(left,mid,start,end,2 * index) , max_range(mid+1,right,start,end,2* index + 1))
print(ans)
for j,k in queries:
    print(max_range(0,len(arr)-1,j,k,1))
    


arr = [3,2,4,6,5,8,1,3]
# queries = [[1,2,5],[2,2,4],[1,1,5],[1,2,5],[2,4,1],[1,0,3]]
queries = [[2,5],[0,3],[3,5],[4,6],[1,5],[0,1],[0,6]]

ans = [0] * 16

def Create(left,right,index):
    if left == right:
        ans[index] = arr[left]
        return ans[index]
    mid = left + ((right- left) >> 1)
    ans[index] = Create(left,mid,2 *index) + Create(mid+1,right,2 * index+ 1)
    return ans[index]

def sum_range(left,right,start,end,index):
    if left > end or right < start:
        return 0
    if left >= start and right <= end:
        return ans[index]
    mid = left + ((right - left)>>1)
    return sum_range(left,mid,start,end,2 * index) + sum_range(mid+1,right,start,end,2 * index+ 1)

Create(0,len(arr)-1,1)
print(ans)
for i,j in queries:
    print(sum_range(0,len(arr)-1,i,j,1))


        
