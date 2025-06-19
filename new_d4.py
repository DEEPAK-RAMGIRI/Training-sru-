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
    
    
ll = Linkedlist()
arr = [1,2,3,4,5,6]
for i in arr: ll.insert(i) 
# ll.find_middle1()
ll.find_middle2() 
#ll.find_middle3()
            