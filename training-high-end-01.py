#exam
#Delete Node from the mid point of Linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def insert(arr,head):
    head = Node(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = Node(i)
        temp = temp.next
    return head

def printing(head):
    temp = head
    while temp:
        print(temp.data,end= " ")
        temp = temp.next
        
        
# Time Complexcity O(n)
#Space Complexcity O(1)
        
def delete_middle_element(head):
    if not head  or not head.next:
        return None
    fast = head.next.next
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head


#Time COmplexcity O(n)
#Space Complexcity O(1)
def rotate_linked_list(head,k):
    if not head or not head.next:
        return head
    
    temp = head
    count = 1
    
    while temp.next:
        temp = temp.next
        count+=1
        
    k %= count
    
    temp1 = head
    for _ in range(k-1):
        temp1 = temp1.next
        
    new_head = temp1.next
    
    temp1.next = None
    temp.next = head
    return new_head



def cycle_in_linked_list(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False 
arr = [1,2,3,4,5,6]
head = None
head = insert(arr,head)
# delete_middle_element(head)
head=rotate_linked_list(head,2)
printing(head)

class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
def insert_dll(head,arr):
    head = Node2(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = Node2(i)
        temp.next.prev = temp
        temp = temp.next
    return head

def printing_dll(head):
    while head.next:
        print(head.data,end=" ")
        head = head.next
    while head:
        print(head.data,end=" ")
        head = head.prev    
        
        
    

#Swap a secound Node with the last Node
#Time Complexcity O(n)
#Space Complexcity O(1)
def swap(head):
    if not head or not head.next: return None
    temp = head
    count = 1
    secound = None
    while temp.next:
        if count == 2:
            secound = temp
        temp  = temp.next
        count+=1
    secound.data,temp.data = temp.data,secound.data
    return head


def swap2(head):
    if not head or not head.next: return head
    secound = head.next
    temp = head
    while temp.next:
        temp = temp.next
    secound.data,temp.data =temp.data,secound.data
    return head 

#Time Complexcity O(n ^ 2)
#space Complexcity O(1)
def sort(head):
    if not head or not head.next: return head
    temp = head
    changed = True
    while changed:
        changed = False
        temp = head
        while temp.next:
            if temp.data > temp.next.data:
                temp.data,temp.next.data = temp.next.data,temp.data
                changed = True
            temp = temp.next
    return head
        
        
def find_middle(head):
    prev = None
    fast = head
    slow = head
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    if prev:
        prev.next = None
    return slow


def conquer(first,secound):
    dummy = Node2(0)
    temp = dummy
    
    while first and secound:
        if first.data > secound.data:
            temp.next = secound
            secound = secound.next
        else:
            temp.next = first
            first = first.next
        temp.next.prev = temp
        temp = temp.next

    if first: 
        temp.next = first
        first.prev = temp
    else: 
        temp.next = secound
        secound.prev = temp
    return dummy.next
        
def merge(head):
    if head and head.next:
        mid = find_middle(head)
        first = merge(head)
        secound = merge(mid)
        return conquer(first,secound)
    return head
        
        
        


head = None
arr=[1,3,4,2,5,7,6]
head = insert_dll(head,arr)
# # head = swap(head)
# head = swap2(head)
print()
# head = sort(head)
head = merge(head)
printing(head)