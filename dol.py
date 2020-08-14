def dol(n):
    ls = [0]*n
    ls = [0] + ls
    
    for i in range(1, len(ls)):
        if i==1:
            ls[i] = 1
        elif i==2:
            ls[i] = 2
        elif i==3:
            ls[i]=4
        else:
            ls[i] = (ls[i-1] + ls[i-2] + ls[i-3]) % 1904101441
    return ls[n]

T = int(input())

for _ in range(T):
    n = int(input())   
    
    print(dol(n))
    