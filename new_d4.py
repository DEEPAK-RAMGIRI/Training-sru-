class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head =None
        
    def insert(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        
    def printing(self,head = None):
        temp = head if head else self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            
    # Middle of the Linked List
    # Time Complexcity O(n) + O(n//2) ~ o(n)
    #Space Complexcity O(n)
    def find_middle1(self):
        temp =self.head
        arr = []
        while temp:
            arr.append(temp.data)
            temp =temp.next
        middle = len(arr)//2
        temp = self.head
        while middle:
            middle-=1
            temp = temp.next
        self.printing(temp)
    
    #Time Complexcity O(n) + O(n//2) ~ O(n)
    #Space Complexcity O(1)
    def find_middle2(self):
        count = 0 
        temp = self.head
        while temp:
            count+=1
            temp = temp.next
        count//=2
        temp = self.head
        while count:
            count-=1
            temp = temp.next
        self.printing(temp)
            
    #Time Complexcity O(n/2) ~ O(n)
    #Space Complexcity O(1)
    def find_middle3(self):
        fast,slow = self.head.next,self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    #Check Palindrome Linked List
    #Time Complexcity O(n) + O(n) ~  O(n)
    #Space Complexcity O(n)
    def check_palindrome1(self):
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.data)
            temp = temp.next
        return arr == arr[::-1]
    
    #Time Complexcity  O(n) +O(n//2) + O(n//2) ~ O(n)
    #Space Complecity O(1)
    def check_palindrome2(self):
        temp = self.head
        
        def reverse(head):
            prev,temp = None,head
            while temp:
                nextnode,temp.next = temp.next,prev
                prev,temp = temp,nextnode
            return prev
        
        fast,slow = self.head,self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        secound_half = reverse(slow)
        temp = self.head
        self.printing(secound_half)
        while temp != slow:
            if temp.data != secound_half.data:
                print(False)
                break
            temp = temp.next
            secound_half = secound_half.next
        else: print(True)
    
    
   # Odd Even Linked List
   #Time Complexcity O(n) + O(n) ~ O(n)
   #Space Complexcity O(n) + O(n)  ~ O(n)
    def oddEven_Linkedlist1(self):
        odd,even = [],[]
        temp = self.head
        count = 0
        while temp:
            count += 1 
            if count & 1: odd.append(temp.data)
            else:even.append(temp.data)
            temp = temp.next
        odd.extend(even)
        
        dummy = Node(0)
        temp = dummy
        for i in odd:
            temp.next = Node(i)
            temp = temp.next
        self.printing(dummy.next)
        
    
    #Time Complexcity O(n)
    #Space Complexcity O(1)
    
    def oddEven_Linkedlist2(self):
        slow,fast = self.head,self.head.next
        even = fast
        while fast and fast.next:
            slow.next = fast.next
            slow = slow.next
            fast.next = slow.next
            fast = fast.next
        slow.next = even
        
        self.printing(self.head)
        
        
    # Swapping Nodes in a Linked List
    #Time Complexcity O(n)
    #Space Complexcity O(n)
    def swap_k_node1(self,k):
        temp = self.head
        arr = []
        while temp:
            arr.append(temp)
            temp = temp.next
        arr[k-1].data,arr[~k+1].data = arr[~k+1].data,arr[k-1].data

        self.printing()
        
    #Time Complexcity O(n) 
    #Space Complexcity O(1)
    def swap_k_node2(self,k):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count+=1

        temp = self.head
        secound = self.head
        for _ in range(k-1):
            temp = temp.next
        for _ in range(count - k):
            secound = secound.next
        temp.data,secound.data =secound.data,temp.data
        self.printing()
        
    def swap_k_node3(self,k):
        temp = self.head
        secound = self.head
        count = 0
        while temp:
            count+=1
            if count == k: start = temp
            if count > k: secound = secound.next
            temp = temp.next
        start.data,secound.data =secound.data,start.data
        self.printing() 
        
        
    
    
    # Merge Nodes in Between Zeros
    #Time Complexcity O(n)
    #Space Complexcity O(1)
    def merge_nodes_bw_zeros1(self):
        arr = []
        temp = self.head
        value = 0
        while temp:
            value += temp.data
            if not temp.data and value:
                arr.append(value)
                value = 0

            temp =temp.next

        temp = dummy = Node(0)
        for i in arr: 
            temp.next = Node(i)
            temp = temp.next

        self.printing(dummy.next)
    
    #Optimised version
    #Time Complexcity O(n)
    #Space Complexcity O(1)
    
    def merge_nodes_bw_zeros2(self):
        dummy = Node(0)
        temp1 = dummy
        temp= self.head
        value = 0
        while temp:
            value += temp.data
            if value and not temp.data:
                temp1.next = Node(value)
                temp1 = temp1.next
                value = 0
            temp = temp.next
        self.printing(dummy.next)
        
        
    # More Optimised version🔥
    # we are using the auxillary space of the programme
    def merge_nodes_bw_zeros3(self):
        temp1,temp2 = self.head,self.head.next
        total = 0
        while temp2:
            total += temp2.data
            if not temp2.data and total:
                temp2.data,temp1.next  = total,temp2
                temp1,total = temp1.next,0
            temp2 = temp2.next
        self.printing(self.head.next)
     
    #Time Complexcity O(n)
    #Space Complexcity O(1)
    def Minimum_and_Maximum_Number_of_Nodes_Between_Critical_Points1(self):
        temp = self.head
        ans = []
        prev,temp = temp.data,self.head.next
        count = 0
        while temp.next:
            count +=1
            if prev < temp.data > temp.next.data or prev > temp.data < temp.next.data:
                ans.append(count)
            prev = temp.data
            temp = temp.next

        if len(ans) < 2: return [-1,-1]
        mini = float("inf")
        for i in range(len(ans)-1):
            mini = min(mini,ans[i+1] - ans[i])
        print([mini,ans[-1] - ans[0]])


         
    def Minimum_and_Maximum_Number_of_Nodes_Between_Critical_Points2(self):
        temp = self.head
        first = secound = -1
        mini = float("inf")
        prev,temp = temp.data,self.head.next
        count = 0
        while temp.next:
            count +=1
            if prev < temp.data > temp.next.data or prev > temp.data < temp.next.data:
               if first == -1: 
                   first = secound = count
               else:
                   mini = min(mini,abs(count - secound))
                   secound = count
            prev = temp.data
            temp = temp.next
        if mini == float("inf"): return [-1,-1]
        print([mini,secound- first])

        
    
            

