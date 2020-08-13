ls=[(0,1), (1,0)]
def BFS():
    queue = []
    queue.append((0,0))
    visit[0][0] = 1
    while queue:
        y,x = queue.pop(0)
        
        for i,j in ls:
            toy = y+i
            tox = x+j
            if toy in range(0,len(table)) and tox in range(0,len(table[0])):
                if visit[toy][tox] < visit[y][x] + table[toy][tox]:
                    visit[toy][tox] = visit[y][x] + table[toy][tox]
                    queue.append((toy,tox))

T = int(input())

for _ in range(T):
    n,m = map(int, input().split())
    
    table = []
    visit = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        table.append(tmp)
    
    BFS()
    print(visit[n-1][m-1])