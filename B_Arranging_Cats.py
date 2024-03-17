test=int(input())
for i in range(test):
    boxes=int(input())
    initial_pos=list(map(int, list(input())))
    final_pos=list(map(int, list(input())))
    init_sum=sum(initial_pos)
    final_sum=sum(final_pos)
    diff=abs(init_sum-final_sum)

    offset=0

    for i in range(len(final_pos)):
        if final_pos[i]!=initial_pos[i]:
            offset+=1
    ans=diff+ (offset-diff)//2

    print(ans)