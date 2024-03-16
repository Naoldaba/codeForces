test = int(input())
for _ in range(test):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, arr_len, 2):
        arr[i] = -arr[i]
    flag = False  
    prefix = 0
    seen_prefixes = set()
    seen_prefixes.add(prefix)
    for i in range(arr_len):
        prefix += arr[i]
        if prefix in seen_prefixes:
            print("YES")
            flag = True 
            break
        else:
            seen_prefixes.add(prefix)
    if not flag:  
        print("NO")
