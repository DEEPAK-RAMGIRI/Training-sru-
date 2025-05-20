# find the floor value of no
n = 54
left = 0
right = n
while left <=  right:
    mid = left + ((right - left) >> 1)
    square = mid * mid 
    if n == square:
        print(mid)
        break
    elif square <= n:
        left = mid + 1
    else:
        right = mid - 1
        
print(left-1)