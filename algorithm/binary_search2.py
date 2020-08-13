T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    query = list(map(int, input().split()))
    answer = []
    
    for q in query:
        left = 0
        right = len(data)-1
        diff = 2100000000
        while left <= right:
            mid = (left + right) // 2
            
            tmp = data[mid] - q
            if abs(tmp) < diff:
                diff = abs(tmp)
                result = data[mid]
            elif abs(tmp) == diff and tmp<0:
                diff = abs(tmp)
                result = data[mid]
                
            if data[mid] == q:
                break
            elif data[mid] > q:
                right = mid-1
            elif data[mid] < q:
                left = mid+1
            
        if left > right:
            answer.append(result)
        else:
            answer.append(data[mid])
            
    print(*answer)
                
                
    