class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None
        self.height = 0
        
def height(root):
    return root.height if root else 0  
    
def diffheight(root):
    return height(root.left) - height(root.right) if root else 0  

def right_rotation(root):
    x = root.left
    temp = x.right
    x.right = root
    root.left = temp
    root.height=  1 + max(height(root.left), height(root.right))
    x.height = 1 + max(height(x.left),height(x.right))
    return x


def left_rotation(root):
    x = root.right
    temp = x.left
    x.left = root
    root.right = temp
    root.height=  1 + max(height(root.left), height(root.right))
    x.height = 1 + max(height(x.left),height(x.right))
    return x

     
def insert(root,data):
    if not root: 
        return Node(data)
    if data == root.data:
        return root 
    elif root.data > data:
        root.left = insert(root.left,data)
    else:
        root.right = insert(root.right,data)
    
        

    root.height = 1 + max(height(root.left), height(root.right))
    hd = diffheight(root)
    
    if hd > 1 and root.left.data > data:
        root = right_rotation(root)
    if hd < -1 and root.right.data < data:
        root = left_rotation(root)
        
    if hd > 1 and root.left.data < data:
        root.left = left_rotation(root.left)
        root = right_rotation(root)
    
    if hd < -1 and root.right.data > data:
        root.right = right_rotation(root.right)
        root = left_rotation(root)
    
    return root
    
def traversal(direction,root):
    if root:
        traversal(direction + '.left ',root.left)
        print(f"{direction,(root.data),root.height}")
        traversal(direction + '.right',root.right)
        
    
arr = [25,6,1,23,12,78,34,54,21,90,78]
# arr = [25,78,34,90,54]
# arr = [10,11,12]
# arr = [5,7,6]
root = None
for i in arr:
    root = insert(root,i)
traversal("root",root)
    
    
 
# Min heap
arr = []

def bubbleup(index):
    while index > 0  and arr[index] < arr[(index - 1)// 2]:
        arr[index],arr[(index - 1)// 2]= arr[(index - 1)// 2],arr[index]
        index = (index - 1) // 2
        
        
def bubble_down(index):
    while True:
        smallest = index
        left = 2 * index + 1
        right= 2 *index + 2

        if left < len(arr) and arr[left] < arr[smallest]:
            smallest = left
        
        if right < len(arr) and arr[right] < arr[smallest]:
            smallest = right
        if smallest != index:
            arr[smallest],arr[index] = arr[index],arr[smallest]
        else:
            break
        
        
def delete_element(element):
    if element not in arr:
        print("element not found")
        return
    index = arr.index(element)
    arr[index],arr[-1] = arr[-1],arr[index]
    arr.pop()
    bubbleup(index)
    bubble_down(index)
    
def get_top():
    arr[0],arr[-1] = arr[-1],arr[0]
    temp = arr.pop()
    bubble_down(0)                
    return temp

def insertion(n):
    arr.append(n)
    bubbleup(len(arr)-1)
temp  = [10, 80, 40, 10, 9, 800, 5, 10, 800, 3, 23, 1, 2, 3, 10, 6, 9]
        # [1, 5, 2, 6, 10, 3, 3, 10, 800, 10, 23, 800, 9, 40, 10, 80]
        
for i in temp:
    insertion(i)
print(arr)

