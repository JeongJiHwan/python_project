class Set:    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, n):
        if self.parent[n]==n:
            return n

        return self.find(self.parent[n])

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return
        if self.rank[u]>self.rank[v]:
            u,v = v,u
        self.parent[u]=v
        if self.rank[u]==self.rank[v]:
            self.rank[v]+=1
        
T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    s = Set(N)
    ls = []
    for _ in range(M):
        tmp = list(map(int, input().split()))
        ls.append(tmp)
    ls.sort(key=lambda e:e[2])
    
    total = 0
    for u,v,c in ls:
        if s.find(u) != s.find(v):
            s.union(u,v)
            total += c
    print(total)