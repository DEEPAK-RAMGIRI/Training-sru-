#Creating subsequence 
arr = [1,2,3]
ans = []
#time Complexcity O(2 ^ n)
#Space complexcity O(n)
def function(i,temp):
    if i == len(arr): 
        ans.append(temp)
        return
    function(i+1,temp + [arr[i]])
    function(i+1,temp)
function(0,[])
# print(ans)


#printing subsequence whose sum is k
arr = [1,2,3,4,0,1]
ans = []
k = 8
def function(i,sums,temp):
    if i == len(arr):
        if sums == k:
            ans.append(temp)
        return
    function(i+1,sums + arr[i],temp + [arr[i]])
    function(i+1,sums,temp)
function(0,0,[])
print(ans)