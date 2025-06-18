# Maximum Points You Can Obtain from Cards

# Method 01
#Time Complexcity O(k)
#Space Complexcity O(1)
cardPoints = [1,2,3,4,5,6,1]
k = 3
total = maxi = sum(cardPoints[:k])
j = len(cardPoints) - 1
for i in range(k-1,-1,-1):
    maxi += cardPoints[j] - cardPoints[i]
    j-=1
    total = max(total,maxi)
# print(total)
 
#Method 02   
#Time Complexcity O(k)
#Space Complexcity O(1)
cardPoints = [1,2,3,4,5,6,1]
k = 3
total = maxi = sum(cardPoints[:k])
for i in range(k):
    maxi += cardPoints[~i] - cardPoints[k-i-1] 
    total = max(total,maxi)
# print(total)

#Time Complexcity O(n^2)
#Space Complexcity O(1)

s = "abciiidef"
k = 3
maxi = 0
vowels = {'a','e','i','o','u'}
for i in range(len(s)-k+1):
    count = 0
    for j in range(i,k+i):
        if s[j] in vowels:
            count+=1
    maxi = max(maxi,count)
# print(maxi)

# Time Complexcity O(n)
#Space Complexcity O(1)
s = "abciiidef"
k = 3
left = count = maxi = 0
vowels = {'a','e','i','o','u'}
for right in range(len(s)):
    if s[right] in vowels:
        count+=1
    if right - left + 1 > k:
        if s[left]in vowels:
            count-=1
        left+=1
    maxi = max(maxi,count)

print(maxi)
