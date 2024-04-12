t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Read the value of n for the current test case

    if n % 2 == 1:  # Check if n is odd
        print("No")
        continue

    pairs = []
    for i in range(1, 2 * n + 1):
        if i + n <= 2 * n:
            pairs.append((i, i + n))
        else:
            pairs.append((i, i + n - 2 * n))

    print("Yes")
    for pair in pairs:
        print(pair[0], pair[1])