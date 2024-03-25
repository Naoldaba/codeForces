from collections import defaultdict, deque

test = int(input())
for _ in range(test):
    input()
    n, k = list(map(int, input().split()))
    friends_room = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()
    times_friends_reach_rooms = [float('inf')] * (n + 1)

    for frd_room in friends_room:
        queue.append((frd_room, 0))
        times_friends_reach_rooms[frd_room] = 0

    while queue:
        frd_room, time = queue.popleft()

        for neighbor in graph[frd_room]:
            if times_friends_reach_rooms[neighbor] == float('inf'):
                times_friends_reach_rooms[neighbor] = time + 1
                queue.append((neighbor, time + 1))

    flag = False
    queue = deque([(1, 0)])
    visited = set([1])

    while queue:
        room, time = queue.popleft()

        if time >= times_friends_reach_rooms[room]:
            continue

        if room != 1 and len(graph[room]) == 1:
            flag = True
            break

        for neighbor in graph[room]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, time + 1))

    if flag:
        print("YES")
    else:
        print("NO")
