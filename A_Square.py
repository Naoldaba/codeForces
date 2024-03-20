test=int(input())
for i in range(test):
    matrix=[]
    for i in range(4):
        row=list(map(int, input().split(" ")))
        matrix.append(row)
    matrix=sorted(matrix)
    area=(matrix[1][1]-matrix[0][1])**2
    print(area)
