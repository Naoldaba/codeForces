Mod = (10**9) + 7

test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = sm = 0
    for i in range(len(arr)):
        sm = max(arr[i], sm + arr[i])
        ans= max(sm, ans)

    ans %= Mod

    arr_sum = ((sum(arr) - ans) + Mod) % Mod
    k_times = (pow(2, k, Mod) * ans) % Mod
    output = (arr_sum + k_times) % Mod

    print(output)

        
# 7, 7, 14, 28, 56, 


# Mod = (10**9) + 7

# t = int(input())
# for _ in range(t):
#     n, k, ans, sm, Sum = 0, 0, 0, 0, 0
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))

#     ans = sm = 0
#     for i in range(len(arr)):
#         Sum+=arr[i]
#         sm = max(arr[i], sm + arr[i])
#         ans= max(sm, ans)
        
#     Sum = ((Sum - ans) + Mod) % Mod
#     ans %= Mod
#     print((Sum % Mod + ((pow(2, k, Mod) % Mod * ans % Mod) % Mod) % Mod) % Mod)
    
