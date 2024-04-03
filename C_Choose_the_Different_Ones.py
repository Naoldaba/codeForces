from collections import Counter

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    nums_1 = list(map(int, input().split()))
    nums_2 = list(map(int, input().split()))

    freq_map_1 = Counter(nums_1)
    freq_map_2 = Counter(nums_2)

    count_1 = sum(1 for num in range(1, k + 1) if freq_map_1[num] > 0)
    count_2 = sum(1 for num in range(1, k + 1) if freq_map_2[num] > 0)

    flag = 0
    for i in range(1, k + 1):
        flag = 0
        if freq_map_1[i] > 0:
            flag = 1
        if freq_map_2[i] > 0:
            flag = 1
        if flag == 0:
            print("NO")
            break
    else:
        if count_1 >= k // 2 and count_2 >= k // 2:
            print("YES")
        else:
            print("NO")
