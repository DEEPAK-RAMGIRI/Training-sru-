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
arr = [1,2,3,4,5]
for i in arr: ll.insert(i)
# ll.oddEven_Linkedlist1()
ll.oddEven_Linkedlist2()