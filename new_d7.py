# palindrome recursion
string = 'aba'

def palindrome(string,left,right):
    while left >= 0 and  right < len(string) and string[left] == string[right]:
        left-=1
        right+=1
    return (string[left+1:right] == string[right:left+1])
count = [0]
def function(i):
    if i == len(string): 
        return count[0]
    if palindrome(string,i,i):
        count[0]+=1
    if palindrome(string,i,i+1):
        count[0]+=1
    function(i+1)
# function(0)
# print(count[0])

n = 4
def function(i):
    if not i : return 1
    elif i < 0: return 0
    return function(i-1) + function(i-2) + function(i-3)
print(function(n))

        
    
    