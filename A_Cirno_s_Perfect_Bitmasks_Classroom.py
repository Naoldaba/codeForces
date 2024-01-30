test=int(input())

for _ in range(test):
    num = int(input())
    if num % 2:  
        if num > 1:
            print("1")
        else:
            print("3")
            
    else:
        if not (num & (num - 1)):
            print(num + 1)
        else:  
            print(num & ~(num - 1))


