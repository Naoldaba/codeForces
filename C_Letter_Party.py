n, k = map(int, input().split(" "))
string = input()

a_count = 0
b_count = 0
l = 0
ans = 0

for i in range(len(string)):
    if string[i] == "a":
        a_count += 1
    else:
        b_count += 1

    while min(a_count, b_count) > k and l <= i:
        if string[l] == "a":
            a_count -= 1
        else:
            b_count -= 1
        l += 1

    ans = max(ans, i - l + 1)

print(ans)