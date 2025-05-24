string = "abcdecfbgce"

string = "abcdaecdb"
# string ="abcdbef"
# string ="abcda"
# string = "abfehcbdaf"
# string = "abcdcecdb"
# string = "abcdcecda"

#Time complexcit is O(n)

left = 0
seen =dict()
maxi = 0
for right in range(len(string)):
    if string[right] in seen:
        left = max(left,seen[string[right]])
    seen[string[right]] = right
    maxi = max(maxi,right - left)
# print(maxi)


# print the longest substring which have m,n
string = "abcdedacefaebg"
m,n = 'c','d'

left = 0
seen =dict()
maxi = 0
for right in range(len(string)):
    if string[right] in seen:
        left = max(left,seen[string[right]])
    seen[string[right]] = right
    if m in seen and n in seen:
        maxi = max(maxi,right - left)
print(maxi)



    
    