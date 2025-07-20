# Lexicographical Numbers
#Time Complexcity O(n) + O(n log n) + O(n)
#Space Complexciy O(1)
n = 13
ans = []
for i in range(1,n + 1):
    ans.append(str(i))
ans.sort()
print([int(i) for i in ans])


#Time Complexcity O(n)
#Space Complexcity O(1)
ans = [1]
def find(index):
    if index > n or len(ans) == n: return
    if index * 10 <= n:
        ans.append(index*10)
        find(index*10)
    if 1 <= (index + 1)%10 <= 9 and index + 1 <= n:
        ans.append(index + 1)
        find(index+1)
    return
find(1)
print(ans)



#Time Complexcity O(n)
#space Complexcit O(1)
nums = [1 ,2, 3, 4]
# nums = [1 ,2, 3, 4, 5]

nums.sort()
time = total = nums[0] + nums[1] 

for i in range(2,len(nums)):
    total += nums[i]
    time += total
# print(time)


#time Complexcity O(N)
#Space complexcity O(N)
n,k = 12,3
n,k = 30,9
ans = [1]


for i in range(2,n+1):
    if not n % i: 
        ans.append(i)
        if len(ans) == k+1: 
            break
if len(ans) < k:
    print(ans[0])
else: print(ans[-1])


#Time Complexcity O(root(n))
#Space Complexcity O( max(a,b)) 
# O(max(a,b)) < n
n,k = 12,3 
n,k = 30,9
temp1,temp2 = [],[]
for i in range(1,int(n ** 0.5)+ 1):
    if not n % i:
        temp1.append(i)
        if i != n// i: temp2.append(n//i)
temp1.extend(temp2[::-1])
# print(temp1[k] if len(temp1) >= k else temp1[0])
    
    
# House Problem

#Time Complexcity O(2 ^ n)
#SpaceComplexcity O(1) 
val = [6, 7, 1, 3, 8, 2, 5] 
def find(index):
    if index >= len(val):
        return 0
    left = find(index+2) + val[index]
    right = find(index+1)
    return max(left,right)

print(find(0))

#Time Complexcity O(n)
#Space Complexcity O(1)

val = [6, 7, 1, 3, 8, 2, 5]
dp = [-1] * len(val)
def find(index):
    if index >= len(val):
        return 0 
    elif dp[index] != -1: return dp[index]
    left = find(index + 2) + val[index]
    right = find(index + 1)
    dp[index] = max(left,right)
    return dp[index]
print(find(0))

#Time Complexcity O(n)
#space Complexcity O(1)
left = 0
right= 0
for i in range(len(val)):
    maxi = max(left,right + val[i])
    right = left
    left = maxi
print(maxi)


# Count the factors which are not  perfect squares

#Time Complexcity O(n) + O(sqrt(m))
#Space complexcity O(m)
n = 20
n = 72
factors = []
for i in range(2,n+1):
    if not n % i and ((i**0.5) ** 2) != i: 
        factors.append(i)
print(factors)
count = 0     
for i in factors:
    for j in range(2,int(i ** 0.5)+1):
        if not i % (j**2):
            break
    else: 
        count+=1
         
print(count)

    
# Find the middle node in the circular double linked list

print("linked list")
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#Time Complexcity O(n)
#Space Complexcity O(1)
                    
def insert(head,arr):
    dummy = Node(arr[0])
    head = dummy
    for i in arr[1:]:
        dummy.next = Node(i)
        dummy.next.prev = dummy
        dummy = dummy.next
        
    dummy.next = head
    head.prev = dummy
    return head

#Time Complexcity O(n)
#Space Complexcity O(1)
def printing(head):
    if not head: 
        print("head is empty")
        return 
    if head.next == head:
        print(head.data)
        return 
    print(head.data,end=" ")
    temp = head.next
    while temp != head:
        print(temp.data,end= " ")
        temp = temp.next
        
#Time complexcity O(n)
#Space Complexcity O(1)
def find_middle_element(head):
    slow,fast = head,head.next
    while fast != head and fast.next != head:
        slow = slow.next
        fast = fast.next.next
    return slow.data 
arr = [1,2,3,4,5,6,7,8,9,10]
head = insert(None,arr)
print(find_middle_element(head))
printing(head)



arr = [1,10,2,25]
#Time Complexcity O(n)
#Space Complexcity O(11)
# next Greater Element
stack = []
ans = []
for i in arr[::-1]:
    while stack and stack[-1] < i:
        stack.pop()
    if stack: ans.append(stack[-1])
    else: ans.append(-1)
    stack.append(i)
print(ans[::-1])
    
    
# subtraction linked list

arr2=[2,4,3]
arr1=[4,9,3,3]
#ouput = 3052



head1 = insert(None,arr1)
head2 = insert(None,arr2)

def subtract(head1,head2):
    if not head1 and not head2: return None
    if not head1: return head2
    if not head2: return head1

    
    temp1 = head1.next
    no1 = str(head1.data)
    while temp1 != head1:
        no1 += str(temp1.data)
        temp1 = temp1.next
    
    no2 = str(head2.data)
    temp2 = head2.next
    
    while temp2 != head2:
        no2 += str(temp2.data)
        temp2 = temp2.next
        
    diff = list(map(str,str(int(no2[::-1])-int(no1[::-1]))))
    
    dummy = Node(0)
    head = dummy
    for i in diff:
        dummy.next = Node(i)
        dummy.next.prev= dummy
        dummy = dummy.next
    dummy.next = head
    head.prev = dummy
        
    return head.next
    
    
head = subtract(head1,head2)
printing(head)
print()
    
    
        
class Stack:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def push(head,data):
    node = Stack(data)
    if not head:
        return node
    node.next = head
    head = node
    return head

def pop(head):
    if not head: 
        return "Stack is Empty"
    return head.next,head.data

def peek(head):
    if not head : return None
    return head.data

def printing(head):
    while head:
        print(head.data,end=" ")
        head = head.next

arr = [1,2,3,4,5]
head = None

for i in arr:
    head = push(head,i)

head,value = pop(head)
head,value = pop(head)
print(value)
print(peek(head))
     
    
stack1, stack2 = [], []

def enque(data):
    stack1.append(data)

def deque():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if stack2:
        return stack2.pop()
    return "Queue is Empty"

def peek(): 
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if stack2:
        return stack2[-1]
    return "Queue is Empty"

def printing():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    print(stack2[::-1])  

for i in [1, 2, 3, 4]:
    enque(i)

printing()        # Output: [1, 2, 3, 4]
print(deque())    # Output: 1
printing()        # Output: [2, 3, 4]



    

        
   
    