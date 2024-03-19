# n = int(input())
# names = {}

# for _ in range(n):
#     request = input().strip()

#     if request in names:
#         names[request] += 1
#         new_name = f"{request}{names[request]}"
#         print(new_name)
#     else:
#         names[request] = 0
#         print("OK")

t=int(input())
Map={}
for i in range(t):
    name=input()
    if name not in Map:
        print("OK")
        Map[name]=1
    else:
        print(f'{name}{Map[name]}')
