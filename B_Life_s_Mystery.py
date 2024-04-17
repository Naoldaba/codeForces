
stack=[]
string=input()
for i in range(len(string)):
    
    if stack and stack[-1]==string[i]:
        stack.pop()
    else:
        stack.append(string[i])
print(''.join(stack))