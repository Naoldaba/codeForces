test=int(input())
for i in range(test):
    matrix=[]
    for i in range(3):
        row=list(input())
        matrix.append(row)  

    dic1={"A":0,"B":0,"C":0}
    for r in range(3):
        dic2=dic1.copy()
        for c in range(3):
            if matrix[r][c]!="?":
                dic2[matrix[r][c]]=1
        for i,j in dic2.items():
            if dic2[i]==0:
                print(i)
                break
            

