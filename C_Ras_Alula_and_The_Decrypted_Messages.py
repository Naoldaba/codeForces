
test=int(input())
for _ in range(test):
    n, m = map(int, input().split())

    s=input()
    w=input()

    if len(s)<len(w):
        print("NO")
    else:
        w_ord_sum=0
        sub_str_sum=0
        for i in range(len(w)):
            w_ord_sum+=ord(w[i])
            sub_str_sum+=ord(s[i])
        if w_ord_sum==sub_str_sum:
            print("YES")
        else:
            l=0
            flag=False
            for i in range(len(w), len(s)):
                sub_str_sum+=ord(s[i])
                sub_str_sum-=ord(s[l])
                if sub_str_sum==w_ord_sum:
                    flag=True
                    break
                l+=1
            print("YES") if flag else print("NO")
        
        