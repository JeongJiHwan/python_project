N = int(input())
ls = []
for _ in range(N):
    s,f = map(int, input().split())
    ls.append((s,f))
    
ls.sort(key = lambda e : e[1])

fin = ls[0][1]
cnt = 1

for i in ls[1:]:
    if i[0] >= fin:
        fin = i[1]
        cnt+=1
print(cnt)