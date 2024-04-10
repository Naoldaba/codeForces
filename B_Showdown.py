test=int(input())

for _ in range(test):

    pridiction=input()
    score_a, score_b=0,0
    rem_a, rem_b=5,5
    turns=0

    i=0
    while i<10:
        if score_a > score_b + rem_b or score_b > score_a + rem_a:
            print(turns)
            break
        if pridiction[i] =='1' or pridiction[i]=='?':
            score_a+=1
            rem_a-=1
        elif pridiction[i]=='0':
            rem_a-=1
        turns+=1
        
        i+=1
        if score_a > score_b + rem_b or score_b > score_a + rem_a:
            print(turns)
            break
        if pridiction[i] =='1':
            score_b+=1
            rem_b-=1
        elif pridiction[i]=='0' or pridiction[i]=='?':
            rem_b-=1
        turns+=1
    else:
        print(10)
   
