#stack = 📦
# yesterday exam prefix to postfix conversion
s = '*+AB-CD'

s = s[::-1]
stack = []
for i in s:
    if i.isalpha():
        stack.append(i)
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(f"{a}{b}{i}")
# print(stack[-1]) # prefix to postfix

# postfix to prerfix
postfix = 'ABC/-AK/L-*'
s = stack[-1]
for i in s:
    if i.isalpha():
        stack.append(i)
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(f"{a}{b}{i}")
# print(stack[-1][::-1])



#infix to postfix

def priority(char):
    if char in"^":
        return 3
    elif char in "*/":
        return 2
    elif char in "+-":
        return 1
    else:
        return -1
stack = []
string = "(a-b/c)*(a/k-l)"
ans = ""
for i in string:
    if i.isalpha():
        ans+=i
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            ans+=stack.pop()
        stack.pop()
    else:
        while stack and priority(i) <= priority(stack[-1]):
            ans+=stack.pop()
        stack.append(i)
while stack: ans+=stack.pop()          
# print(ans)


#infix to prefix
# revese the infix

string = "(a-b/c)*(a/k-l)"
ans =""
stack =[]
string = string[::-1] # reverse the string do the same thing like converstion to infix to postfix
string = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in string])
def priortity(char):
    if char =="^":
        return 3
    elif char in "*/":
        return 2
    elif char in "+-":
        return 1
    else: return 0

for i in string:
    if i.isalpha():
        ans+=i
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            ans+=stack.pop()
        stack.pop()
    else:
        while stack and priority(i) <= priortity(stack[-1]):
            ans+=stack.pop()
        stack.append(i)
while stack: ans+=stack.pop()
# print("infix to prefix", ans[::-1])
    


stack = ['15','3','+','6','2','-','*']
ans = []
for i in stack:
    if i.isdigit():
        ans.append(i)
    else:
        b = int(ans.pop())
        a = int(ans.pop())
        if i == "+":
            ans.append(a+b)
        elif i == "-":
            ans.append(a-b)
        elif i == '*':
            ans.append(a*b)
# print(ans[-1])
            
            
# optmised version🔥🔥
stack = ['15','3','+','6','2','-','*']
ans = []

operation = {
    '+': lambda a,b :a+b,
    '-': lambda a,b :a-b,
    '*': lambda a,b :a*b,
    '/': lambda a,b :a/b,
    '%': lambda a,b :a%b
}

for i in stack:
    if i.isdigit():
        ans.append(i)
    else:
        b = ans.pop()
        a = ans.pop()
        ans.append(operation[i] (int(a),int(b)))
        
# print(ans[-1])

#convert the string into postfix then print the actual ans

string = "( 15 + 3 ) * ( 6 - 2 )".split()

def priortity(char):
    if char == '^': return 3
    elif char in "*/": return 2
    elif char in "+-": return 1
    else: return 0

def infix_to_postfix(string):
    stack = []
    ans = []
    for i in string:
        if i.isdigit(): ans.append(i)
        elif i == "(": stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                ans.append(stack.pop())
            stack.pop()
        else:
            while stack and priority(i) <= priority(stack[-1]):
                ans.append(stack.pop())
            stack.append(i)
    while stack: ans.append(stack.pop())
    return ans

def answer(stack):
    ans = []

    operation = {
        '+': lambda a,b :a+b,
        '-': lambda a,b :a-b,
        '*': lambda a,b :a*b,
        '/': lambda a,b :a/b,
        '%': lambda a,b :a%b
    }

    for i in stack:
        if i.isdigit():
            ans.append(i)
        else:
            b = ans.pop()
            a = ans.pop()
            ans.append(operation[i] (int(a),int(b)))
            
    # print(ans[-1])                                                                                                              
ans = infix_to_postfix(string)
# answer(ans)



