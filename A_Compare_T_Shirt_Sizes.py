test=int(input())
dic={"S":0, 'M': 1, "L": 2}

for _ in range(test):
    flag=''
    t_sizes=input().split()
    if t_sizes[0][-1]==t_sizes[1][-1]:
        if len(t_sizes[0])==len(t_sizes[1]):
            print('=')
        elif len(t_sizes[0])>len(t_sizes[1]):
            if t_sizes[0][-1]=="S":
                print('<')
            else:
                print('>')
        else:
            if t_sizes[0][-1]=="S":
                print('>')
            else:
                print('<')
        continue

    else:
        if dic[t_sizes[0][-1]]>dic[t_sizes[1][-1]]:
            print(">")
        else:
            print("<")
            
