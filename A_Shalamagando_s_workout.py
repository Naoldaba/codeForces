test = int(input())
workout_reps = list(map(int, input().split()))

chest = 0
biceps = 0
back = 0

for j in range(test):
    if j % 3 == 0:
        chest += workout_reps[j]
    elif j % 3 == 1:
        biceps += workout_reps[j]
    else:
        back += workout_reps[j]

if chest > biceps and chest > back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
else:
    print("back")
