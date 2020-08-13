def dijkstra(G, dist, s):
    queue = []
    for i in range(len(G)):
        tmp = [2100000000]
        dist[i] = tmp
        queue.append((tmp,i))
    dist[s][0] = 0
    queue.sort(key = lambda e : e[0][0])

    while queue:
        d, u = queue.pop(0)

        for v,s in G[u]:
            if dist[v][0] > d[0] + s:
                dist[v][0] = d[0] + s
        
        queue.sort(key = lambda e : e[0][0])
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    ls = [[] for i in range(N)]

    for i in range(M):
        u, v, c = map(int, input().split())
        ls[u].append((v,c))
    
    dist = [0 for i in range(N)]

    dijkstra(ls, dist, 0)

    if dist[N-1][0] == 2100000000:
        print(-1)
    else:
        print(dist[N-1][0])
