def dbro(l,n):
    dp = [0]*len(l)
    for i in range(1, n+1):
        if i==1:
            dp[i] = l[i]
        elif i%2==0: #짝수발판
            dp[i] = max(dp[i-1]+l[i], dp[i-2]+l[i], dp[i//2]+l[i])
        else:
            dp[i] = max(dp[i-1]+l[i], dp[i-2]+l[i])
    return dp[n]
        
T = int(input())

for _ in range(T):
    n = int(input())
    
    ls = list(map(int, input().split()))
    ls = [0] + ls
    
    print(dbro(ls, n))