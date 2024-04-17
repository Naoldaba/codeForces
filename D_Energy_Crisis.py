n, k =map(int, input().split())
acc=list(map(int, input().split()))

l, r= 0, max(acc)

while r - l > 1e-6:
    mid=(l+r)/2
    Sum=0
    for a in acc:
        if a < mid:
            Sum+=(mid-a)/((mid-a)-k/100)
    if Sum<=mid:
        l=mid
    else:
        r=mid

print(l)