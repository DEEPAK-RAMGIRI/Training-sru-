arr = [3,5,2,9,7,5,4,7,4,3]
arr = [2,5,1,3,6,8,7,9,4,5]
ans = [0] * (4 * len(arr))

# maxi

def Create_max(left,right,index):
    if left == right:
        ans[index] = arr[left]
        return ans[index]
    mid = left + ((right - left) >> 1)
    ans[index] = max(Create_max(left,mid,2 * index) , Create_max(mid+1,right,2* index+1))
    return ans[index]

def find_max(left,right,start,end,index):
    if left > end or right < start:
        return 0
    if start <= left and end >= right:
        return ans[index]
    mid = left + ((right - left) >> 1)
    return max(find_max(left,mid,start,end,2 * index) , find_max(mid+1,right,start,end,2 * index + 1))

def update_max(left,right,index,i,value):
    if left == right:
        ans[index] = value
    else:
        mid = left + ((right - left) >> 1)
        if mid <= i:
            update_max(left,mid,2 * index,i,value)
        else:
            update_max(mid+1,right,2*index+1,i,value)
        ans[index] = max(ans[2*index] ,ans[2*index + 1])
        
        

 
Create_max(0,len(arr)-1,1)
print(ans)
# sum
def Create_sum(left,right,index):
    if left == right:
        ans[index] = arr[left]
        return ans[index]
    mid = left + ((right - left) >> 1)
    ans[index] = Create_sum(left,mid,2 * index) + Create_sum(mid+1,right,2* index+1)
    return ans[index]

def find_sum(left,right,start,end,index):
    if left > end or right < start:
        return 0
    if start <= left and end >= right:
        return ans[index]
    mid = left + ((right - left) >> 1)
    return find_sum(left,mid,start,end,2 * index) + find_sum(mid+1,right,start,end,2 * index + 1)
 


no = 7
no = 10
no = 12
no = 11
# while no:
#     print(no)
#     no &= (no-1)
# print(no)

# no = 11
# while no:
#     print(no)
#     no -= (no & -no)
# print(no)


# Fenwick Tree

arr = [4,1,3,2,6,5,2,3,4,7]

ans = [0] * (len(arr) + 1)

def find(index,value):
    while len(arr) >= index:
        ans[index] += value
        index += (index & - index)

# Time complexcity O(n log n)
# Space Complexcity O(n)  
for i in range(1,len(ans)):
    if i & 1:
        ans[i] = arr[i - 1]
    else:
        ans[i] += arr[i- 1]
    find(i+ (i & - i),arr[ i - 1])


queries  = [[0,2],[2,3],[1,5],[1,2]]


def find_sum(index):
    sums = 0
    while index:
        sums += ans[index]
        index -= (index & -index)
    return sums
 
        


in1 = "   "
in2 = "|_|"
in3 = "  |"


in1 = " _  _  _     _ "
in2 = "  | _|| |  | _|"
in3 = "  ||_ | |  ||_ "

dictionary = {'1222' : '1','0111122021':'2','0111122122':'3','10111222':'4','0110112122':'5','011011202122':'6','011222':'7', '01101112202122':'8','0110111222':'9','011012202122':'0', '0110122022': '&','1012202122':'|','1011122022':"^" }
arr = [list(in1),list(in2),list(in3)]

k = 0
final = 0
a = op = None
while k < len(arr[0]):
    ans = ''
    for i in range(3):
        for j in range(k,k+3):
            if arr[i][j] != ' ':
                ans += str(abs(i)) + str(abs(j - k))
    k+=3
    ans = dictionary[ans]
    if ans.isdigit():
        final = (final * 10) + int(ans)
    else:
        a = final
        op = ans
        final = 0
print(a, final,op)
if op == '&':
    print(a & final)
elif op == "|":
    print(a | final)
else:
    print(a ^ final) 