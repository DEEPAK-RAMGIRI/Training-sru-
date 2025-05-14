# a = [2,5,6,7,2,1,4,3,6]
# #method 01
# def function(a,x,ans):
#     if x == len(a):
#         return ans
#     elif not a[x] & 1:
#         ans+=a[x]
#     return function(a,x+1,ans)

# #method 02
# def function2(a,i):
#     if i == len(a):
#         return 0
#     return (a[i]  if not a[i] & 1 else 0) + function2(a,i+1)

# ans = 0
# print(function(a,0,ans))
# print(function2(a,0))






# def reverse(no,ans= 0):
#     if no == 0:
#         return ans
#     ans = ans*10 + no%10
#     return reverse(no//10,ans)
# no = 153
# print(reverse(no))

# def loop(a,i,count = 0):
#     if i == len(a):
#         return count
#     count += prime(a[i],2)
#     return loop(a,i+1,count)

# def prime(a,i):
#     if i == (int(a ** 0.5) + 1):
#         return 1
#     elif a % i == 0: return 0
#     return prime(a,i+1)

# a = [2,4,5,6,7,8,9,13]
# a = [13,17,21,23,22,7,29]
# print(loop(a,0))

def trueorfalse(n,count = 0):
    if n == 1:
        return True
    elif n <= 0:
        return False 
    return trueorfalse(n-3) or trueorfalse(n-5)


# Counting minimum no of subtraction to get 1
def trueorfalse1(n, count=0):
    if n == 1:
        return count
    elif n <= 0:
        return 99999 
    return min(trueorfalse1(n - 3, count + 1), trueorfalse1(n - 5, count + 1))

n = 4
ans = trueorfalse1(n)
if ans == 99999:
    print(False)
else:
    print(ans)

    


