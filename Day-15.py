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
            
    print(ans[-1])       
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
ans = []
matching = dict()
for i in list2:
    while ans and ans[-1] < i:
        matching[ans.pop()] = i
    ans.append(i)
    
while ans: matching[ans.pop()] = -1

for i in list1: ans.append(matching[i])
print(ans)


#we have sorted with full of dupicates
arr = [2,2,2,3,3,4,5,5,6,6,6,10,10]
            

        
    