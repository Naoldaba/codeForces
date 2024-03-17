test=int(input())

for i in range(test):
    n=int(input())
    arr=[]
    for i in range(2):
        arr.append(list(input()))
    i=j=0
    string=arr[0][0]
    ways=temp=1

    while j<n-1:
        if i==0:
            if arr[i][j+1]=="1" and arr[i+1][j]=="0":
                string+=arr[i+1][j]
                i+=1
                ways=temp
            elif arr[i][j+1]==arr[i+1][j]:
                string+=arr[i][j+1]
                j+=1
                temp+=1
            else:
                string+=arr[i][j+1]
                temp=1
                j+=1
        else:
            string+=arr[i][j+1]
            j+=1
    if i==0:
        string+=arr[1][n-1]
        ways=temp

    print(string)
    print(ways)
    