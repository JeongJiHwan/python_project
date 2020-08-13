def BFS(v,List, Check):
    queue = []
    queue.append(v)
    
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        
        for i in List[v]:
            if not Check[i]:
                queue.append(i)
                Check[i]=True
                
T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    List = [[] for _ in range(N)]
    for i in range(M):
        u,v = map(int, input().split())
        List[u].append(v)

    for i in range(N):
        List[i].sort()
    
    Check = [False]*N
    Check[0] = True
    
    print()