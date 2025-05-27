#Linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_nodes(self,arr):
        self.head = Node(arr[0])
        curr = self.head
        
        for i in arr[1:]:
            curr.next = Node(i)
            curr = curr.next
            
    def print_linkedlist(self):
        curr= self.head
        while curr:
            print(curr.data,end="-")
            curr = curr.next
        print()
            
            
    #linked list have a loop and hindi how many nodes in the loop 
    def find_length(self):
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        node4 = Node(40)
        node5 = Node(50)
        
        
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node3        
        
        head = node1
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        temp = slow
        while temp.next != slow:
            temp = temp.next
        temp.next = None
        count = 0
        while head:
            count+=1
            head = head.next
        print(count)
        
    def reverse_the_linked_list(self):
        temp = self.head
        prev = None
        while temp:
            nextnode,temp.next = temp.next,prev
            prev,temp = temp,nextnode
        self.head = prev
        
        
    def palindrome_or_not(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow
        prev = None
        while temp:
            nextnode,temp.next = temp.next,prev
            prev,temp = temp,nextnode
         
        temp = self.head

        while prev and temp :
            if temp.data != prev.data:
                print("not palindrome")
                break
            temp = temp.next
            prev =prev.next
        else:
            print("palindrome")
        
            
          
ll  = Linkedlist()
# ll.add_nodes([1,2,3,4,5,6,7,8,9,10][::-1])
ll.add_nodes([1,2,3,4,5,6,4,3,2,1])

# ll.find_length()
# ll.reverse_the_linked_list()
ll.print_linkedlist() 
ll.palindrome_or_not()
# ll.print_linkedlist()             