T = int(input())

for _ in range(T):
    N,C = map(int, input().split())
    ls = []
    for i in range(N):
        w,v = map(int, input().split())
        d = w/v
        ls.append((w,v,d))
        
    ls.sort(key=lambda e:e[2], reverse=True)
    
    maxval=0
    limit = 0
    idx = 0
    while limit < C:
        if limit + ls[idx][1] > C:
            maxval += int(ls[idx][0] * ((C-limit) / ls[idx][1]))
            limit = C
        else:
            maxval += ls[idx][0]
            limit += ls[idx][1]
        idx+=1
    
    print(maxval)