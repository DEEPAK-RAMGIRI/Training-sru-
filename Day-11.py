arr1 = [0,3,8,1,5,7,9]
arr2 = [5,6,10,2,6,9,11]

 
# finding the possible max intervals 
time_intervals = []

i= 0
while i < len(arr1):
    time_intervals.append([arr1[i],arr2[i]])
    i+=1
#instead of while loop use zip
#here it will convert to tuple instead of use list bcoz tuple is immutable
# for i in zip(arr1,arr2):
#     time_intervals.append(i)

time_intervals.sort(key = lambda x:(x[-1],x[0])) # sorting the time_intervals values
# print(time_intervals)
count = 1
last = time_intervals[0]

for i in range(1,len(time_intervals)):
    if last[-1] < time_intervals[i][0]:
        # print(last,end=" ")
        last = time_intervals[i]
        count+=1
        
# print(last,end=" ")
# print(count)

#merging intervals
ans = []
ans.append(time_intervals[0])
for i in range(1,len(time_intervals)):
    if ans[-1][-1] > time_intervals[i][0]:
        ans[-1][0] = min(ans[-1][0],time_intervals[i][0])
        ans[-1][-1]= max(ans[-1][0],time_intervals[i][-1])
    else:
        ans.append(time_intervals[i])
# print(ans)



# string = "aaabbaaaacccddeff"
# string="abbacbababc"
# left = 0
# for right in range(1,len(string)):
#     if string[right] != string[right-1]:
#         print(string[right-1],right-left,end=" ")
#         left = right
# print(string[right],len(string)-left,end=" ")

#reverse the string without changing the vowels but u can change the vowels

string = "hippopotamus"
string = list(string)
vowels = "aeiou"
left = 0
right = len(string) -1
while left < right:
    while left < right and string[left] in vowels:
        left+=1
    while left < right and string[right] in vowels:
        right-=1
    string[left],string[right] = string[right],string[left]
    left+=1
    right-=1
# print(''.join(string))
    
# find the subarray value in the k size contiguous array
#Time Complexcity O(n)
#Space Complexcity O(1)

arr = [2,1,6,4,2,3,1,1,4,2,6,7,3]
k = 5
maxi = sum(arr[:k])
ans = maxi
left = 0
for right in range(k,len(arr)):
    maxi +=  (arr[right]-arr[left])
    left+=1
    ans= max(maxi,ans)
# print(ans)


# find the longest subarray with smallest sum
maxi = float("inf")
arr = [2,1,6,4,2,3,1,1,4,2,6,7,3]
for i in range(len(arr)):
    currsum = arr[i]
    for j in range(i+1,len(arr)-1):
        currsum += arr[j]
        if  currsum < maxi:
            maxi = currsum
            ans = arr[i:j+1]
# print(ans)

#printing the length longest subarray whose sum is k
#Time Complexcity O(n)
arr = [2, 1, 6, 4, 2, 3, 1, 1, 4, 2, 6, 7, 3]
left = 0
k = 11
ans = 0
maxlen = -1
res = []
for right in range(len(arr)):
    ans += arr[right]
    while left < right and ans > k:
        ans -= arr[left]
        left+=1
    if ans == k:
        maxlen = max(maxlen,right - left + 1)
        res.append(arr[left:right+1])
# print(maxlen)   
# print(res)
    
#length of the largest substring
#Time Complexity: O(n²)

#method 01
def checkpalindrome(s,left,right):
    while left >=0 and right < len(s) and s[left] == s[right]:
        left-=1
        right+=1
    return s[left+1:right]
s = 'ababba'
maxlen = ""
for i in range(len(s)):
    odd_oc = checkpalindrome(s,i,i)
    even_oc = checkpalindrome(s,i,i+1)
    maxlen = max(maxlen,odd_oc,even_oc,key = len)
# print(maxlen)
# print(len(maxlen))


#method 02

def checkpalindrome(s,left,right):
    while left >=0 and right < len(s) and s[left] == s[right]:
        left-=1
        right+=1
    return (right - left - 1)
s = 'ababba'
maxlen = 0
for i in range(len(s)):
    odd_oc = checkpalindrome(s,i,i)
    even_oc = checkpalindrome(s,i,i+1)
    maxlen = max(maxlen,odd_oc,even_oc)
# print(maxlen)


#method 03
# Time Complexcity O(n^2)
maxi = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i:j+1] == s[i:j+1][::-1]:
            maxi = max(maxi,(j - i + 1)) 
# print(maxi)   


#print all substring with length k
s ="abba"
count = 0
substring = []
for i in range(len(s)):
    string = ""
    for j in range(i,len(s)):
        string += s[j]
        substring.append(string)
        count+=1
# print(substring)
# print(count)

#find it in using recursion at hostel :)
res = []
def substring_len_k(i,j):
    if i == len(s):
        return
    if j == len(s):
        substring_len_k(i+1,i+1)
        return
    res.append(s[i:j+1])
    substring_len_k(i,j+1)
        
        
substring_len_k(0,0)  
print(res)

# string = "abcdaecdb"
# string ="abcdbef"
string ="abcda"
string = "abfehcbdaf"

left = 0
count = 0
seen_or_not = set()

#find the length of longest substring without repeating characters
#Time Complexcity O(n)

for right in range(len(string)):
    if string[right] in seen_or_not:
        while string[left] in seen_or_not:
            seen_or_not.remove(string[left])
            left+=1
    seen_or_not.add(string[right])
    count = max(count,(right-left+1))
# print(count)

# using dictionary


# string = "abcdaecdb"
string ="abcdbef"
# string ="abcda"
# string = "abfehcbdaf"
# string = "abcdcecdb"
string = "abcdcecdb"
seen = {}
start = 0
max_len = 0

for i in range(len(string)):
    if string[i] in seen and seen[string[i]] >= start:
        start = seen[string[i]] + 1
    seen[string[i]] = i
    max_len = max(max_len, i - start + 1)

# print(max_len)

    
    
    
    

    