test=int(input())

for i in range(test):
    n,k=map(int, input().split(" "))

    string=input()
    Min= float('inf')
    for i in range(3):
        change=0
        for j in range(n):
            if string[j]!= "RGB"[(j+i)%3]:
                change+=1
            
            if j+1>=k:
                Min=min(Min, change)
                if string[j+1-k]!="RGB"[(j+i+1-k)%3]:
                    change-=1
    print(Min)

