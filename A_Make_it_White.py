t=int(input())
for _ in range(t):
    n=int(input())
    s=input().strip()
    l=s.find('B')
    r=s.rfind('B')
    if l==-1:
        print(0)
    else:
        print(r-l+1)
