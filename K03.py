# longest valid palindrome subsequence

# Time Complexcity O(n)
# Space Complexcity O(1)
string = "ababbac"

def function(left,right):
    maxi = 0
    while left >= 0 and right < len(string) and string[left] == string[right]:
        maxi = max(maxi,right - left + 1)
        left-=1
        right+=1
    return maxi
ans = 0
for i in range(len(string)):
    ans = max(ans,function(i,i), function(i,i+1))



# print all the plaindromic substring from the string

def function(left,right):
    ans= []
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left-=1
        right+=1
    return string[left + 1:right]
 
allstring = set()
# for i in range(len(string)):
#     allstring.add(function(i,i))
#     allstring.add(function(i,i+1))


# Reverse the k last node


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
def insert(root,data):
    node = Node(data)
    if not root:
        return node 
    temp = root
    while temp.next:
        temp = temp.next
    temp.next = node
    return root

def display(root):
    while root:
        print(root.data,end=" ")
        root = root.next
        
       
def find_mid(root):
    fast = root
    slow = root
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow 

def reverse(root):
    prev = None
    while root:
        nextnode,root.next = root.next,prev
        prev,root = root,nextnode
    return prev

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:   
            return True
    return False

def find_k_node(k,root):
    fast = root
    slow = root
    for i in range( k ):
        fast = fast.next
    if not fast or not fast.next:
        return None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    temp =slow.next
    slow.next = None
    
    temp  =  reverse(temp)
    
    temp1 = root
    while temp1.next:
        temp1 = temp1.next
    temp1.next = temp
    return root
    
    
    
        
arr = [10,20,30,40,50,60,70,80,90]
root = None
for i in arr:
    root = insert(root,i)

display(find_k_node(3,root))