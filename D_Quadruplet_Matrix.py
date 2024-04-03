for _ in range(int(input())):
    n = int(input())
    a=[]
    for i in range(n):
        temp= input()
        a.append(temp)
    ans=0
    
    for i in range(n):
        for j in range(n):
            sumOnes = int(a[i][j])+int(a[j][n-i-1])+int(a[n-i-1][n-j-1])+int(a[n-j-1][i])
            sumZeros = 4-sumOnes
            ans+=min(sumOnes, sumZeros)
    print(ans//4)