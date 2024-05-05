test=int(input())

for _ in range(test):
    or_time=input().split(':')
    
    converted=str(int(or_time[0])%12)
    if int(or_time[0])==0 or int(or_time[0])==12:
        converted='12'
    # print(converted)
    if 0<=int(or_time[0])<=11:
        if len(converted)==1:
            converted='0'+converted
        print(converted+':'+or_time[1]+" "+ "AM")
    else:
        if len(converted)==1:
            converted='0'+converted
        print(converted+':'+or_time[1]+" "+ "PM")

