test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    max_element = max(arr)
    operations = 0

    for num in arr:
        operations = max(operations, max_element-num)

    print(operations)