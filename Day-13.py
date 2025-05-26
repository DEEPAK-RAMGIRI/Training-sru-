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
        if not self.head:
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
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
        
        
        
        
    # method 01
    # def reverse_linked_list(self):
    #     prev = None
    #     temp = self.head
    #     while temp:
    #         nextnode = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = nextnode
         
    #     self.head = prev
    
    #method 02 same as above but with less lines 😏
    def reverse_linked_list(self):
        prev,temp = None,self.head
        while temp:
            nextnode,temp.next = temp.next,prev
            prev,temp = temp,nextnode
        self.head = prev
        
        
    def remove_element_from_first(self):
        if not self.head:
            return None
        self.head = self.head.next
        
    def remove_element_from_last(self):
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        
        
    def sum_of_all_nodes(self):
        ans = 0
        temp = self.head
        while temp:
            ans += temp.data
            temp = temp.next
        print(ans)
        
    def sum_of_all_even_occurenece(self):
        ans = 0
        temp = self.head
        while temp:
            ans += temp.data if not temp.data & 1 else 0
            temp = temp.next
        print(ans)
    

    def recursion_sum_of_odd_occurence_and_even_occurence(self):
        def function(node):
            if not node:
                return 0, 0
            odd_sum, even_sum = function(node.next)
            if node.data & 1:
                odd_sum += node.data
            else:
                even_sum += node.data
            return odd_sum, even_sum

        odd, even = function(self.head)
        print("Odd Sum:", odd)
        print("Even Sum:", even)
        
        
    def sum_of_all_even_position(self):
        ans = 0
        temp = self.head
        count = 1
        while temp:
            ans += temp.data if not count & 1 else 0
            count += 1
            temp = temp.next
        print(ans)
        
    def secound_larget(self):
        secound = first = 0
        temp = self.head
        while temp:
            if temp.data > first:
                secound = first
                first = temp.data
            elif temp.data !=first and temp.data > secound :
                secound = temp.data                
            temp = temp.next
        print(first,secound)
        
        
    def countingues_sum_subarray(self,target):
        temp1 = self.head
        temp2 = self.head
        count = ans = 0
        while temp1:
            ans += temp1.data
            while temp1 != temp2 and ans > target:
                ans -= temp2.data
                temp2 = temp2.next
            if ans == target:
                count+=1
            temp1 = temp1.next
        print(count)

        
    def sum_continues_pair(self,target):
        temp = self.head
        count = 0
        while temp and temp.next:
            if temp.data + temp.next.data == target:
                count+=1
            temp =temp.next
        print(count)
        
    #find count of all possible pair is less than k but continouse
    def count_continues_pair_whose_sum_is_less_then_k(self,target):
        temp = self.head
        count = 0
        while temp and temp.next:
            if temp.data + temp.next.data <= target:
                count+=1
            temp =temp.next
        print(count)
        
     #find count of all possible pair is less than k but all possible pairs
    def possible_pairs(self,k):
        temp1 = self.head
        count = 0
        while temp1:
            temp2 = temp1.next
            while temp2:
                if temp1.data + temp2.data < k:
                    print([temp1.data,temp2.data])
                    count+=1 
                temp2 = temp2.next
            temp1 = temp1.next
        # print(count)
        
    # given sorted linked list and print the secound of the linked list
    def secound_half(self):
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        self.head = slow
    
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head.next
       
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data) 
        
    #method 01
    def kth_last_node(self,k):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        temp =self.head
        if count < k:
            print(None)
            return
        for _ in range(count-k):
            temp = temp.next
        print(temp.data)
        
    #method 02 optimised version 🔥
    def kth_last_node2(self,k):
        slow = self.head
        fast = self.head
        
        for _ in range(k):
            if not fast:
                print(None)
                return
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        print(slow.data)
        
    def delte_kth_last_node(self,k):
        slow = self.head
        fast = self.head
        
        for _ in range(k):
            if not fast:
                print(None)
                return
            fast = fast.next
        # If fast is None after moving k steps, delete head
        if not fast:
            self.head = self.head.next
            return
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev: prev.next = slow.next
        
    
    
    def swap_2_element(self):
        temp = self.head
        prev = None
        while temp and temp.next:
            temp.data,temp.next.data = temp.next.data,temp.data
            temp = temp.next.next       
            
            
    def perform_buble_sort(self,ans):
        while True:
            temp2 = self.head
            flag = True
            k-=1
            if k == 0:
                break
            while temp2 and temp2.next:
                if temp2.data > temp2.next.data:
                    temp2.data,temp2.next.data = temp2.next.data,temp2.data
                    flag =False
                temp2 = temp2.next
            
            if flag: break
        self.kth_largest()
            
    #print the kth lagest element in the unsoerted list
    def kth_largest(self,k):
        #performing bubble sort
        a = k
        while True:
            temp2 = self.head
            flag = True
            k-=1
            if not k:
                break
            while temp2 and temp2.next:
                if temp2.data > temp2.next.data:
                    temp2.data,temp2.next.data = temp2.next.data,temp2.data
                    flag =False
                temp2 = temp2.next
            if flag: break
        self.kth_last_node2(a)
        
    def cycle_in_linkedlist(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("cycle exists")
                break
        else:
            print("not exists")
        
        
            
    #selection sort
    def selection_sort(self):
        temp = self.head
        while temp:
            mini = temp
            temp2 = temp.next
            while temp2:
                if mini.data > temp2.data:
                    mini = temp2
                temp2 = temp2.next
            temp.data,mini.data = mini.data,temp.data 
            temp = temp.next
        
          
arr1 = [10,9,8,7,6,5,4,3,2,1]   
arr1=[1,2,0,3,4]
arr1 =[5,2,4,7,3,6,5,8,9]
k = 10
ll = Linkedlist()
# for i in arr1:
#     ll.add_front(i)
# ll.print_linked_list()
for i in arr1:
    ll.add_last(i)
# ll.print_linked_list()
# ll.add_middle(22.5)
# ll.reverse_linked_list()
# ll.remove_element_from_first()
# ll.remove_element_from_last()
# ll.sum_of_all_nodes()
# ll.sum_of_all_even_occurenece()
# ll.sum_of_all_even_position()
# ll.recursion_sum_of_odd_occurence_and_even_occurence()
# ll.secound_larget()
# ll.countingues_sum_subarray(3)
# ll.sum_continues_pair(k)
# ll.count_continues_pair_whose_sum_is_less_then_k(k)

# ll.possible_pairs(k)
# ll.secound_half()
# ll.print_linked_list()
# ll.find_middle_node()
# ll.kth_last_node(2)

# ll.kth_last_node2(2)
# ll.swap_k_elements(2)
# ll.swap_2_element()
# ll.perform_buble_sort()

# ll.kth_largest(3)
ll.selection_sort()
ll.print_linked_list()

