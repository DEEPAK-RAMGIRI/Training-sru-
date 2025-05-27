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
            
    def add_two_numbers(self):
        arr1 = [4,2,7,5]
        arr2 = [8,7,3,8]
        head1 = head2 = None 
        def nodes(head,arr):
            head = Node(arr[0])
            curr = head
            for i in arr[1:]:
                curr.next = Node(i)
                curr = curr.next
            return head
        
        head1 = nodes(head1,arr1)
        head2 = nodes(head2,arr2)
        dummy = Node(0)
        temp = dummy
        carry = 0
        while head1 and head2:
            if (head1.data + head2.data + carry) > 9:
                temp.next = Node(((head1.data + head2.data + carry) % 10 ) )
                carry = 1
            else:
                temp.next = Node(head1.data + head2.data + carry)
                carry = 0
            temp = temp.next 
            head1 = head1.next
            head2 = head2.next
        if carry: temp.next = Node(carry)
    
        
        temp = dummy.next
        prev  = None
        while temp:
            nextnode,temp.next = temp.next,prev
            prev,temp = temp,nextnode
         
        while prev:
            print(prev.data,end= " ")
            prev = prev.next
        
                 
            
        
def merge_sort(head1,head2):
    
    node = Node(0)
    dummy = node
    while head1 and head2:
        if head1.data < head2.data:
            dummy.next = head1
            head1 = head1.next
        else:
            dummy.next = head2
            head2 = head2.next
        dummy = dummy.next
    dummy.next = head1 if head1 else head2
    temp = node.next
    while temp:
        print(temp.data,end=" ")
        temp = temp.next
        

        
        
def common_node_in_linked_list():
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)
    node6 = Node(60)
    node7 = Node(70)
    node8 = Node(100)
    node9 = Node(200)
    node10 = Node(300)
    node11 = Node(400)
    node12 = Node(500)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node8.next = node9
    node9.next = node10
    node10.next = node11
    node11.next = node12
    node12.next = node5
    
    temp1 = node1
    temp2 = node8

    while temp1 != temp2:
        temp1 = temp1.next if temp1 else node8
        temp2 = temp2.next if temp2 else node1
    
    print(temp1.data)
        
    
                
            
        
            
        
ll  = Linkedlist()
# ll1 = Linkedlist()
# ll.add_nodes([1,2,3,4,5,6,7,8,9,10][::-1])
# ans1 = sorted([11,2,32,14,53,36,24,13,324,1])
# ans2 = sorted([10,3,33,15,55,43,25,31,4,0])
# ll.add_nodes(ans1)
# ll1.add_nodes(ans2)
# merge_sort(ll.head,ll1.head)

# ll.find_length()
# # ll.reverse_the_linked_list()
# ll.print_linkedlist() 
# ll.add_nodes([1,2,1])
# ll.palindrome_or_not()
# # ll.print_linkedlist() 

# common_node_in_linked_list()   
# ll.add_two_numbers()         



def valid_parenthesis(string):
    valid = [False] * len(string)
    stack = []
    for i,ch in enumerate(string):
        if ch == "(":
            stack.append(i)
        elif ch == ")":
            if stack:
                valid[i] = True
                valid[stack.pop()] = True
        else:
            valid[i] = True 
    ans = ""
    ans += ''.join([string[i] for i in range(len(string)) if valid[i]])
    print(ans)
valid_parenthesis("((abc)((de))")
valid_parenthesis("((de)()()))(ab(c)))")