ll = Linkedlist()
# arr = [1,2,3,4,5,6]
# for i in arr: ll.insert(i)
# Middle of the Linked List 
# ll.find_middle1()
# ll.find_middle2() 
#ll.find_middle3()
            
            
#Check Palindrome Linked List
# arr = [1,2,2,1]
# for i in arr: ll.insert(i)
# ll.check_palindrome1()
# ll.check_palindrome2()


# Odd Even Linked List
# arr = [1,2,3,4,5]
# for i in arr: ll.insert(i)
# ll.oddEven_Linkedlist1()
# ll.oddEven_Linkedlist2()


#  Swapping Nodes in a Linked List
# nums = [1,2,3,4,5]
# k = 2
# for i in nums: ll.insert(i)
# ll.swap_k_node1(k)
# ll.swap_k_node2(k)
# ll.swap_k_node3(k)



# Merge Nodes in Between Zeros
# arr = [0,3,1,0,4,5,2,0]
# for i in arr: ll.insert(i)
# ll.merge_nodes_bw_zeros1()
# ll.merge_nodes_bw_zeros2()
# ll.merge_nodes_bw_zeros3()


# Find the Minimum and Maximum Number of Nodes Between Critical Points
# arr = [5,3,1,2,5,1,2]
# for i in arr: ll.insert(i)
# ll.Minimum_and_Maximum_Number_of_Nodes_Between_Critical_Points1()
# ll.Minimum_and_Maximum_Number_of_Nodes_Between_Critical_Points2()




# Stacks 
# Remove All Adjacent Duplicates In String
#Time Complexcity O(n)
#Space Complexcity O(1)
s = "abbaca"
stack = []
for i in s:
    if stack and stack[-1] == i: stack.pop()
    else: stack.append(i)
# print(''.join(stack))



#Time Complexcity O(n)
#Space Complexcity O(n)
tokens = ["2","1","+","3","*"]
stack = []
for i in tokens:
    if i in '+-*/':
        a = (stack.pop())
        b = (stack.pop())
        if i == "+":
            stack.append(a+b)
        elif i == "-":
            stack.append(b-a)
        elif i == "*":
            stack.append(a*b)
        else:
            stack.append(int(float(b)/a))
    else:
        stack.append(int(i))
# print(stack[-1])

#Time Complexcity O(n^2)
#Space Complexcity O(n)
# Daily Temperatures

t = [73,74,75,71,69,72,76,73]

ans = []
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[j] > t[i]:
            ans.append(j-i)
            break
    else:
        ans.append(0)
# print(ans)

#Time Complexcity O(n)
#Space Complexcity O(1)
temperatures = [73,74,75,71,69,72,76,73]
stack = []
ans = [0] * len(temperatures)
for i in range(len(temperatures)-1,-1,-1):
    while stack and temperatures[stack[-1]] <= temperatures[i]:
        stack.pop()
    if stack: ans[i] = stack[-1] - i
    stack.append(i)
print(ans)

