import heapq


T = int(input())

for _ in range(T):
    cnt = int(input())
    hq_min = []
    hq_max = []
    
    for i in range(cnt):        
        num = int(input())        
        if num>0:
            check = [True]
            heapq.heappush(hq_min, (num, check))
            heapq.heappush(hq_max, (-num, check))
        elif num == -1:
            pop_num = heapq.heappop(hq_min)
            while not pop_num[1][0]:
                pop_num = heapq.heappop(hq_min)
            pop_num[1][0]=False
            print(pop_num[0])
        else:
            pop_num = heapq.heappop(hq_max)
            while not pop_num[1][0]:
                pop_num = heapq.heappop(hq_max)
            pop_num[1][0]=False
            print(-pop_num[0])
            