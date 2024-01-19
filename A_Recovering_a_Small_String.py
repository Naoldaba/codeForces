test=int(input())
def func(n):
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                if (i+j+k)-(3*96)==n:
                    return chr(i)+chr(j)+chr(k)
for i in range(test):
    n=int(input())
    print(func(n))

