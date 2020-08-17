import heapq

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    EL = []
    distL = []
    for m in range(M):
        U,V,C = map(int,input().split())
        EL.append([U,V,C])
    for n in range(N):
        distL.append(9999999)
    distL[0] = 0
    PQ = [0]
    while len(PQ) != 0:
        U = heapq.heappop(PQ)
        for el in EL:
            if distL[el[1]] > distL[el[0]] + el[2]:
                distL[el[1]] = distL[el[0]] + el[2]
                heapq.heappush(PQ,V)
    print(distL[N-1])