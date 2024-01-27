test = int(input())

for _ in range(test):
    string = input()
    Len=len(string)
    if string == string[:Len//2] * 2:
        print("YES")
    else:
        print("NO")