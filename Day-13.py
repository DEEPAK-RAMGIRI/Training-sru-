#Linked list 
class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def add_front(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return 
        node.next = self.head
        self.head = node
        
    def add_last(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        
    def add_middle(self,data):
        node = Node(data)
        if not self.head and self.head.next:
            self.add_front(node)
            return
        slow = self.head
        fast = self.head.next
       
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node.next = slow.next
        slow.next = node                        
            
        
    def print_linked_list(self):
        while self.head:
            print(self.head.data,end=" ")
            self.head = self.head.next

arr1 = [10,9,8,7,6,5,4,3,2,1]
arr1=[0,0,0,0]

ll = Linkedlist()
# for i in arr1:
#     ll.add_front(i)
# ll.print_linked_list()
for i in arr1:
    ll.add_last(i)
# ll.print_linked_list()
ll.add_middle(22.5)
ll.print_linked_list()