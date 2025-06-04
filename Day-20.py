# DP With 2d Array
#Using recursion
coin =  [1,2,3]
coin =[2,3,4,5,7]
amt= 12
arr = []
def coin_change(n,sums,new):
    if sums == 0: 
        arr.append(new)
        return
    if sums < 0 or n < 0:
        return
    # print(sums)
    coin_change(n,sums-coin[n],new + [coin[n]])
    coin_change(n-1,sums,new) 
    
coin_change(len(coin)-1,amt,[])
print(arr)

#using dp 2d dp 
#memoization
coin =  [1,2,3]
coin =[2,3,4,5,7]
amt= 12
dp = [[-1 for _ in range(amt +1)] for  _ in range(len(coin))]
def coin_change_dp(sums,n):
    if sums == 0:
        return 1
    elif sums < 0 or n < 0:
        return 0
    elif dp[n][sums] != -1: return dp[n][sums]
    dp[n][sums] = (coin_change_dp(sums-coin[n],n) + coin_change_dp(sums,n-1))
    return dp[n][sums]
# print("no of ways coin change",coin_change_dp(amt,len(coin)-1))


# Finding minimum change
coin =  [1,2,3]
amt= 4
coin =[2,3,4,5,7]
amt= 12
dp = [[-1 for _ in range(amt + 1)] for _ in range(len(coin) + 1)]
def min_coin_change(n,sums):
    if sums == 0: return 0
    elif sums < 0 or n < 0: return float("inf")
    if dp[n][sums] != -1: return dp[n][sums]
    with_value = 1 + min_coin_change(n,sums-coin[n])
    with_out_value = min_coin_change(n-1,sums)
    dp[n][sums] = min(with_value,with_out_value)
    return dp[n][sums]
# print(min_coin_change(len(coin)-1,amt))


def coinChange(coins,amount):
    l = [amount+1] * (amount+1)
    l[0] = 0
    for i in range(1,amount+1):
        for j in coins:
            if i-j >= 0:
                l[i] = min(l[i],1+l[i-j])
    return -1 if l[-1] == amount+1 else l[-1]
# print(coinChange(coin,amt))


# Length of the longest subsequence
s1 = "ababd"
s2 = "adabd"
# s2 = 'a'
final = 0
for i in range(len(s2)):
    count = -1
    for j in range(len(s1)):
        if s2[i] == s1[j]: 
            count+=1
            print(s2[i],s1[j])
        else:final = max(final,count)
print(final)
        





