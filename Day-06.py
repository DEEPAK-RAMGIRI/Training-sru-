# make a bubble sort
#method 01
arr = [3,4,1,5,68,34,12,67767,3,1,2,3,4,0]
arr = [5,2,3,8,1,6,7,4]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr,"\n")

# method 02 optimised version
# using flag
arr = [2,5,8,6,3,1,9,4,7]
for i in range(len(arr)-1):
    flag = True
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            flag = False
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if flag:
        break
# print(arr,"\n")
 
        
# here we are not going to sort first and last k digits       
k = 2
arr = [5,2,3,8,1,6,7]
for i in range(len(arr)-1):
    for j in range(k,len(arr)-i-1-k):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)

#print the kth largest element using bubble sort

k = 5
arr = [2,5,8,6,3,1,9,4,7]   
for i in range(len(arr)-1):
    if i == k-1:
        break
    flag = True
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            flag = False
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if flag:
        break
# print(arr[-k])


# sort the alphabets using bubble sort

alpha = ['e','c','a','b','f']

for i in range(len(alpha)-1):
    flag = True
    for j in range(len(alpha)-i-1):
        if ord(alpha[j]) > ord(alpha[j+1]):
            flag = False
            alpha[j],alpha[j+1] = alpha[j+1],alpha[j]

    if flag:
        break
# print(alpha,"\n")


#given 2d list every row have 2 elements [[2,3],[5,1],[1,4],[2,7],[1,3]]
#output should be [[5,1],[2,3],[1,3],[1,4],[1,4],[2,7]]

list1 = [[2,3],[5,1],[1,4],[2,7],[1,3]]
for i in range(len(list1)-1):
    flag = False
    for j in range(len(list1)-i-1):
        if list1[j][-1] > list1 [j+1][-1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
            flag = True
    if not flag:
        break
# print(list1)



#string comparsion done manually in the python
#compare string lexicographically condtion: if first ele[0] == secound ele[0] check for 
#first ele[1] and secound ele[1] if they are just append them normally else swap ther positions
  
# alpha = ["hello","cat","apples","he"]
# alpha = ["zebra","car","apple","cat"]
# alpha = ["cat","zebra","car","apple"]
alpha = ['school','car','hello','apple','cat','bat']
for i in range(len(alpha)-1):
    flag = True
    for j in range(len(alpha)-i-1):
        if alpha[j][0] == alpha[j+1][0]:
            flag = False
            if len(alpha[j]) > 2 and len(alpha[j+1])  and alpha[j][1] > alpha[j+1][1]:
                alpha[j],alpha[j+1] = alpha[j+1],alpha[j]
                break
        elif alpha[j][0] > alpha[j+1][0]:
            flag = False
            alpha[j],alpha[j+1] = alpha[j+1],alpha[j]
    if flag:
        break
# print(alpha)


# bubble sort we have 3 ele one is prime and other is not
#[
    # [4,13,12],
    # [8,10,5],
    # [7,9,20],
    #[14,8,3]
# ]        

# output = [[14,8,3],[8,10,5],[7,9,20],[4,13,12]] sort accordingly with prime number
#method 01
arr = [
     [4,13,12],
     [8,10,5],
     [7,9,20],
    [14,8,3]
]     
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def first_prime(row):
    for num in row:
        if is_prime(num):
            return num
    return float('inf')

n = len(arr)
for i in range(n - 1):
    flag = True
    for j in range(n - i - 1):
        if first_prime(arr[j]) > first_prime(arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            flag = False
    if flag: break

# print(arr)


#method 02 optimised version using dict
arr = [
    [4, 13, 12],
    [8, 10, 5],
    [7, 9, 20],
    [14, 8, 3]
]     

hashmap = {}

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_primes(i, row):
    for num in row:
        if is_prime(num):
            hashmap[i] = num 
            return

def loop(arr):
    for i in range(len(arr)):
        find_primes(i, arr[i])

loop(arr)

for i in range(len(arr)-1):
    flag  = True
    for j in range(len(arr)-i-1):
        if hashmap.get(j) > hashmap.get(j+1):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            hashmap[j], hashmap[j+1] = hashmap[j+1], hashmap[j] 
            flag = False
    if flag: break
            
        
# print(hashmap
# print(arr)


#using array
res = []
def find_primes(row):
    for num in row:
        if is_prime(num):
            res.append(num)

def loop(arr):
    for i in range(len(arr)):
        find_primes(arr[i])

loop(arr)

for i in range(len(arr)):
    flag = True
    for j in range(len(arr)-i-1):
        if res[j] > res[j+1]:
            res[j],res[j+1] = res[j+1],res[j]
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag =False
    if flag: break
print(arr)
    
            