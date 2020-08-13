import sys
sys.setrecursionlimit(1000000)

def DFS(v, List, Check):
    print(v, end=' ')
    for i in List[v]:
        if not Check[i]:
            Check[i] = True
            DFS(i, List, Check)

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    List = [[] for _ in range(N)]
    for i in range(M):
        u,v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
    for i in range(N):
        List[i].sort()
    
    Check = [False]*N
    Check[0] = True
    DFS(0, List, Check)
    print()