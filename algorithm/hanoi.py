def H(n,A,B,C):
    if n==1:
        C[1].append(A[1].pop())
        print(*A[0],'->', *C[0])
        return
    H(n-1, A, C, B)
    H(1, A, B, C)
    H(n-1, B, A, C)
    
T = int(input())

for _ in range(T):
    num = int(input())
    A = [['A'],[i for i in range(num, 0, -1)]]
    B = [['B'],[]]
    C = [['C'],[]]
    H(num, A, B, C)