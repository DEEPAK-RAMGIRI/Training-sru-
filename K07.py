# cheap travels
n,m,a,b = map(int,input().split()) 
cost1= (n // m)* b + (n % m) * a
cost2 = n*a
cost3 =  ((n // m) + 1) * b
print(min(cost1,cost2,cost3))
