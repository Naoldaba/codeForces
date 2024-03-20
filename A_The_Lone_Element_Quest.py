t = int(input()) 

for _ in range(t):
    n = int(input())  
    numbers = list(map(int, input().split()))  
    
  
    counts = {}
    for i, num in enumerate(numbers):
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    unique_num = None
    for num, count in counts.items():
        if count == 1:
            unique_num = num
            break
    
    
    for i, num in enumerate(numbers):
        if num == unique_num:
            print(i + 1)  
            break
