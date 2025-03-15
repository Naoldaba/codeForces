tests =int(input())

for _ in range(tests):
    n = int(input())
    array = list(map(int, input().split()))

    total = sum(array)
    if total%2 == 0:
        print(0)
        continue

    min_operations = float('inf')
    for x in array:
        operations_count = 0
        while x%2 == (x//2) %2:
            operations_count += 1
            x //= 2
        min_operations = min(min_operations, operations_count+1)
    
    print(min_operations)