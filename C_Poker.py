import heapq

test = int(input())

for _ in range(test):
    n = int(input())
    powers = list(map(int, input().split()))

    heap = []
    max_power = 0

    for power in powers:
        if power:
            heapq.heappush(heap, -power)
        elif heap:
            current_power = heapq.heappop(heap)
            max_power += -current_power

    print(max_power)