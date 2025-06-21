#Recursion
#Time Complexcity O(n)
#Space Complexcity O(1)
def function(i):
    if not i: return 
    print("Sru")
    function(i-1)
# function(3)

# if we don't give base case it will go until stack overflows

#Printing of n natual numbers
def n_natural_no(i):
    if i == 0:return
    print(i,end=" ")
    n_natural_no(i-1)
# n_natural_no(10)

#sum of first n natural nos
def sum_n_natural(i):
    if not i:return 0
    return i + sum_n_natural(i-1)
# print(sum_n_natural(10))

#Merge Sort
arr = [152,32,13,12,0,34,2,5,6]
def conquer(arr,left,mid,right):
    ind1= left
    ind2 = mid+1
    output = []
    while ind1 <= mid and ind2 <= right:
        if arr[ind1] <= arr[ind2]:
            output.append(arr[ind1])
            ind1+=1
        else:
            output.append(arr[ind2])
            ind2+=1
    while ind1 <= mid:
        output.append(arr[ind1])
        ind1+=1
    
    while ind2 <= right:
        output.append(arr[ind2])
        ind2+=1
    
    for i in range(len(output)):
        arr[i+left] = output[i]
        
def divide(arr,left,right):
    if left < right:
        mid = (left + right) // 2
        divide(arr,left,mid)
        divide(arr,mid+1,right)
        conquer(arr,left,mid,right)
# divide(arr,0,len(arr)-1)
# print(arr)


#  Subsets

def subsets(nums):
    ans = []
    def function(i,arr = []):
        if i == len(nums): 
            ans.append(arr)
            return 
        function(i+1,arr+[nums[i]]) + function(i+1,arr)
    function(0)
    return ans
# print(subsets([1,2,3]))
n = 5
k = 1
def kthGrammar( n, k):
    ans = ['0']
    def function(i):
        if i == n+1:
            return
        string =""
        for j in ans[i-1]:
            if j == '0':string+='01'
            else:string+='10'
        ans.append(string)
        function(i+1)
    function(1)
    print(ans[n][k])
# kthGrammar(n,k)     


#  Reorder List
arr = [1,2,3,4]
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def printing(head):
    temp = head
    while temp:
        print(temp.data,end= " ")
        temp = temp.next
        
def findmiddle(head):
    fast,slow = head.next,head
    while fast and fast.next:
        fast = fast.next.next
        slow= slow.next
        
    return slow

def reverse(head):
    prev,temp= None,head
    while temp:
        nextnonde,temp.next = temp.next,prev
        prev,temp = temp,nextnonde
    return prev
        
head = Node(arr[0])
node = head
for i in arr[1:]:
    node.next = Node(i)
    node= node.next
middle = findmiddle(head) 

first = head
secound = reverse(middle)

while secound.next:
    first_nn, first.next = first.next,secound
    first = first_nn
    secound_nn,secound.next = secound.next,first
    secound = secound_nn
    
printing(head)