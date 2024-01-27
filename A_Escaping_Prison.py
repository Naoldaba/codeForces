test=int(input())
for _ in range(test):
    n, h= map(int, input().split())
    total_height=0
    for i in range(n):
        w, l=map(int, input().split())
        total_height+=max(w,l)
    if total_height>=h:
        print("YES")
    else:
        print("NO")
        
        
