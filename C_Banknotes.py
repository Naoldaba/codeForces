test_cases = int(input())

powers_of_10 = [0] * 10
powers_of_10[0] = 1
for i in range(1, 10):
    powers_of_10[i] = powers_of_10[i - 1] * 10

while test_cases > 0:
    test_cases -= 1
    size, limit = map(int, input().split())

    numbers = list(map(int, input().split()))

    result_sum = 0

    for i in range(size):
        if limit < 0:
            break

        occurrences = limit + 1
        if i != size - 1:
            occurrences = min(occurrences, powers_of_10[numbers[i + 1]] // powers_of_10[numbers[i]] - 1)

        limit -= occurrences
        result_sum += occurrences * powers_of_10[numbers[i]]

    print(result_sum)