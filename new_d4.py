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
        
    def swap_k_node3(self):
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
        
        
    def swap_k_node4(self):
        pass
    #have error herre
    # dummy = ListNode()
    #     secound = dummy
    
    #     temp = head
    #     while temp and temp.next:
    #         if temp.next.data >= x:
    #             secound.next = temp.next
    #             temp.next = temp.next.next
    #             secound = secound.next
    #         else:
    #             temp = temp.next
    #     temp.next = dummy.next
    #     return head
    
    
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
arr = [0,3,1,0,4,5,2,0]
for i in arr: ll.insert(i)
# ll.merge_nodes_bw_zeros1()
# ll.merge_nodes_bw_zeros2()
ll.merge_nodes_bw_zeros3()