#vaild parenthesis
string = '(({}))'
string = '()[]{}('
string = '([[]])(([]))'
stack = []
compare = {')':'(' ,']':'[','}':'{'}
for i in string:
    if i in compare.values():
        stack.append(i)
    else:
        if not stack and compare[i] != stack[-1]:
            break
        stack.pop()
# print("NotValid" if stack else "Valid")


# #method 01
# find first largest element fro list1 elements from the list2

list1 = [4,1,2]
list2 = [2,1,3,4]
ans = []
for i in list1:
    flag = True
    go_in = False
    for j in list2:
        if flag and i == j:
            flag = False
            go_in = True
        elif go_in:
            if i < j:
                ans.append(j)
                break
    else:
        ans.append(-1)
# print(ans)

#method 02
list1 = [4,1,2]
list2 = [2,1,3,4]
ans = []
matching = dict()
for i in list2:
    while ans and ans[-1] < i:
        matching[ans.pop()] = i
    ans.append(i)
 
while ans: matching[ans.pop()] = -1

for i in list1: ans.append(matching[i])
# print(ans)


#we have sorted with full of dupicates
arr = [2,2,2,3,3,4,5,5,6,6,6,10,10]
            

        
# 🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳Trees🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲🌳🌲
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
# inserting nodes      
def insert(root,data):
    if not root:
        return Node(data)
    elif data < root.data:
        root.left = insert(root.left,data)
    else: 
        root.right = insert(root.right,data)
    return root

# tree traversals
def traversal(value,root):
    if root:
        traversal('left',root.left)
        print(value, root.data)
        traversal('right',root.right)
        
def inorder_traversal(root):
    if root:
        traversal(root.left)
        print(root.data,end=" ")
        traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.data,end=" ")
        traversal(root.left)
        traversal(root.right)
        
def postorder_traversal(root):
    if root:
        traversal(root.left)
        traversal(root.right)
        print(root.data,end=" ")
        
#balanced tree
def balanced(root,arr):
    if not arr:
        return None
    n = len(arr) // 2
    root = Node(arr[n])
    root.left = balanced(root.left,arr[:n])
    root.right = balanced(root.right,arr[n+1:])
    return root 

def height_of_tree(root):
    if not root:
        return 0
    return 1 + max(height_of_tree(root.left),height_of_tree(root.right))

def balanced_Tree(root):
    if not root:
        return
    return (height_of_tree(root.left) - height_of_tree(root.right))

# functional method
def sum_of_nodes_in_tree(root):
    if not root:
        return 0
    return root.data + sum_of_nodes_in_tree(root.left) + sum_of_nodes_in_tree(root.right)

# parameterised method
def _sum_of_nodes_in_tree(maxi,root):
    if not root:
        return maxi
    maxi+=root.data
    maxi = _sum_of_nodes_in_tree(maxi,root.left)
    maxi = _sum_of_nodes_in_tree(maxi,root.right)
    return maxi


#sum of even node in the tree:
# method 01 
def sum_of_even_nodes(root):
    if not root:
        return 0
    elif not root.data & 1:
        return root.data + sum_of_even_nodes(root.left) + sum_of_even_nodes(root.right)
    return sum_of_even_nodes(root.left) + sum_of_even_nodes(root.right)
    
#method 02
def _sum_of_even_nodes(root):
    if not root: return 0
    elif not root.data & 1: k = root.data
    else: k = 0
    return k + _sum_of_even_nodes(root.left) + _sum_of_even_nodes(root.right)

def search_element(root,key):
    if not root:
        return "Not Found"
    elif root.data == key:
        return "Found"
    elif root.data < key:
        return search_element(root.right,key)
    else:
        return search_element(root.left,key) 
       
root = None  
arr = [10,1,22,33,4,5]
for i in arr:
    root = insert(root,i)
# root = balanced(root,arr)
# print(height_of_tree(root))
# print(balanced_Tree(root))
traversal('root',root)
# print(sum_of_nodes_in_tree(root))
# print(_sum_of_nodes_in_tree(0,root))
# print(sum_of_even_nodes(root))
print(search_element(root,10))