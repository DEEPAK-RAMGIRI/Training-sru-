# Maximum Points You Can Obtain from Cards 
# Method 01
#Time Complexcity O(k)
#Space Complexcity O(1)
cardPoints = [1,2,3,4,5,6,1]
k = 3
total = maxi = sum(cardPoints[:k])
j = len(cardPoints) - 1
for i in range(k-1,-1,-1):
    maxi = maxi - cardPoints[i] + cardPoints[j]
    j-=1
    total = max(total,maxi)
print(total)
    



#Time Complexcity O(k)
#Space Complexcity O(1)
cardPoints = [1,2,3,4,5,6,1]
k = 3
total = maxi = sum(cardPoints[:k])
for i in range(k):
    maxi = maxi + cardPoints[~i] - cardPoints[k-i-1] 
    total = max(total,maxi)
print(total)
