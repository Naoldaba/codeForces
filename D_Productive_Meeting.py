import heapq

test = int(input())
for _ in range(test):
    num_people = int(input())
    sociability = list(map(int, input().split()))

    Heap=[]
    for i in range(num_people):
        if sociability[i]>0:
            tup=(-sociability[i], i+1)
            heapq.heappush(Heap, tup)
    
    result=[]
    while len(Heap)>1:
        p1=heapq.heappop(Heap)
        p2=heapq.heappop(Heap)

        result.append((p2[1], p1[1]))
        p1=(p1[0]+1, p1[1])
        p2=(p2[0]+1, p2[1])

        if p1[0]<0:
            heapq.heappush(Heap, p1)
        if p2[0]<0:
            heapq.heappush(Heap, p2)

    print(len(result))
    for a, b in result:
        print(a, b)
    

        