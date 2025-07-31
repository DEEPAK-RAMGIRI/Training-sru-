class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None
        self.height = 0
        
def height(root):
    return root.height if root else -1  
    
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
        
def get_max_node(root):
    while root.right:
        root = root.right
    return root

def delete_node(root, key):
    if not root:
        return None

    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            temp = get_max_node(root.left)
            root.data = temp.data
            root.left = delete_node(root.left, temp.data)

    root.height = 1 + max(height(root.left), height(root.right))


    hd = diffheight(root)
    
    if hd > 1 and diffheight(root.left) >= 0:
        return right_rotation(root)
    
    if hd > 1 and diffheight(root.left) < 0:
        root.left = left_rotation(root.left)
        return right_rotation(root)
    
    if hd < -1 and diffheight(root.right) <= 0:
        return left_rotation(root)
    
    if hd < -1 and diffheight(root.right) > 0:
        root.right = right_rotation(root.right)
        return left_rotation(root)

    return root
  
arr = [25,6,1,23,12,78,34,54,21,90,78]
# arr = [25,78,34,90,54]
# arr = [10,11,12]
# arr = [5,7,6]
root = None
for i in arr:
    root = insert(root,i)
traversal("root",root)









# =================================================== After Noon Session =========================================


# Undirected graphsfrom collections import defaultdict, deque

from collections import defaultdict,deque
class UndirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def send_auto_accepted_friend_request(self, x, y):
        self.graph[x].append(y)
        self.graph[y].append(x)

    def is_friend(self, x, y):
        return y in self.graph[x]

    def remove_friend(self, x, y):
        if self.is_friend(x, y):
            self.graph[x].remove(y)
            self.graph[y].remove(x)
        else:
            print("Friend not found")

    def get_friends(self, x):
        print(", ".join(map(str, self.graph[x])))


class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def follow(self, fan, cel):
        self.graph[cel].append(fan)

    def is_following(self, fan, cel):
        return fan in self.graph[cel]

    def unfollow(self, fan, cel):
        if self.is_following(fan, cel):
            self.graph[cel].remove(fan)
        else:
            print("No such fan in the celebrity's circle")

    def get_followers(self, cel):
        print(", ".join(map(str, self.graph[cel])))


class WeightedGraph:
    def __init__(self):
        self.routes = defaultdict(list)

    def establish_route(self, source, destination, toll_price):
        self.routes[source].append((destination, toll_price))
        self.routes[destination].append((source, toll_price))

    def report_road_damage(self, source, destination):
        print(f"Damage reported on route {source} - {destination}")

    def get_toll_price(self, source, destination):
        for dest, price in self.routes[source]:
            if dest == destination:
                print(price)
                break

    def get_all_routes(self, source):
        for dest, _ in self.routes[source]:
            print(dest)


class GraphTraversal:
    def __init__(self, graph_dict, n):
        self.graph = graph_dict
        self.visit = [False] * n

    def bfs(self, index):
        queue = deque([index])
        self.visit[index] = True
        while queue:
            curr = queue.popleft()
            for neighbor in self.graph[curr]:
                if not self.visit[neighbor]:
                    self.visit[neighbor] = True
                    queue.append(neighbor)

    def dfs(self, index):
        self.visit[index] = True
        for neighbor in self.graph[index]:
            if not self.visit[neighbor]:
                self.dfs(neighbor)
