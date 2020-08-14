t = int(input())
for _ in range(t):
    a = '0' + input()
    b = '0' + input()
    n = len(a)
    m = len(b)
    
    lcs = [[0]*m for _ in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            if a[i]==b[j]:
                lcs[i][j] = max(lcs[i-1][j-1]+1, lcs[i-1][j], lcs[i][j-1])
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    print(lcs[-1][-1])