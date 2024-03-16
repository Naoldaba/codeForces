import heapq

n, k, q = map(int, input().split())
arr = list(map(int, input().split()))
min_heap = []
Set = set()

for i in range(q):
    command, Id = map(int, input().split())

    if command == 1:
        if len(min_heap) < k:
            heapq.heappush(min_heap, (arr[Id - 1], Id))
            Set.add(Id)

        else:
            heapq.heappush(min_heap, (arr[Id - 1], Id))
            Set.add(Id)
            elem, min_id = heapq.heappop(min_heap) 
            Set.remove(min_id)
    else:
        if Id in Set:
            print('YES')
        else:
            print('NO')
