from collections import defaultdict

test = int(input())

for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count_a = defaultdict(int)
    count_b = defaultdict(int)
    
    idx = 0
    while idx < n:
        val = a[idx]
        cnt = 0
        while idx < n and a[idx] == val:
            cnt += 1
            idx += 1
        count_a[val] = max(count_a[val], cnt)
    
    idx = 0
    while idx < n:
        val = b[idx]
        cnt = 0
        while idx < n and b[idx] == val:
            cnt += 1
            idx += 1
        count_b[val] = max(count_b[val], cnt)
    
    ans = 0
    for val, val_cnt_in_a in count_a.items():
        val_cnt_in_b = count_b[val]
        ans = max(ans, val_cnt_in_a + val_cnt_in_b)
    
    for val, val_cnt_in_b in count_b.items():
        val_cnt_in_a = count_a[val]
        ans = max(ans, val_cnt_in_a + val_cnt_in_b)
    
    print(ans)
    