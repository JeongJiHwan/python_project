T = int(input())
for _ in range(T):
    ls = list(map(int, input().split()))
    
    maxval = 0
    total = 0
    for i in ls[::-1]:
        total += i
        if total > maxval:
            maxval = total
        if total < 0:
            total = 0
    if max(ls)<0:
        maxval = max(ls)
    print(maxval)