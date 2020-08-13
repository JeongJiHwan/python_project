T = int(input())

for _ in range(T):
    ls = list(map(int, input().split()))
    find = list(map(int, input().split()))
    result = []
    for i in find:
        first = 0
        last = len(ls)-1
        found = False

        while first<=last and not found:
            mid = (first+last)//2
            if ls[mid] == i:
                result.append(mid)
                found = True
            else:
                if i< ls[mid]:
                    last = mid-1
                else:
                    first = mid+1
        if not found:
            result.append(-1)
    print(*result)