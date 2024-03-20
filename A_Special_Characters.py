test=int(input())
for _ in range(test):
    n=int(input())
    String=''
    if n%2==0:
        for i in range(n//2):
            String+=(2*chr(ord('A')+(i%26)))
        print("YES")
        print(String)
        
    else:
        print("NO")
        

