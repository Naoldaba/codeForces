size = int(input())  

mat = []
for _ in range(size):
    row = list(map(int, input().split())) 
    mat.append(row)


total_sum = 0

for i in range(size):
    total_sum += mat[i][i]  
    total_sum += mat[i][size - 1 - i]  
    total_sum += mat[size // 2][i]  
    total_sum += mat[i][size // 2]  


total_sum -= 3 * mat[size // 2][size // 2]

print(total_sum)  
