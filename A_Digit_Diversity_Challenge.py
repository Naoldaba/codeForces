lower, upper = map(int, input().split())

for num in range(lower, upper + 1):
    digit_set = set()
    temp_num = num
    is_valid = True

    while temp_num > 0:
        digit = temp_num % 10
        if digit in digit_set:
            is_valid = False
            break
        digit_set.add(digit)
        temp_num //= 10

    if is_valid:
        print(num)
        break
else:
    print(-1)
