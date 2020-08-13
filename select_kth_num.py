import random
def select_min(ls, k):
    x = random.randint(0,len(ls)-1)
    sl=[]
    sv=[]
    sr=[]
    for i in ls:
        if i < ls[x]:
            sl.append(i)
        elif i > ls[x]:
            sr.append(i)
        else:
            sv.append(ls[x])
    if k <= len(sl):
        return select_min(sl, k)
    elif k>len(sl) and k<=len(sl)+len(sv):
        return ls[x]
    else:
        return select_min(sr, k-(len(sl)+len(sv)))

def select_max(ls, k):
    x = random.randint(0,len(ls)-1)
    sl=[]
    sv=[]
    sr=[]
    for i in ls:
        if i > ls[x]:
            sl.append(i)
        elif i < ls[x]:
            sr.append(i)
        else:
            sv.append(ls[x])
    if k <= len(sl):
        return select_max(sl, k)
    elif k>len(sl) and k<=len(sl)+len(sv):
        return ls[x]
    else:
        return select_max(sr, k-(len(sl)+len(sv)))

T = int(input())

for _ in range(T):
    ls = list(map(int, input().split()))
    k = int(input())
    print(abs(select_max(ls, k) - select_min(ls, k)))