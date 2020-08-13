T = int(input())
for _ in range(T):
    n = int(input())
    
    check = [False for i in range(n)]
    ls = []
    for i in range(n):
        s,t = map(int, input().split())
        ls.append([s,t])
    
    ls.sort(key = lambda e : e[1])
    time = ls[0][1]
    cnt = 1
    
    for i in range(1, len(ls)):
        if ls[i][0] > time:
            time = ls[i][1]
            cnt+=1
            
    print(cnt)
            
            