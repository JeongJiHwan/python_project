def calcDist(ls, dic):
    dist = []
    for i in range(len(ls)-1):
        x1,y1,z1 = ls[i]
        for j in range(i+1, len(ls)):
            x2,y2,z2 = ls[j]
            if x1 != x2:
                dist.append(abs(x2-x1) + abs(z2-z1))
    if not dist:
        return 2100000000
    minval = min(dist)
    if minval not in dic:
        dic[minval] = 1
    else:
        dic[minval] +=1
    return minval

def minDist(ls, dic):
    if len(ls)==1:
            return 2100000000
    if len(ls) <= 3:
        return calcDist(ls, dic)
    else:
        mid = len(ls)//2
        L = ls[0:mid]
        print(L)
        R = ls[mid:]
        print(R)
        C = []
        sig = min(minDist(L, dic), minDist(R, dic))
        
        for pt in L[::-1]:
            if pt[2] > ls[mid][2]-sig:
                C.append(pt)
            else:
                break
        for pt in R:
            if pt[2] < ls[mid][2] + sig:
                C.append(pt)
            else:    
                print((cow+horse).sort(key=lambda e:e[2]))
                break
        tmp = calcDist(C, dic)
        return min(sig, tmp)
        
T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    c1, c2 = map(int, input().split())
    
    cow = [(c1,0,i) for i in map(int, input().split())]
    horse = [(c2,0,i) for i in map(int, input().split())]
    
    dic = {}
    
    ls = cow + horse
    ls.sort(key = lambda e:e[2])
    minDist(ls, dic)
    print(dic)