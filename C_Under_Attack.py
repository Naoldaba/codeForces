t = int(input())  

for _ in range(t):
    n, m = map(int, input().split())  
    chessboard = []
    for _ in range(n):
        row = list(map(int, input().split()))  
        chessboard.append(row)

    maxSum = 0  

    for i in range(n):
        for j in range(m):
            currentSum = chessboard[i][j]
            for k in range(1, min(n-i, m-j)):
                currentSum += chessboard[i+k][j+k]
            for k in range(1, min(n-i, j+1)):
                currentSum += chessboard[i+k][j-k]
            for k in range(1, min(i+1, m-j)):
                currentSum += chessboard[i-k][j+k]
            for k in range(1, min(i+1, j+1)):
                currentSum += chessboard[i-k][j-k]
                
            maxSum = max(maxSum, currentSum)

    print(maxSum)