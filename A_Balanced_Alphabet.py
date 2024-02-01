test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    
    chars = 'abcdefghijklmnopqrstuvwxyz'
    freq = n // k
    rem = n % k

    string = ''
    for i in range(k):
        string += chars[i] * freq

    string += chars[:rem]

    print(string)