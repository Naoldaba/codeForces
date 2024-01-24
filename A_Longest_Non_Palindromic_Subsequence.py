
test = int(input())

for _ in range(test):
    flag = 0
    string = input()
    start = string[0]
    for i in range(len(string)):
        if start != string[i]:
            flag = 1
            break
    if flag == 0:
        print(-1)
    else:
        print(len(string) - 1)