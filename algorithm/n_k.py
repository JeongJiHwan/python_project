def pow(n,k,m):
    if k==0:
        return 1
    if k==1:
        return n
    x = pow(n,k//2,m) % m
    if k%2==1:
        return (x*x*n)%m
    else:
        return (x*x)%m
    
T = int(input())

for _ in range(T):
    n,k,m = map(int, input().split())
    
    if k==0 or n==1:
        print(1)
    else:
        print(pow(n,k,m))