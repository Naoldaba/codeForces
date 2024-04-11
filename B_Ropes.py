
n, k= map(int, input().split())
arr=[]

for i in range(n):
    In=int(input())
    arr.append(In)

def pieces(rope_lengths, length):
    count = 0
    for rope in rope_lengths:
        count += rope // length
    return count


left = 0
right = max(arr)

while right - left > 1e-6:
    mid = (left + right) / 2
    if pieces(arr, mid) >= k:
        left = mid
    else:
        right = mid

print(left)





   