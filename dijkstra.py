import heapq

def dijkstra(G, s):
    hq = []
    for i in range(len(G)):
        tmp = [2100000000]
        dist[i] = tmp
        hq.append((tmp, i))
    dist[s][0]=0
    while hq:
        dis, u = heapq.heappop(hq)

        for v in G[u]:
            if dist[v[0]][0] > dis[0] + v[1]:
                dist[v[0]][0] = dis[0] + v[1]
                
T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    List = [[] for x in range(N)]
    
    for i in range(M):
        u,v,c = map(int, input().split())
        List[u].append((v,c))
        
    dist = [0 for i in range(N)]
    dijkstra(List, 0)
    
    if dist[N-1][0]==2100000000:
        print(-1)
    else:
        print(dist[N-1][0])