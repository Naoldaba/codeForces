def solve():
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    
    if n == 1:
        print("YES")
        print(strings[0])
        return
    
    strings.sort(key=len)
    for i in range(1, n):
        a = strings[i]
        b = strings[i - 1]
        if b not in a:
            print("NO")
            return
    
    print("YES")
    print("\n".join(strings))

t = 1
for _ in range(t):
    solve()
