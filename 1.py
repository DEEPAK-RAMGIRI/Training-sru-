# remove digit from the string so ans will max

no = "551"
digit = "5"

no = "1231"
digit = "1"

no = "123"
digit = "3"
ans = float("-inf")
for i in range(len(no)):
    if no[i] == digit:
        ans = max(ans,int(no[:i] + no[i+1:]))

print(ans if ans != float("inf") else -1)
         
    